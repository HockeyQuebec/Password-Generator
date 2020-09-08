import random
from time import sleep
import csv
#print("These are how many charecters the generater can chose from." + " " + str(26 + 26 +10 + 24 + 24 + 25))

password_alphabet = [   "a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "j" , "k" , "l" , "m" , "n" , "o" , 
                        "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"]

password_alphabet_caps = [  "A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "J" , "K" , "L" , "M" , "N" , "O" , 
                            "P" , "Q" , "R" , "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z"]

password_symbols = [ "?", "/", ".", ",", "<", ">", ":", ";", "\"", "'", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "=", "-", "`", "~"]

password_numbers = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0"]

password_greek_symbols = ["α", "β", "γ", "δ", "ε", "ζ", "η", "θ", "ι", "κ", "λ", "μ", "ν", "ξ", "ο", "π", "ρ",
                           "σ", "ς", "τ", "υ", "φ", "χ", "ψ", "ω"]

password_greek_symbols_caps = ["Α", "Β", "Γ", "Δ", "Ε", "Ζ", "Η", "Θ", "Ι", "Κ", "Λ", "Μ", "Ν", "Ξ", "Ο", "Π", 
                                "Ρ", "Σ", "Τ", "Υ", "Φ", "Χ", "Ψ", "Ω"]

 #= ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "j" , "k" , "l" , "m" , "n" , "o" , 
#"p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"]

password_all_characters = [""]

print("Please respond with y or n")

althabet = input("would you like the alphabet?")
if althabet.__contains__("y") == True:
   password_all_characters = password_all_characters + password_alphabet

q_althabet_caps = input("would you like caps alphabet?")
if q_althabet_caps.__contains__("y") == True:
    password_all_characters = password_all_characters + password_alphabet_caps

symbols = input("would you like symbols?")
if symbols.__contains__("y") == True:
    password_all_characters = password_all_characters + password_symbols

numbers = input("would you like numbers?")
if numbers.__contains__("y") == True:
    password_all_characters = password_all_characters + password_numbers

q_greek_althabet = input("would you like the greek alphabet?")
if q_greek_althabet.__contains__("y") == True:
    password_all_characters = password_all_characters + password_greek_symbols

q_greek_althabet_caps = input("would you like caps greek alphabet?")
if q_greek_althabet_caps.__contains__("y") == True:
    password_all_characters = password_all_characters + password_greek_symbols_caps

password_length = int (input("length"))




generated_password = ""

for i in range(0, password_length):
    n = random.randint(0,len(password_all_characters)-1)
    # print("index " + str(n) + " character " + password_all_characters[n]
    generated_password = generated_password + password_all_characters[n]

print(generated_password)

write_to = input("would you like to save this password?")

password_index_set = {"password"}

if write_to.__contains__("y") == True:
    label = input("What is the label for your passwords")
    password = open("passwords.txt","a")
    password_index = (label + ":" + "\r\n" + "  " + generated_password + "\r\n")
    password.write(password_index)
    password_index_set.add(password_index)

    find = input("Would you like yo find a password?")
    if find.__contains__("y") == True:
        fin = open("passwords.txt")
        for element in fin:
            print(element)

    
if write_to.__contains__("n") == True:
    exit
    SystemExit
    