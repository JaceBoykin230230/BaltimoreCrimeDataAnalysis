import pandas as pd 
import rich
import matplotlib.pyplot as plt

df = pd.read_csv('BPD_Part_1_Victim_Based_Crime_Data.csv')

'''
Column names: 
Index(['CrimeDate', 'CrimeTime', 'CrimeCode', 'Location', 'Description','Inside/Outside', 'Weapon', 'Post', 'District', 'Neighborhood',
'Longitude', 'Latitude', 'Location 1', 'Premise', 'Total Incidents'], dtype='object') 
'''
rich.print(df.columns)
rich.print(df.dtypes)

# Analysis:

# 1. For indoor crime, what is the most common weapon used?
rich.print("The most common weapon used for indoor crime is:")
indoor_crime = df[df['Inside/Outside'] == 'I']
rich.print(indoor_crime['Weapon'].value_counts().idxmax())
rich.print()

# 2. What is the most common crime in each district?
rich.print("The most common crime in each district is:")
rich.print(df.groupby('District')['Description'].value_counts().groupby('District').idxmax())
rich.print()

# 3. What neighborhood has the most crime?
rich.print("The neighborhood with the most crime is:")
rich.print(df['Neighborhood'].value_counts().idxmax())
rich.print()

# 4. What is the most common crime code based on location?
rich.print("The most common crime code based on location is:")
rich.print(df.groupby('Location')['CrimeCode'].value_counts().groupby('Location').idxmax())
rich.print()

# 5. For each neighboorhood, what is the most common time of day for crime to occur?
rich.print("For each neighborhood, the most common time of day for crime to occur is:")
rich.print(df.groupby('Neighborhood')['CrimeTime'].value_counts().groupby('Neighborhood').idxmax())
rich.print()

# 6. On what premise are you most likely to be a victim of each type of crime?
rich.print("On what premise are you most likely to be a victim of each type of crime?")
rich.print(df.groupby('Description')['Premise'].value_counts().groupby('Description').idxmax())
rich.print()

# 7. For each year, what day has the most crime?
rich.print("For each year, what day of the year has the most crime?")
df['CrimeDate'] = pd.to_datetime(df['CrimeDate'])
df['Year'] = df['CrimeDate'].dt.year
rich.print(df.groupby('Year')['CrimeDate'].value_counts().groupby('Year').idxmax())
rich.print()


#Graphs

# 1. for each district create a bar graph showing the most common hour for a crime to occur
df['Hour'] = df['CrimeTime'].str.split(':').str[0]
df['Hour'] = df['Hour'].astype(int)
district_hour_counts = df.groupby(['District', 'Hour']).size()
most_common_hour_per_district = district_hour_counts.groupby('District').idxmax().str[1]
most_common_hour_per_district = most_common_hour_per_district.sort_values()
plt.figure(figsize=(18, 8))
plt.bar(most_common_hour_per_district.index, most_common_hour_per_district.values)
plt.ylabel('HOUR')
plt.xlabel('DISTRICT')
plt.title('Most Common Hour of Crime Occurrence in Each District')
plt.tight_layout()
plt.savefig('most_common_hour_per_district.png')
plt.tight_layout()
plt.show()
plt.close()

# 2. Pie chart of precentage of crime that occurs in each premise.
premise_counts = df['Premise'].value_counts()
plt.figure(figsize=(18, 8))
# get the percentage, and if the percentage is less thatn 1% then don't show it
if premise_counts.min() / premise_counts.sum() < 0.01:
    premise_counts = premise_counts[premise_counts / premise_counts.sum() > 0.01]
plt.pie(premise_counts, labels=premise_counts.index, autopct='%1.1f%%')
plt.title('Percentage of Crime Occurring in Each Premise')
plt.tight_layout()
plt.savefig('precentage_of_crime_per_premise.png')
plt.show()
plt.close()



