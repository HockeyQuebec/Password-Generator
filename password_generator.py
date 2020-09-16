import random
from time import sleep
import csv
import threading

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
password_all_characters = [""]

print("Please respond with y or n")

# Desides if you want the alphabet
althabet = input("Would you like the alphabet?:")
if althabet.__contains__("y") == True:
   password_all_characters = password_all_characters + password_alphabet

# Desides if you want the alphabet in capitals
q_althabet_caps = input("Would you like caps alphabet?:")
if q_althabet_caps.__contains__("y") == True:
    password_all_characters = password_all_characters + password_alphabet_caps

# Desides if you want symbols
symbols = input("Would you like symbols?:")
if symbols.__contains__("y") == True:
    password_all_characters = password_all_characters + password_symbols

# Desides if you want numbers
numbers = input("Would you like numbers?:")
if numbers.__contains__("y") == True:
    password_all_characters = password_all_characters + password_numbers

# Desides if you want the greek alphabet
q_greek_althabet = input("Would you like the greek alphabet?:")
if q_greek_althabet.__contains__("y") == True:
    password_all_characters = password_all_characters + password_greek_symbols

# Desides if you want the greek alphabet in capitals
q_greek_althabet_caps = input("Would you like caps greek alphabet?:")
if q_greek_althabet_caps.__contains__("y") == True:
    password_all_characters = password_all_characters + password_greek_symbols_caps

# Gets user input how long they want the password
password_length = int(input("length"))

# create work for each thread rounding down
password_length_partions = password_length//12

# makes the partions back up to the highest number that is lowwer than the inputed value.
password_length_help = password_length_partions*12

# figures out how much extra charecters that are needed
corrrect = password_length - password_length_help

# Defines that the generated password is a string
generated_password = ""

# created two tasks because 12 threads on a single funtion is too much. It doesn't have all 12 working at the same time. Both tasks are the same.  
def task2():
    global generated_password
    for i in range(0, password_length_partions):
        h = random.randint(0,len(password_all_characters)-1)
        generated_password = generated_password + password_all_characters[h]

def task3():
    global generated_password
    for i in range(0, password_length_partions):
        f = random.randint(0,len(password_all_characters)-1)
        generated_password = generated_password + password_all_characters[f]



# Defines all of the threads

t1 = threading.Thread(target=task2, name="task1")

t2 = threading.Thread(target=task2, name="task2")

t3 = threading.Thread(target=task2, name="task3")

t4 = threading.Thread(target=task2, name="task4")

t5 = threading.Thread(target=task2, name="task5")

t6 = threading.Thread(target=task2, name="task6")

t7 = threading.Thread(target=task3, name="task7")

t8 = threading.Thread(target=task3, name="task8")

t9 = threading.Thread(target=task3, name="task9")

t10 = threading.Thread(target=task3, name="task10")

t11 = threading.Thread(target=task3, name="task11")

t12 = threading.Thread(target=task3, name="task12")

# Start all of the threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()

# Waits for the threads to do their work
t1.join() 
t2.join()
t3.join() 
t4.join()
t5.join() 
t6.join()
t7.join() 
t8.join()
t9.join() 
t10.join()
t11.join() 
t12.join()

# Generates all of the extra charaters
print(corrrect)
for i in range(0, corrrect):
    t = random.randint(0,len(password_all_characters)-1)
    generated_password = generated_password + password_all_characters[t]

# Prints the generated password
print(generated_password)

# Desides if you want to save the password you generated
write = input("Would you like to save this?")
if write.__contains__("y") == True:
    # This opens the file to be appended
    password = open("passwords.txt","a")

    # This gets user input to fill out the name for the password
    label = input("What is the label for your password?:")

    # This adds a couple of line breaks to make reading it easier
    generated_password = (label + ":" + "\r\n" + "  " + generated_password + "\r\n")

    # This writes the password, label, and line breaks to password. Password = open("passwords.txt", "a")
    password.write(generated_password)

    # This closes the file
    password.close()

# This takes user input to deside if you want to "find" a password. By that I mean it prints out the text file
find = input("Would you like you find a password?")

if find.__contains__("y") == True:
    fin = open("passwords.txt")
    for element in fin:
        print(element)

# This takes user input to deside if you want to exit
if find.__contains__("n") == True:
    exit
    SystemExit