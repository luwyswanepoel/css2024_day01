# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:29:17 2024

@author: Luwy Swanepoel
"""
# PART1 Reading Files In With Pandas
import pandas

file1 = pandas.read_csv("country_data.csv")
print(file1)
print(file1.info())
print(file1.describe())

file2 = pandas.read_csv("diab_data.csv")
print(file2)
print(file2.info())
print(file2.describe())

column_names = ["a","b","c","d","e"]
file3 = pandas.read_csv("housing_data.csv", names = column_names)
print(file3)
print(file3.info())
print(file3.describe())

file4 = pandas.read_csv("insurance_data.csv",skiprows=6)
print(file4)
print(file4.info())
print(file4.describe())

file5 = pandas.read_csv("iris.csv")
print(file5)
print(file5.info())
print(file5.describe())

# PART2 Storing Data In Python
# PART2 PART1 Storing Data
B1 = 30
B2 = 40
B3 = 30
B4 = 49
B5 = 22
B6 = 35
B7 = 22
B8 = 46
B9 = 29
B10 = 25
B11 = 39
print(B1)
print(B2)
print(B3)
print(B4)
print(B5)
print(B6)
print(B7)
print(B8)
print(B9)
print(B10)
print(B11)

# Age List
age = [30,40,30,49,22,35,22,46,29,25,39]
print(age)

# List indexes start at 0 which has the value of 30
print(age[0])
print(age[1])
print(age[2])
print(age[3])
print(age[4])
print(age[5])
print(age[6])
print(age[7])
print(age[8])
print(age[9])
print(age[10])

# Basic Stats
age = [30,40,30,49,22,35,22,46,29,25,39]
print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)


# PART2 PART2 STORING TEXT
C1 = "M"
C2 = "F"
C3 = "M"
C4 = "M"
C5 = "F"
C6 = "F"
C7 = "F"
C8 = "M"
C9 = "F"
C10 = "M"
C11 = "M"
print(C1)
print(C2)
print(C3)
print(C4)
print(C5)
print(C6)
print(C7)
print(C8)
print(C9)
print(C10)
print(C11)

# Gender List
gender = ["M","F","M","M","F","F","F","M","F","M","M"]
print(gender)

# List indexes start at 0 which has the text M
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[3])
print(gender[4])
print(gender[5])
print(gender[6])
print(gender[7])
print(gender[8])
print(gender[9])
print(gender[-1])


# PART2 PART3 STORING TEXT
D1 = "Sudan"
D2 = "Egypt"
D3 = "Kenya"
D4 = "Kenya"
D5 = "Lesotho"
D6 = "Mozambique"
D7 = "Kenya"
D8 = "South Africa"
D9 = "South Africa"
D10 = "Botswana"
D11 = "South Africa"
print(D1)
print(D2)
print(D3)
print(D4)
print(D5)
print(D6)
print(D7)
print(D8)
print(D9)
print(D10)
print(D11)

# Country List
country = ["Sudan","Egypt","Kenya","Kenya","Lesotho","Mozambique","Kenya","South Africa","South Africa","Botswana","South Africa"]
print(country)

# List indexes start at 0 which has the text M
print(country[0])
print(country[1])
print(country[2])
print(country[3])
print(country[4])
print(country[5])
print(country[6])
print(country[7])
print(country[8])
print(country[9])
print(country[-1])


# PART3 LISTS
# Data Storage With Lists
my_list = [42,-2021,6.283,"tau","node"]
print(my_list)
print(my_list[:])
my_list.append("pi")
my_list.insert(1,"pi2")
my_list.remove("pi")
print(my_list)
print(len(my_list))
print(my_list[0:3])


# PART4 DICTIONARIES
person = {'name':'John Doe', 'age': '30', 'address':'123 Main St.'}
print(person['name'])

# PART5 DATA FRAMES
# Creating Dataframe
import pandas as pd
data = {
    'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}
df = pd.DataFrame(data)
print(df)

# Accessing specific columns
print(df['age'])
print(df['gender'])

# Basic statistics
print(df['age'].min())
print(df.describe())

# Filtering data
print(df[df['age']>30])

# Slicing rows and columns
print(df[0:5])

# Adding a new column
df['new_column'] = [1,2,3,4,5,6,7,8,9,10,11]
print(df)

# Removing a column
df.drop(columns=['new_column'],inplace=True)
print(df)

