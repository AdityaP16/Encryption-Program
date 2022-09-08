# encryption.py
# Aditya Prasad, ENDG 233 F21
### Define your functions here
import string

#Creates the output function for the cipher, and replaces each index of the user cipher with the corresponding dictionary keys.
#Iterates through the cipher in the function when called upon
def output_function(cipher_text,cipher_dict): 
    output_cipher_text = ''
    i = 0
    while i < len(cipher_text):
        if cipher_text[i] in cipher_dict.keys():
            output_cipher_text += cipher_dict[cipher_text[i]]
        i += 1

    return output_cipher_text
'''
returns the output_cipher_text
the parameters include the cipher text and cipher dict
this function takes the function text at each index (value) and inserts it into the cipher dict which becomes the output cipher text
'''
#creates a new dictionary with the user inputed values for the keys and the values when called upon 
def dict_function_mapping(dict_keys,dict_values):
    new_dict = dict(zip(dict_keys,dict_values))
    return new_dict

'''
returns new_dict to the output 
the parameters include the dict_keys and dict_values meant to represent the keys and values inputted by the user into the program
creates a dictionary based off the keys and values inputted by the user into the program
'''

#third function just for printing out the end
def print_end():
    print('\nThank you for using the encryption program.')

'''
returns none 
no parameters
just prints the end string to the program
'''


#Prints beginning statement and inits the alphabet list [a->z], asks user for choices
print('Encryption Program')
alphabet = list(string.ascii_lowercase)
choice = int(input('(1) Encode \n(2) Decode your message \n(0) Exit program\n'))

#While loop used so that if user selects a number >=3 or <=-1, it wont execute code and if they choose the options, it'll execute
while choice != 0: 
    if choice >= 3 or choice <= -1:
        x = 1
        print('Invalid Selection Entry.')
        break
    x = 0
    #checks the cipher to see if it equals to exactly 26 letters, if not repeat loop until user inputs value
    while x == 0:
        user_made_cipher = list(input('Please enter the Cipher text: '))
        if len(set(user_made_cipher)) != 26:
            print('Your cipher must contain 26 unique elements of a-z or 0-9')
        else:
            print('Your Cipher is valid.')
            x = 1 
    #if first choice is used enter the cipher and execute the functions defined above with the parameters taken from the user variables
    if choice == 1:
        x = 0
        while x == 0:
            if len(set(user_made_cipher)) != 26:
                print('Your cipher must contain 26 unique elements of a-z or 0-9')
                user_made_cipher = list(input('Please enter the Cipher text: '))
                x = 1
            else:
                x = 1        

        user_text = str(input('Please enter the text to be processed: '))
        encoding_dict = dict_function_mapping(alphabet,user_made_cipher)
        print(f'Your Output is: {output_function(user_text,encoding_dict)}')
        choice = int(input('(1) Encode \n(2) Decode your message \n(0) Exit program\n'))

    #Decode: Program checks length of the cipher, making sure its equal to 26 and if not then executes the decoding portion of the program using user input variables
    elif choice == 2:
        x = 0
        while x == 0:
            if len(set(user_made_cipher)) != 26:
                print('Your cipher must contain 26 unique elements of a-z or 0-9')
                user_made_cipher = list(input('Please enter the Cipher text: '))
                x = 1
            else:
                x = 1 

        user_text = str(input('Please enter the text to be processed: '))
        decoding = dict_function_mapping(user_made_cipher,alphabet)
        print(f'Your Output is: {output_function(user_text,decoding)}')
        choice = int(input('(1) Encode \n(2) Decode your message \n(0) Exit program\n'))
#end
print_end()