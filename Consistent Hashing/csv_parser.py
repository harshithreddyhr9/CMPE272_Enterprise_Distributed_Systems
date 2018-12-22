import csv,sys,requests


hash_key = []
hash_value = [] 


def csv_parser_(filename):
    with open(filename,mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)


        for row in csv_reader:
            hash_key.append(hash('{}:{}:{}'.format(row['Year'],row['Cause Name'],row['State'])))
            hash_value.append(row['Year']+" "+row['113 Cause Name']+" "+row['Cause Name']+" "+row['State']+" "+row['Deaths']+" "+row['Age-adjusted Death Rate'])
        return hash_key, hash_value        
            

