import random
from time import sleep
import csv
#print("These are how many charecters the generater can chose from." + " " + str(26 + 26 +10 + 24 + 24 + 25))

password_length = int (input("length"))
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



password_all_characters = password_alphabet_caps + password_numbers + password_alphabet + password_symbols + password_greek_symbols + password_greek_symbols_caps

generated_password = ""

for i in range(0, password_length):
    n = random.randint(0,len(password_all_characters)-1)
    # print("index " + str(n) + " character " + password_all_characters[n]
    generated_password = generated_password + password_all_characters[n]

print(generated_password)


write_to = input("would you like to save this password?")


if write_to.__contains__("y") == True:
    label = input("What is the label for your passwords")
    password = open("passwords.txt","a")
    password.write(generated_password + "   " + label)
    
if write_to.__contains__("n") == True:
    exit
    SystemExit
    