import requests
from csv_parser import csv_parser_

if __name__=='__main__':
        count = 0
        #hash_key, hash_value = csv_parser_()
        url = 'http://127.0.0.1:5000/api/v1/entries'
        
        for hash_key, hash_value in csv_parser_():
                for i in range(len(hash_key)): 
                        data= {'hash_key':hash_key[i],
                                'hash_value':hash_value[i]
                        }
                        response = requests.post(url,data)
        
                
