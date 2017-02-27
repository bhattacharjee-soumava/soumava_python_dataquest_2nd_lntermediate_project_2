
# coding: utf-8

# In[15]:

import csv

f = open('guns.csv','r')
data_read = csv.reader(f)
data = list(data_read)

print(data[0:5])


# In[16]:

headers = data[0]
data = data[1:len(data)]

print(data[0:5])


# In[3]:

years = [row[1] for row in data]
year_counts = {}
for year in years:
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1
print(year_counts)        


# In[9]:

import datetime

dates = [datetime.datetime(year=int(row[1]),month=int(row[2]),day=1) for row in data]
print(dates[0:5])
print('\n\n')
date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1
print(date_counts)


# In[4]:

sexs = [row[5] for row in data]
sex_counts = {}
for sex in sexs:
    if sex in sex_counts:
        sex_counts[sex] += 1
    else:
        sex_counts[sex] = 1
print(sex_counts)



# In[18]:

races = [row[7] for row in data]
race_counts = {}
for race in races:
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1
print(race_counts)


# # Need further Examination:
# 
# ## Topis:
# 
# - Class
# - Datetime functions
# - Regular Expressions
# 

# In[19]:

import csv

f2 = open('census.csv','r')
csvread = csv.reader(f2)
census = list(csvread)
print(census)


# In[20]:


mapping = {}
for race in race_counts:
    if race == 'Asian/Pacific Islander':
        mapping[race] = int(census[1][14]) + int(census[1][15])
    elif race == 'Black':
        mapping[race] = int(census[1][12])    
    elif race == 'Native American/Native Alaskan':
        mapping[race] = int(census[1][13])
    elif race == 'Hispanic':
        mapping[race] = int(census[1][11])
    elif race == 'White':
        mapping[race] = int(census[1][10])    
        
race_per_hundredk = {}

for race in race_counts:
    race_per_hundredk[race] = race_counts[race] / mapping[race] * 100000

print(race_per_hundredk)    


# In[21]:

intents = [row[3] for row in data]
race_counts = {}
for i, race in enumerate(races):
    if intents[i] == 'Homicide':
        if race in race_counts:
            race_counts[race] += 1
        else:
            race_counts[race] = 1
print(race_counts)    

homicide_race_per_hundredk = {}

for race in race_counts:
    homicide_race_per_hundredk[race] = race_counts[race] / mapping[race] * 100000

print(homicide_race_per_hundredk)  


# In[ ]:



