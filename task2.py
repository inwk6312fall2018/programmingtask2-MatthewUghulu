import csv
def crime_list():
	with open("Crime.csv","r") as myfile: # open and reas csv file imported from github
		my_dict= dict()
		my_list = []
	for line in myfile:
		line=line.strip()
	for line in line.split(','):
		my_list.append(line[-1])  #adding crime name data to my_list
	for i in my_list: 
		if(i not in my_dict): 
			my_dict[i]=1      
		else:
			my_dict[i]=my_dict[i]+1           # incrementing by adding to my_dict if none found
	print ("{:<12} {:<29}".format('keys','values')) 
	for keys, values in my_dict.items():   # making a table format
		crime_type=keys
		crime_count=values
		print("{:<12} {:<19}".format(crime_type, crime_count))
       
crime_list() # called function from the defination

