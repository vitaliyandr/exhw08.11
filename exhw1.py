a = int(input('a-> '))
b = int(input('b-> '))
c = int(input('c-> '))

action = input('Enter your action(+ *): ')

if action == '+':
    res = a + b + c
    print("Ur result" + " " + str(res))
elif action == '*':
    res = a * b * c
    print("Ur result" + " " + str(res))
else:
    print("Entered wrong number/sign")
print("Good Luck!")
