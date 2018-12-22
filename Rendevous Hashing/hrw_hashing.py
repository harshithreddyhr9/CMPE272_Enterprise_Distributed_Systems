from csv_parser import csv_parser_
import requests
import sys
class HashRing:
    
    def __init__(self):
        
        self.serveraddress = ['5000', '5001', '5002', '5003'] 
        self.url = ['http://127.0.0.1:5000/api/v1/entries','http://127.0.0.1:5001/api/v1/entries','http://127.0.0.1:5002/api/v1/entries','http://127.0.0.1:5003/api/v1/entries']
        self.weights = {} 
        
        
        
        '''
        self.weights = {
            '5000' : hash(key:5000),
            '5001' : hash(key:5001),
            '5002' : hash(key:5002),
            '5003' : hash(key:5003),
        }
        '''

    '''
     w = hash(key, node)
     post the data to the node whose hash(key, node) is maximum 
    '''
    def calculate_weights(self):  
        
        self.noofentries = len(self.hash_key)
        for key,value in zip(self.hash_key,self.hash_value):
            for address in self.serveraddress:
                self.weights[address]= hash('{}:{}'.format(key, address))
            self.sortweights(key,value)

    '''
    To sort the weights of the key formed with all the nodes in the network
    '''
    def sortweights(self,key,value):
        weights_foreachkey = list(self.weights.values())
        weights_foreachkey.sort()
        
        url = self.selectmaxweight(weights_foreachkey)
        self.postdata(url,key,value)

    '''
    To select the maximum weight value of hash(key, node).
    '''

    def selectmaxweight(self, weights_foreachkey):
        
        self.noofentries = len(self.hash_key)    
        max_weight = max(weights_foreachkey)
        
        # Get the index using the value of a dictionary
        s = list(self.weights.keys())[list(self.weights.values()).index(max_weight)]
        
        # Check if the index is equal to any port num and set the url
        if s == "5000":
            url = 'http://127.0.0.1:5000/api/v1/entries'
           
        elif s == "5001":
            url = 'http://127.0.0.1:5001/api/v1/entries'
            
        elif s == "5002":
            url = 'http://127.0.0.1:5002/api/v1/entries'
            
        elif s == "5003":
            url = 'http://127.0.0.1:5003/api/v1/entries'    
            
        return url
                        
        

    '''
    To post the data to the server
    '''
    def postdata(self,url,key,value): 

        data= {'hash_key':key,
                    'hash_value': value
                    }
        response = requests.post(url,data)
        
        
    '''
    To get the data from all the servers
    '''
    def getdata(self):
        print("Uploaded all " +str(self.noofentries)+" entries.")
        print("Verifying the data.")
        with open("hrw_output.txt", "w") as out_file:
            for i in self.url:
                response = requests.get(i)
                out_file.write("GET " +str(i))
                out_file.write(response.text)
        print("GET "+str(i))
        print(response.text)
    '''
    To pass the csv file to the csv_parser.py to get the key,value pairs
    '''
    def passthefile(self,filename):
        self.hash_key, self.hash_value = csv_parser_(filename)


if __name__ == '__main__':
    
    h = HashRing()
    h.passthefile(sys.argv[1])
    h.calculate_weights()
    h.getdata()