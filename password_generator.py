import random
from time import sleep
import csv
import threading
ex = 1
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

#
# checks if workers are running and when they have finished prints the generated password
#
def control_task():
    while True:
        worker_threads_running = 0
        for thread in threading.enumerate():
            print("Thread " + thread.name + " isAlive " + str(thread.is_alive()) + "\n")
            if thread.name.startswith("worker"):
                worker_threads_running = worker_threads_running + 1

        if worker_threads_running == 0:
            print("All threads have finished")
            finish()
            exit()

        sleep(3.0)

#
# worker that will generate part of the password
#
def password_worker_task():
    global generated_password
    for i in range(0, password_length_partions):
        h = random.randint(0,len(password_all_characters)-1)
        generated_password = generated_password + password_all_characters[h]
        if i % 10000 == 0:
            print(threading.current_thread.__name__ + " iteration [" + str(i) + "] of [" + str(password_length_partions) + "]\n")

#
# print the password and ask if they want to save to file
#
def finish(generated_password):
    # Generates all of the extra charaters
    for i in range(0, corrrect):
        t = random.randint(0,len(password_all_characters)-1)
        generated_password = generated_password + password_all_characters[t]

    # Prints the generated password
    print(generated_password)

    # Desides if you want to save the password you generated
    write = input("Would you like to save this?:")
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
    find = input("Would you like to find a password?:")

    if find.__contains__("y") == True:
        fin = open("passwords.txt")
        for element in fin:
            print(element)
        ex = 0
    v = input("would you like to exit?:")

    # This takes user input to deside if you want to exit
    if v.__contains__("y") == True:
        ex = 0   

print("Please respond with y or n")
while ex==1:

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
    threads = input("How many threads do you want?:")
    threads = int(threads)
    # create work for each thread rounding down
    password_length_partions = password_length//12

    # makes the partions back up to the highest number that is lowwer than the inputed value.
    password_length_help = password_length_partions*12

    # figures out how much extra charecters that are needed
    corrrect = password_length - password_length_help

    # Defines that the generated password is a string
    generated_password = ""

   
    # Defines all of the threads
    for i in range(0, threads):
        name = "worker " + str(i)
        thread = threading.Thread(target=password_worker_task, name=name)
        thread.daemon = True
        thread.start()

    # start the main control thread that will output the password once all the threads have finished
    thread = threading.Thread(target=control_task, name="main control")
    thread.daemon = True
    thread.start()

