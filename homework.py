import pandas as pd
import numpy as np

marathon = pd.read_csv('../files/boston_marathon2017_edited.csv', sep=',')
sox2017 = pd.read_csv('../files/redsox_2017_hitting.txt')

names = ['Alice',
         'Bob',
         'James',
         'Beth', 
         'John', 
         'Sally',
         'Richard', 
         'Lauren',
         'Brandon', 
         'Sabrina']

ages = np.random.randint(18,35,len(names))

my_people = {
    'names': names,
    'ages': ages
}

data = pd.DataFrame.from_dict(my_people)


my_row = data.loc[0]
print(f'1st row of data:\n{my_row}\n')

multiple_people = data.loc[[4, 5, 8]]
print(f'first three rows of data:\n{multiple_people}\n')
print(type(multiple_people))

multiple_people = data.loc[[4, 5, 8]][['names', 'ages']]
print(f'first three rows of data w/ specific columns:\n{multiple_people}\n')
print(type(multiple_people))

other_people = multiple_people.reset_index()
other_people

multiple_people.reset_index(drop=True, inplace=True)

sorted_hitters = sox2017.sort_values('HR')
sox2017.keys().tolist()