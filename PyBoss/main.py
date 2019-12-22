#First import the os model for read csv file
import os
import csv
#import the path for the pyboss data
#PyBoss\02-Homework_03-Python_ExtraContent_Instructions_PyBoss_employee_data.csv
pyboss_csv=os.path.join('PyBoss','02-Homework_03-Python_ExtraContent_Instructions_PyBoss_employee_data.csv')
#set the dictionary for us state abbrev
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
#define the place holder 
emp=[]
first_name= []
last_name= []
dob=[]
ssn=[]
state=[]
#read the file
with open(pyboss_csv,"r",newline="") as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=",")
    print(csv_reader)
    #read the header row
    row=next(csv_reader)
    print(f"CSV Header: {row}")
    #example used in link https://stackoverflow.com/questions/50035827/split-one-column-in-csv-file-into-multiple-columns-while-grouping-the-data-in-py
    for row in csv_reader:
        emp.append(row[0])
        first_name.append(row[1].split(" ")[0])
        last_name.append(row[1].split(" ")[1])
        dob.append(row[2].split('-')[1]+"/"+row[2].split('-')[2]+"/"+row[2].split('-')[0])
        ssn.append("***-**"+row[3].split("-")[2])
        state.append(us_state_abbrev[row[4]])
    #check if get the correct list
    #print(emp)
    #print(first_name)
    #print(last_name)
    #print(dob)
    #print(ssn)
    #print(abbrstate)
#zip all the lists together into tuples
new_columns=zip(emp,first_name,last_name,dob,ssn,state)
output_path=os.path.join('Pyboss','pyBoss_new.csv')
with open(output_path,'w',newline='') as datafile:
    #initialize csv.writer
    csvwriter=csv.writer(datafile)
    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
    csvwriter.writerows(new_columns)