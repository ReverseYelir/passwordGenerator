import urllib.request
import random
import math

def response_processor(password_input_response):
    '''
        Function takes in a user inputted string and compares it the the response 'y' for yes.
        If password_input_response equals 'y', program will continue by adding any newly
        generated password to the pre-existing file. If it != 'y', a new file for generated
        password is created under the name: "keybank.txt"
    '''

    # if statement checks to see if user has password txt doc 
    if password_input_response == 'y' or password_input_response == 'Y':
        name_query = input("Is that file keybank.txt?\ny/n: ")
        print()
        has_doc = True
        # decides if pre-existing text doc is generated for this program
        if name_query == 'y' or name_query == 'Y':
            file_name = 'keybank.txt'
        else:
            file_name = input("Enter the file name containing password(include .txt extension):\n")
            print()
    else:
        has_doc = False
        file_name = 'keybank.txt'
    
    return file_name, has_doc
    
def document_maker(boolean):
    '''
        Function takes in a boolean as a parameter and if True, function with append any
        new passwords to the existing document. If False, program will created a new text 
        document named: "keybank.txt" and write newly generated passwords to that file
    '''
    if boolean == False:
        file = open('keybank.txt', 'w')
        file.close()

def password_generator(file_name, word_list, password_purpose):
    password = ''
    final_password_list = []
    # loop iterates twice
    for iteration in range(2):
        random_word = word_list[random.randint(0,len(word_list))]
        random_word_length = random.randint(1,len(random_word))
        cap_letter_step = random.randint(1,random_word_length)
        random_word = random_word[:random_word_length]
        password += random_word
        password += str(random.randint(0,99))

    for i in range(len(password)):
        if i%cap_letter_step == 0 and password[i].isalpha():
            final_password_list.append(password[i].upper())
        else:
            final_password_list.append(password[i])
        
    final_password = ''.join(final_password_list)
    file = open(file_name, 'a')
    file.write(password_purpose + ' password: ' + final_password + '\n')
    file.close()
    print('Pasword({}) generated for {} and stored in {}'.format(final_password, password_purpose, file_name))
    print()

def main():
    
    # block fetches huge english word list via http request and converts the content into a list
    word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = urllib.request.urlopen(word_url)
    word_list = response.read().decode().split()
    
    # block responsible for gather data about any files and opens correct file
    password_response = input("Do you have a pre-existing file containing passwords?\ny/n: ")
    print()
    file_name, has_doc = response_processor(password_response)
    document_maker(has_doc)
    password_purpose = input("What is this password for?\n")
    print()
    password_generator(file_name, word_list, password_purpose)
    again = 'y'
    
    # loop controls if the generation proccess is continued
    while again == 'y' or again == 'Y':
        again = input('Generate another password?\ny/n? ')
        if again =='n' or again == 'N':
            break
        print()
        password_purpose = input("What is this password for?\n")
        print()
        password_generator(file_name, word_list, password_purpose)
    
main()
