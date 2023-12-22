import random
import string
import time

list=["12"]

def generate_key():
    
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbol2=string.punctuation
    
    nr_letters = 4
    nr_symbols = 2
    nr_numbers = 2

    password = []

    while nr_letters > 0:
        pass_lett = random.choice(letters)
        password.append(pass_lett)
        nr_letters -= 1

    while nr_numbers > 0:
        pass_num = random.choice(numbers)
        password.append(pass_num)
        nr_numbers -= 1

    while nr_symbols > 0:
        pass_sym = random.choice(symbol2)
        password.append(pass_sym)
        nr_symbols -= 1

    random.shuffle(password)
    return("".join(password))




def check_duplicate():
         
    key=generate_key()
    #key="12"
    for l in list:
        if l == key:
            print("key exist program exited")
            exit()
    else:
        list.append(key)



check_duplicate()
time.sleep(5)
check_duplicate()
time.sleep(5)
check_duplicate()
time.sleep(5)
check_duplicate()

def frequency_test(sequence):
    frequency = sequence.count('4')
    total = len(sequence)
    return abs(frequency - (total - frequency)) / total

sequence = generate_key()
print(frequency_test(sequence))

print(list)
