import random
import time
import csv
import threading

# print("These are how many charecters the generater can chose from." + " " + str(26 + 26 +10 + 24 + 24 + 25))

password_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "j", "k", "l", "m", "n", "o",
                     "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

password_alphabet_caps = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "O",
                          "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

password_symbols = ["?", "/", ".", ",", "<", ">", ":", ";", "\"", "'", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
                    "_", "=", "-", "`", "~"]

password_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

password_greek_symbols = ["α", "β", "γ", "δ", "ε", "ζ", "η", "θ", "ι", "κ", "λ", "μ", "ν", "ξ", "ο", "π", "ρ",
                          "σ", "ς", "τ", "υ", "φ", "χ", "ψ", "ω"]

password_greek_symbols_caps = ["Α", "Β", "Γ", "Δ", "Ε", "Ζ", "Η", "Θ", "Ι", "Κ", "Λ", "Μ", "Ν", "Ξ", "Ο", "Π",
                               "Ρ", "Σ", "Τ", "Υ", "Φ", "Χ", "Ψ", "Ω"]
password_all_characters = [""]

print("Please respond with y or n")

althabet = input("would you like the alphabet?")

if althabet.__contains__("y"):
    password_all_characters = password_all_characters + password_alphabet

q_althabet_caps = input("would you like caps alphabet?")
if q_althabet_caps.__contains__("y"):
    password_all_characters = password_all_characters + password_alphabet_caps

symbols = input("would you like symbols?")
if symbols.__contains__("y"):
    password_all_characters = password_all_characters + password_symbols

numbers = input("would you like numbers?")
if numbers.__contains__("y"):
    password_all_characters = password_all_characters + password_numbers

q_greek_althabet = input("would you like the greek alphabet?")
if q_greek_althabet.__contains__("y"):
    password_all_characters = password_all_characters + password_greek_symbols

q_greek_althabet_caps = input("would you like caps greek alphabet?")
if q_greek_althabet_caps.__contains__("y"):
    password_all_characters = password_all_characters + password_greek_symbols_caps


threads = 12


print(threads)
password_length = int(input("length"))
print(password_length)
password_length = int(password_length)
print(password_length)
password_length_1 = password_length // threads
print(password_length_1)
password_length_help = password_length_1 * threads
print(password_length_help)
correct = password_length - password_length_help
print(correct)
generated_password = ""


def task2():
    global generated_password
    for i in range(0, password_length_1):
        h = random.randint(0, len(password_all_characters) - 1)
        generated_password = generated_password + password_all_characters[h]


def thread():
    for i in range(0, threads):
        name = 't' + str(i)
        hello = i
        name = threading.Thread(target=task2, name=name)
        name.start()
        print(generated_password)
        print(time.time_ns() / 1000000000)
        name.join()
        print(time.time_ns() / 1000000000)

    if threads == 1:
        t1 = threading.Thread(target=task2, name='t1')
        print(time.time_ns() / 1000000000)
        t1.start()

        t1.join()
        print(time.time_ns() / 1000000000)

    if threads == 2:
        t1 = threading.Thread(target=task2, name='t1')
        t2 = threading.Thread(target=task2, name='t2')
        print(time.time_ns() / 1000000000)
        t1.start()
        t2.start()

        t1.join()
        t2.join()
        print(time.time_ns() / 1000000000)

    if threads == 3:
        t1 = threading.Thread(target=task2, name='t1')
        t2 = threading.Thread(target=task2, name='t2')
        t3 = threading.Thread(target=task2, name='t3')
        print(time.time_ns() / 1000000000)
        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()
        print(time.time_ns() / 1000000000)

    if threads == 4:
        t1 = threading.Thread(target=task2, name='t1')
        t2 = threading.Thread(target=task2, name='t2')
        t3 = threading.Thread(target=task2, name='t3')
        t4 = threading.Thread(target=task2, name='t4')

        print(time.time_ns() / 1000000000)
        t1.start()
        t2.start()
        t3.start()
        t4.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()

        print(time.time_ns() / 1000000000)

    if threads == 5:
        t1 = threading.Thread(target=task2, name='t1')
        t2 = threading.Thread(target=task2, name='t2')
        t3 = threading.Thread(target=task2, name='t3')
        t4 = threading.Thread(target=task2, name='t4')
        t5 = threading.Thread(target=task2, name='t5')

        print(time.time_ns() / 1000000000)
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        print(time.time_ns() / 1000000000)

    if threads == 6:
        t1 = threading.Thread(target=task2, name='t1')
        t2 = threading.Thread(target=task2, name='t2')
        t3 = threading.Thread(target=task2, name='t3')
        t4 = threading.Thread(target=task2, name='t4')
        t5 = threading.Thread(target=task2, name='t5')
        t6 = threading.Thread(target=task2, name='t6')

        print(time.time_ns() / 1000000000)
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        print(time.time_ns() / 1000000000)

    if threads == 7:
        t1 = threading.Thread(target=task2, name='t1')
        t2 = threading.Thread(target=task2, name='t2')
        t3 = threading.Thread(target=task2, name='t3')
        t4 = threading.Thread(target=task2, name='t4')
        t5 = threading.Thread(target=task2, name='t5')
        t6 = threading.Thread(target=task2, name='t6')
        t7 = threading.Thread(target=task2, name='t7')

        print(time.time_ns() / 1000000000)
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        print(time.time_ns() / 1000000000)

    if threads == 8:
        t1 = threading.Thread(target=task2, name='t1')
        t2 = threading.Thread(target=task2, name='t2')
        t3 = threading.Thread(target=task2, name='t3')
        t4 = threading.Thread(target=task2, name='t4')
        t5 = threading.Thread(target=task2, name='t5')
        t6 = threading.Thread(target=task2, name='t6')
        t7 = threading.Thread(target=task2, name='t7')
        t8 = threading.Thread(target=task2, name='t8')

        print(time.time_ns() / 1000000000)
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()

        print(time.time_ns() / 1000000000)

    if threads == 8:
        t1 = threading.Thread(target=task2, name='t1')
        t2 = threading.Thread(target=task2, name='t2')
        t3 = threading.Thread(target=task2, name='t3')
        t4 = threading.Thread(target=task2, name='t4')
        t5 = threading.Thread(target=task2, name='t5')
        t6 = threading.Thread(target=task2, name='t6')
        t7 = threading.Thread(target=task2, name='t7')
        t8 = threading.Thread(target=task2, name='t8')

        print(time.time_ns() / 1000000000)
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()

        print(time.time_ns() / 1000000000)

    if threads == 9:
        t1 = threading.Thread(target=task2, name='t1')
        t2 = threading.Thread(target=task2, name='t2')
        t3 = threading.Thread(target=task2, name='t3')
        t4 = threading.Thread(target=task2, name='t4')
        t5 = threading.Thread(target=task2, name='t5')
        t6 = threading.Thread(target=task2, name='t6')
        t7 = threading.Thread(target=task2, name='t7')
        t8 = threading.Thread(target=task2, name='t8')
        t9 = threading.Thread(target=task2, name='t9')

        print(time.time_ns() / 1000000000)
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        t9.join()

        print(time.time_ns() / 1000000000)

    if threads == 10:
        t1 = threading.Thread(target=task2, name='t1')
        t2 = threading.Thread(target=task2, name='t2')
        t3 = threading.Thread(target=task2, name='t3')
        t4 = threading.Thread(target=task2, name='t4')
        t5 = threading.Thread(target=task2, name='t5')
        t6 = threading.Thread(target=task2, name='t6')
        t7 = threading.Thread(target=task2, name='t7')
        t8 = threading.Thread(target=task2, name='t8')
        t9 = threading.Thread(target=task2, name='t9')
        t10 = threading.Thread(target=task2, name='t10')

        print(time.time_ns() / 1000000000)
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

        print(time.time_ns() / 1000000000)

    if threads == 11:
        t1 = threading.Thread(target=task2, name='t1')
        t2 = threading.Thread(target=task2, name='t2')
        t3 = threading.Thread(target=task2, name='t3')
        t4 = threading.Thread(target=task2, name='t4')
        t5 = threading.Thread(target=task2, name='t5')
        t6 = threading.Thread(target=task2, name='t6')
        t7 = threading.Thread(target=task2, name='t7')
        t8 = threading.Thread(target=task2, name='t8')
        t9 = threading.Thread(target=task2, name='t9')
        t10 = threading.Thread(target=task2, name='t10')
        t11 = threading.Thread(target=task2, name='t11')

        print(time.time_ns() / 1000000000)
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

        print(time.time_ns() / 1000000000)

    if threads == 12:
        t1 = threading.Thread(target=task2, name='t1')
        t2 = threading.Thread(target=task2, name='t2')
        t3 = threading.Thread(target=task2, name='t3')
        t4 = threading.Thread(target=task2, name='t4')
        t5 = threading.Thread(target=task2, name='t5')
        t6 = threading.Thread(target=task2, name='t6')
        t7 = threading.Thread(target=task2, name='t7')
        t8 = threading.Thread(target=task2, name='t8')
        t9 = threading.Thread(target=task2, name='t9')
        t10 = threading.Thread(target=task2, name='t10')
        t11 = threading.Thread(target=task2, name='t11')
        t12 = threading.Thread(target=task2, name='t12')

        print(time.time_ns() / 1000000000)
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

        print(time.time_ns() / 1000000000)

    if threads == 13:
        t1 = threading.Thread(target=task2, name='t1')
        t2 = threading.Thread(target=task2, name='t2')
        t3 = threading.Thread(target=task2, name='t3')
        t4 = threading.Thread(target=task2, name='t4')
        t5 = threading.Thread(target=task2, name='t5')
        t6 = threading.Thread(target=task2, name='t6')
        t7 = threading.Thread(target=task2, name='t7')
        t8 = threading.Thread(target=task2, name='t8')
        t9 = threading.Thread(target=task2, name='t9')
        t10 = threading.Thread(target=task2, name='t10')
        t11 = threading.Thread(target=task2, name='t11')
        t12 = threading.Thread(target=task2, name='t12')
        t13 = threading.Thread(target=task2, name='t13')

        print(time.time_ns() / 1000000000)
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
        t13.start()

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
        t13.join()

        print(time.time_ns() / 1000000000)

    if threads == 14:
        t1 = threading.Thread(target=task2, name='t1')
        t2 = threading.Thread(target=task2, name='t2')
        t3 = threading.Thread(target=task2, name='t3')
        t4 = threading.Thread(target=task2, name='t4')
        t5 = threading.Thread(target=task2, name='t5')
        t6 = threading.Thread(target=task2, name='t6')
        t7 = threading.Thread(target=task2, name='t7')
        t8 = threading.Thread(target=task2, name='t8')
        t9 = threading.Thread(target=task2, name='t9')
        t10 = threading.Thread(target=task2, name='t10')
        t11 = threading.Thread(target=task2, name='t11')
        t12 = threading.Thread(target=task2, name='t12')
        t13 = threading.Thread(target=task2, name='t13')
        t14 = threading.Thread(target=task2, name='t14')

        print(time.time_ns() / 1000000000)
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
        t13.start()
        t14.start()

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
        t13.join()
        t14.join()

        print(time.time_ns() / 1000000000)

    if threads == 15:
        t1 = threading.Thread(target=task2, name='t1')
        t2 = threading.Thread(target=task2, name='t2')
        t3 = threading.Thread(target=task2, name='t3')
        t4 = threading.Thread(target=task2, name='t4')
        t5 = threading.Thread(target=task2, name='t5')
        t6 = threading.Thread(target=task2, name='t6')
        t7 = threading.Thread(target=task2, name='t7')
        t8 = threading.Thread(target=task2, name='t8')
        t9 = threading.Thread(target=task2, name='t9')
        t10 = threading.Thread(target=task2, name='t10')
        t11 = threading.Thread(target=task2, name='t11')
        t12 = threading.Thread(target=task2, name='t12')
        t13 = threading.Thread(target=task2, name='t13')
        t14 = threading.Thread(target=task2, name='t14')
        t15 = threading.Thread(target=task2, name='t15')

        print(time.time_ns() / 1000000000)
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
        t13.start()
        t14.start()
        t15.start()

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
        t13.join()
        t14.join()
        t15.join()

        print(time.time_ns() / 1000000000)

thread()
#
# t1 = threading.Thread(target=task2, name="task1")
#
# t2 = threading.Thread(target=task2, name="task2")
#
# t3 = threading.Thread(target=task2, name="task3")
#
# t4 = threading.Thread(target=task2, name="task4")
#
# t5 = threading.Thread(target=task2, name="task5")
#
# t6 = threading.Thread(target=task2, name="task6")
#
# t7 = threading.Thread(target=task3, name="task7")
#
# t8 = threading.Thread(target=task3, name="task8")
#
# t9 = threading.Thread(target=task3, name="task9")
#
# t10 = threading.Thread(target=task3, name="task10")
#
# t11 = threading.Thread(target=task3, name="task11")
#
# t12 = threading.Thread(target=task3, name="task12")
#
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()
# t7.start()
# t8.start()
# t9.start()
# t10.start()
# t11.start()
# t12.start()
#
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
# t6.join()
# t7.join()
# t8.join()
# t9.join()
# t10.join()
# t11.join()
# t12.join()
correct = password_length - len(generated_password)
print(correct)

for i in range(0, correct):
    t = random.randint(0, len(password_all_characters) - 1)
    generated_password = generated_password + password_all_characters[t]

print(generated_password)
print(len(generated_password))
write = input("would you like to save this")
if write.__contains__("y"):
    password = open("passwords.txt", "a")
    label = input("What is the label for your passwords")
    generated_password = (label + ":" + "\r\n" + "  " + generated_password + "\r\n")
    password.write(generated_password)
    password.close()

find = input("Would you like to find a password?")
if find.__contains__("y"):
    fin = open("passwords.txt")
    for element in fin:
        print(element)

if find.__contains__("n"):
    exit
    SystemExit
