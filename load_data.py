import numpy as np
from bs4 import BeautifulSoup as soup
import requests
import re
from translate import Translator

class DataLoader():
    def __init__(self, word, site, num_def, from_lang, to_lang):
        self.word = word
        self.site = site
        self.num_def = num_def
        self.from_lang = from_lang
        self.to_lang = to_lang

   
    def load_definition(self):
        """Loads data from different sources and merges them in the dictionary:
           return: results:dict"""
        results = dict()
        
        #form request for definitions
        url_name = self.site+self.word 
        page = requests.get(url_name).text
        bsobj = soup(page,'html.parser')

        definitions_all = bsobj.findAll(class_="DivisionDefinition")
        definitions = []
        
        #check if request has return        
        try:
            #find a gender of word
            gender = bsobj.findAll(class_="CatgramDefinition")[0].get_text()
            
            #take a word which was found
            head_page = bsobj.head.get_text()
            m =  re.search(r'Définitions : \w*', head_page).group(0)
            head = m.split(': ')[1]

            #take resuls for found word
            if self.word.lower() != head:
                results['note'] = f'Did you mean {head}?'
            
            results['head'] = head
            results['gender'] = gender
            
            #find translation of the word
            try:
                translator = Translator(from_lang = self.from_lang, to_lang = self.to_lang)
                results['translation'] = translator.translate(head)
            except:
                results['translation']  = "can't find translation"
                                
            #check if num_def of definitions exist
            if len(definitions_all)>0:
                n = self.num_def

                try:
                    if len(definitions_all) < n:
                        n = len(definitions_all)

                    for i in np.arange(n):
                        definitions.append(definitions_all[i].get_text()) 
                    results['definitions'] = definitions   

                except:
                    results['note'] = "Can't find definition for this word..."

        except:
            results['note'] = "Can't find this word! Please, try again."
        return results

    def out(self):
        
        """Returns pretty output
        return: out:str"""
        
        results = self.load_definition()
        out = ''
            
        for i in results.keys():
            if i in ['note','gender']:
                output_sector = f'\n{results[i]}\n'
            elif i == 'head':
                output_sector = f'\n{results[i].upper()}\n'
            elif i == 'definitions':
                output_sector = ''
                for defin in results[i]:
                    defin = defin.replace('\t','')
                    defin = defin.replace('\n','')
                    output_sector+=f'\n{defin}'

            else:
                output_sector = f'\n\n{i}: {results[i]}\n'
                            
            out += output_sector
        return out