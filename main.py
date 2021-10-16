# This is a short project that shows different solutions for the
# classic programming interview question FizzBuzz that still many companies use it
# as benchmark for new employees. The problem is:
# Looping through numbers from 1 to 100, if the number is divisible by 3 then print Fizz
# if the number is divisible by 5 then print Buzz, if the number is divisible by 3 and 5
# then print FizzBuzz and if the number is not divisible by 3 and 5 print the number

def fizzBuzzClassic():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(str(i))

def fizzBuzzWhile():
    i = 1
    while i < 101:
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
            i += 1
        elif i % 3 == 0:
            print('Fizz')
            i += 1
        elif i % 5 == 0:
            print('Buzz')
            i += 1
        else:
            print(str(i))
            i += 1

def fizzBuzzMathLogic():
    for i in range(1, 101):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(str(i))

def fizzBuzzConcatenation():
    for i in range(1, 101):
        conca = ''
        if i % 3 == 0:
            conca = 'Fizz'
        if i % 5 == 0:
            conca = conca + 'Buzz'
        if conca == '':
            conca = str(i)
        print(conca)

def fizzBuzzConcatenationReminder():
    mod3 = 0
    mod5 = 0
    for i in range(1, 101):
        conca = ''
        mod3 += 1
        mod5 += 1
        if mod3 == 3:
            mod3 = 0
            conca = 'Fizz'
        if mod5 == 5:
            mod5 = 0
            conca = conca + 'Buzz'
        if conca == '':
            conca = str(i)
        print(conca)

def fizzBuzzOneLiner():
    for i in range(1, 101):
        print('Fizz'* (i % 3 == 0) + 'Buzz'* (i % 5 == 0) or i)

