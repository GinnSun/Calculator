#calculator
import math
print('''And so this is my first Python calculator.
it has a lot of features,
and soon you will be able to look at them,
and also ask them to solve some equation
do not judge strictly (^-^)
''')
choice = int(input('Choose from 1 to 8: '))
while choice <= 0 or choice >= 9:
    print('ERROR!!! Enter the correct value!!')
    choice = int(input('Choose from 1 to 8: '))
if choice == 1:
    print('Well done! You chose addition \nlets do it!')
    a, b = map(int, input('a, b = ').split())
    print('a+b =', a+b)
elif choice == 2:
    print('there will be subtraction')
    a2, b2 = map(int, input('a2, b2 = ').split())
    print('a2-b2 =', a2-b2)
elif choice == 3:
    print('its *')
    a3, b3 = map(float, input('a3, b3 = ').split())
    print('a3*b3 =', a3 * b3)
elif choice == 4:
    print('its / ')
    a4, b4 = map(float, input('a4, b4 = ').split())
    print('a4/b4 =', a4 / b4)
elif choice == 5:
    print('its division by remainde ')
    a5, b5 = map(float, input('a5, b5 = ').split())
    if b5 >= 10:
        print('a5%b5 =', a5 % b5)
    elif a5 >= 10:
        print('a5%b5 =', b5 % a5)
    else:
        print('a5%b5 =', a5 % b5)
elif choice == 6:
    print('finding the factorial of a number')
    a6 = int(input('a6 = '))
    print(math.factorial(a6))
elif choice == 7:
    print('exponentiation')
    a7 = int(input('a7 = '))
    print(pow(a7, 2))
elif choice == 8:
    print('Square root')
    a8 = int(input('a8 = '))
    print('sqrt = ', math.sqrt(a8))
ChoiceNumber = []
for i in range(3):
    ChoiceNumber.append(int(input('Choice 1.sqrt(a^2+b^2), 2.a = sqrt(с^2 - b^2), 3.b = sqrt(с^2 - a^2): \n')))
    print('that you would like to conclude an agreement?')
a1 = int(input('Please enter values to use the Pythagorean Theorem, a1 ='))
b1 = int(input('Please enter values to use the Pythagorean Theorem, b1 ='))
c1 = int(input('Please enter values to use the Pythagorean Theorem, c1 ='))
for i1 in ChoiceNumber:
    if i1 == 1:
        print('sqrt(a^2+b^2) = ', math.sqrt((a1**2 + b1**2)))
        break
    elif i1 == 2:
        print('a = sqrt(с^2 - a^2) = ', math.sqrt(c1 ** 2 - b1 ** 2))
        break
    elif i1 == 3:
        print('b = sqrt(с^2 - a^2) = ', math.sqrt(c1 ** 2 - a1 ** 2))
        break
input('Press ENTER to exit') 