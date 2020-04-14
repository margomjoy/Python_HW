# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 09:08:38 2020

@author: Admin
"""

import os
import csv
import collections

csvpath = os.path.join('Resources', 'election_data.csv')
f=open('analysis.txt','w')
tot_v=0
county=[]
candidate=[]


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    for rw in csvreader:
        tot_v += 1
        county.append(rw[1])
        candidate.append(rw[2])
        
f.write('Election Result\n')
f.write('--------------------------\n')
f.write(f"Total Votes : {tot_v}\n")        
#print(tot_v)
#%%

counter=collections.Counter(candidate)
vote=[]

for cand, votes in counter.items():
    vote.append(votes)
    pct=round(((votes/tot_v)*100),2)
    f.write(f"{cand} : {pct} ({votes}) \n")
    #print(cand,":", pct, "(",votes,")") 
    
x=[key for key,val in counter.items() if val == max(counter.values())] 

f.write('---------------------------\n')
f.write(f"Winner : {x} \n") 
f.write('---------------------------\n')

f.close()   

