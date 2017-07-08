#!/usr/bin/env python3

calc_on = True 

def addition():
    first = int(raw_input("First number:"))
    second = int(raw_input("Second number:"))
    print (first + second)

def subtraction():
    first = int(raw_input("First number:"))
    second = int(raw_input("Second number:"))
    print (first - second)

def multiplication():
    first = int(raw_input("First number:"))
    second = int(raw_input("Second number:"))
    print (first * second)

def division():
    first = int(raw_input("First number:"))
    second = int(raw_input("Second number:"))
    print (first / second)

def modulo():
    first = int(raw_input("First number:"))
    second = int(raw_input("Second number:"))
    print (first % second)

def quit():
    global calc_on
    calc_on = False
        
def calc_run():

    op = raw_input('add, subtract, multiply, divide, modulo, quit? ')
    
    if op == 'add':
        addition()
    elif op == 'subtract':
        subtraction()
    elif op == 'multiply':
        multiplication()
    elif op == 'divide':
        division()
    elif op == 'modulo':
        modulo()
    else:
        quit()

while calc_on == True:
    calc_run()


