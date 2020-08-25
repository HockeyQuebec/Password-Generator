import random

password_length = int (input("length"))
password_alphabet = [   "a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "j" , "k" , "l" , "m" , "n" , "o" , 
                        "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"]

password_alphabet_caps = [  "A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "J" , "K" , "L" , "M" , "N" , "O" , 
                            "P" , "Q" , "R" , "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z"]

password_symbols = [ "?", "/", ".", ",", "<", ">", ":", ";", "\"", "'", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "=", "-", "`", "~"]
password_numbers = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0"]

password_all_characters = password_alphabet_caps + password_numbers + password_alphabet + password_symbols

#password_symbols = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "j" , "k" , "l" , "m" , "n" , "o" , 
#"p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"]

 #= ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "j" , "k" , "l" , "m" , "n" , "o" , 
#"p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"]

 #= ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "j" , "k" , "l" , "m" , "n" , "o" , 
#"p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"]

generated_password = ""
for i in range(0, password_length):
    n = random.randint(0,len(password_all_characters))
    # print("index " + str(n) + " character " + password_all_characters[n]
    generated_password = generated_password + password_all_characters[n]

print(generated_password)


