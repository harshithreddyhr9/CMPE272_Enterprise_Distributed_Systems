'''
/* Copyrights: Sai Harshith Reddy */
Implementation of consistent hashing. 
Virtual Ids of the servers have been taken into consideration for this implementation
This distributed network consists of 4 nodes. Adding or removing the nodes has not been implemented
'''

from csv_parser import *
import requests
import sys

class HashRing:
    
    def __init__(self):
        
        self.server_portnumbers = ['5000', '5001', '5002', '5003'] 
        self.serverhashvalues = {}
        #self.hash_key=[]
        #self.hash_value=[]
        self.url = ['http://127.0.0.1:5000/api/v1/entries','http://127.0.0.1:5001/api/v1/entries','http://127.0.0.1:5002/api/v1/entries','http://127.0.0.1:5003/api/v1/entries']
        '''
        serverhashvalues = {
            '5000' : hash(5000)
            '5001' : hash(5001)
            '5002' : hash(5002)
            '5003' : hash(5003)
        }
        '''

    '''
    Hash the server portnums 
    '''
    def hashing_the_server_portnums(self):
        for portnum in self.server_portnumbers:
            self.serverhashvalues[portnum] = hash(portnum)
        
    '''
    To sort the list of portnums hash
    '''
    def sort(self):
        hashedport_nums = list(self.serverhashvalues.values())
        hashedport_nums.sort()
        
        self.selectserver(hashedport_nums)

    '''
    To select which node to post the data
    if hash(portnum) > self.hash_key
        post to the server
    '''
    def selectserver(self, hashedport_nums):
        
        count = 0
        
        
        #self.hash_key, self.hash_value = csv_parser_()
        self.noofentries = len(self.hash_key)    
        for key,value in zip(self.hash_key,self.hash_value):
            url = 'http://127.0.0.1:5000/api/v1/entries'
            for v in hashedport_nums:
                if v > key:
                    s = list(self.serverhashvalues.keys())[list(self.serverhashvalues.values()).index(v)]
                    if s == "5000":
                        url = 'http://127.0.0.1:5000/api/v1/entries'
                    elif s == "5001":
                        url = 'http://127.0.0.1:5001/api/v1/entries'
                    elif s == "5002":
                        url = 'http://127.0.0.1:5002/api/v1/entries'
                    elif s == "5003":
                        url = 'http://127.0.0.1:5003/api/v1/entries'    
                    break
                        
            self.postdata(url,key,value)

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
        with open("ch_output.txt", "w") as out_file:
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
    h.hashing_the_server_portnums()
    h.sort()
    h.getdata()
