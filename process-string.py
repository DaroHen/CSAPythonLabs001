# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "



User_input = input("Please enter any words: ")
User_input1 = User_input
User_input2 = User_input

# Interleave the two lists
User_input1_2 = [None]*(len(User_input1)+len(User_input2))
User_input1_2[::2] = User_input1
User_input1_2[1::2] = User_input2

#convert list to str "afagfafaf"
User_str = ''.join(User_input1_2)
print(User_str)




# Application 2
# Given a string indicating a range of letters, return a string which includes all the letters in that range,
# including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.


alphabet = "abcdefghijklmnopqrstuvwxyz"

user_range = input("Enter a range of letters (e.g., a-z): ")
start, end = user_range.split('-')

upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Com_al_upper = alphabet + upper_alpha

first_index = Com_al_upper.index(start)
second_index = Com_al_upper.index(end)

print(Com_al_upper[first_index :second_index +1 ])



#name : Hen Chandaro










