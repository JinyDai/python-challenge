#First import the os module for read csv file
import os
import csv
#import the path for the budget data base
#PyPoll\02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv
pypoll_csv=os.path.join('PyPoll','02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')
#set the place holder for the calculation
total_votes=[]
candidates={}
vote_num=[]
vote_percent={}
winner=""
winner_count=0
#read the csv file
with open(pypoll_csv,"r",newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    #skip the first row to count the total votes
    header=next(csvreader,None)
    #start the loop to count the total votes
    for row in csvreader:
        total_votes.append(row[0])
    #calculate the total vote
        votes=len(total_votes)
    #print(f"Total Votes: {votes}")
    # use if condition to check the candidate names and add the votes of each candidate
        if row[2] in candidates.keys():
            candidates[row[2]] = candidates[row[2]] + 1
        else:
            candidates[row[2]] = 1
#for loop check the key value(candidate names) and value for each candidate's votes number to calculate the percentage 
for key,value in candidates.items():
    vote_percent[key]=round((value/votes)*100,2)
#for loop to compare each candidate's votes and get the winner
for key in candidates.keys(): 
    if candidates[key]>winner_count:
        winner=key
        winner_count=candidates[key]  
print("Election Results")
print("------------------------------")
print(f'Total votes: {votes}')
print("------------------------------")
for key,value in candidates.items():
    print(f"{key}: {vote_percent[key]}% ({value})")
print("------------------------------")
print(f"Winner: {winner}")

#write the txt file and saved in folder
output_path=os.path.join('PyPoll','pyPoll_output.txt')
with open(output_path,"w") as text:

    text.write("Election Results \n")
    text.write("------------------------------------- \n")
    text.write(f"Total Votes: {votes} \n")
    text.write("------------------------------------- \n")
    for key, value in candidates.items():
        text.write(f"{key}: {vote_percent[key]}% ({value}) \n")
    text.write("------------------------------------- \n")
    text.write(f"Winner: {winner} \n")
    text.write("------------------------------------- \n")
   

    

