# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data_nato = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data_frame = pandas.DataFrame(data_nato)
nato_dict = {row.letter: row.code for (_, row) in nato_data_frame.iterrows()}

while_error = True
while while_error:
    user_input = input("Enter a word: ").upper()
    try:
        list_letters = [word for word in user_input.strip()]
        nato_words = [nato_dict[word] for word in list_letters]
        print(nato_words)
        while_error = False
    except KeyError:
        print("Enter only letters from alphabet please.")
