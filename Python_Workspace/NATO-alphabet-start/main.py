student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

import pandas as pd
nato_cd_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")
nato_ditc = {row.letter:row.code for (index,row) in nato_cd_data_frame.iterrows()}
print(nato_ditc)



def create_Coding():
    name = input("Enter a word: ").upper() #input which makes everthing bigger 
    try:
        codename = [nato_ditc[letter] for letter in name] #it takes from the dic the key Letter for letter in the Word 
    except KeyError:
        print("Sorry but just letter are allowed")
        create_Coding()
    else:
        codename = [nato_ditc[letter] for letter in name] #it takes from the dic the key Letter for letter in the Word 
        print(codename)


create_Coding()