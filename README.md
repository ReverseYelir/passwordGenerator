# passwordGenerator
Random password generator using python
The program accesses a list of approx. 25,000 english words via an http request.
A random word is generated with a random length and a random number between 0-99 is added after the word.
This process is then repeated again, creating the final password. 
The new password and its purpose are then written into a text file and saved in the same directory as password-generator.py
