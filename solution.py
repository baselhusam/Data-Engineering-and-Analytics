# 1) Convert the JSON FILE (data1.json) to CSV File (data1.csv)

import json, csv #import json and csv libraries 

with open("data1.json",'r') as json_file_1: # open the file, 'r' because we want just to read it
    data = json.load(json_file_1) # load all the data from the json file to the "data" variable, variable type --> dictionary
    
records = data['records'] #Taking the value for the 'records' element, this value are the values for all records
    
with open("data1.csv",'w') as csv_file_1: # open the file, "w" for writing and creating one if doesn't exist
    writer = csv.writer(csv_file_1) # object for writing inside the file
    record = records[0] #Taking the first element "first record"
    writer.writerow(record.keys()) #and write the keys for that element, instead of writing (['id','name','age',etc])
    for record in records: #looping inside all the recrods recrod by record
        writer.writerow(record.values()) #writing every record
        
        
        
# 2) Convert the CSV FILE (data2.csv) to JSON FILE (data2.json)

with open('data2.csv','r') as csv_file_2: # open the file, 'r' for reading the file
    csv_reader = csv.DictReader(csv_file_2) # variable that contains all the data in file as a dictionary record by record
    all_data = {} # null dictionary for making the json file
    all_data['records'] = [row for row in csv_reader] # 'records' as key with a list as a value each element in the list is a dictionary
        
with open("data2.json",'w') as json_file_2: # open the file, 'w' for writing and creating one if doesn't exist
    json.dump(all_data,json_file_2) # put all the data inside the json file, using json.dump(all_the_data, the_file)



# 3) Load the data1 and data2 to df1, df2 dataframes respectively, usin numpy as panda libraries

import numpy as np
import pandas as pd

df1 = pd.read_csv('data1.csv') # load file1 into pandas dataframe
df2 = pd.read_csv('data2.csv') # load file2 into pandas dataframe



# 4) Print the number of the records in df1, and df2.

print("Number of records in df1:", df1.shape[0]) # taking the first element of the .shape function that represent the number of records or "rows"
print("Number of records in df2:", df2.shape[0]) 



# 5) Print the average of salary attribute in the df2

salary_mean = df2['salary'].mean() # calculate the mean of the salary attribute
print("The average of the salaray:", salary_mean) 



# 6) Normalize the age attribute in df2 using z-score normalization, and replace the original one with the normalized one.

def z_score(attribute):
    """ Calculate the z-score while z-score = (value - mean) / std
        and return the values """
    mean = np.mean(attribute)
    std = np.std(attribute)
    return [(value - mean) / std for value in attribute] #return a list with the normalized values

df2['age'] = z_score(df2['age']) # replace the original with the normalized