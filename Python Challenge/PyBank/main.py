# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:08:12 2020

@author: Admin
"""
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
tot=0
p_l=[]
date=[]
mx=0
mn=0
indx=0
indn=0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    for rw in csvreader:
        tot += 1
        date.append(rw[0])
        p_l.append(int(rw[1]))
               
        
#%%

changesarray = ([t - s for s, t in zip(p_l, p_l[1:])])
newarray = zip(date[1:],changesarray)


x=sum(changesarray)        
avg=x/len(changesarray)
mx=max(changesarray)
mn=min(changesarray) 
indx=changesarray.index(mx)
indn=changesarray.index(mn) 

  
#%% 

f=open('analysis.txt','w')
f.write("Finacial Analysis \n")
f.write("------------------------- \n")

f.write(f"Total Months: {tot} \n")
f.write(f"Total: {sum(p_l)} \n")
f.write(f"Average Change: {round(avg,2)} \n")  
f.write(f"Greatest Increase in Profits: {date[indx+1]} ({changesarray[indx]}) \n")
f.write(f"Greatest Decrease in Profits: {date[indn+1]} ({changesarray[indn]}) \n")

f.close()