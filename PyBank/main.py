# PyBank 
# import modules 
import os
import csv
import statistics

# file path 
budget_data_csv=os.path.join("Resources", "budget_data.csv")

# output text file 
import os.path
text_file="Output.txt"
txtpath=os.path.join("analysis",text_file)
f=open(txtpath,'w')

# variables 
months=0
net_total=0
greatestinc=0
greatestdec=0
maxmonth=''
minmonth=''

# Lists 
revchange=[]
monthchange=[]

# open csv 
with open(budget_data_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csvheader=next(csvreader)
    # Loop 
    for row in csvreader:
    # Total Months 
        months=months + 1
    # Total 
        net_total=net_total + int(row[1])
    # Greatest increase in Profits 
        if int(row[1]) > greatestinc:
            maxmonth=(row[0])
            greatestinc=int(row[1])
        elif int(row[1]) < greatestinc:
            maxmonth=(row[0])
            greatestinc=int(row[1])
    # Greatest Decrease in Profits
        if int(row[1]) > greatestdec:
            minmonth=(row[0])
            greatestdec=int(row[1])
        elif int(row[1]) < greatestdec:
            minmonth=(row[0])
            greatestdec=int(row[1])
        revchange.append(int(row[1]))
        
# Average Change 
for i in range(len(revchange)-1):
    monthlychange=(revchange[i+1]-revchange[i])
    monthchange.append(monthlychange)
    
averagechange=statistics.mean(monthchange)

# print/write 
print(f"Financial Analysis")
print(f"\n----------------------------")
print(f"\nTotal Months:" +str(months))
print(f"\nTotal:$"+ str(net_total))
print(f"\nAverage Change:$"+str(round(averagechange,2)))
print(f"\nGreatest Increase in revenue:"+str(maxmonth)+" ($" +str(greatestinc) + ")")
print(f"\nGreatest Decrease in revenue:"+str(minmonth)+" ($" +str(greatestdec) + ")")

f.write(f"Financial Analysis")
f.write(f"\n----------------------------")
f.write(f"\nTotal Months:" +str(months))
f.write(f"\nTotal:$"+ str(net_total))
f.write(f"\nAverage Change:$"+str(round(averagechange,2)))
f.write(f"\nGreatest Increase in revenue:"+str(maxmonth)+" ($" +str(greatestinc) + ")")
f.write(f"\nGreatest Decrease in revenue:"+str(minmonth)+" ($" +str(greatestdec) + ")")