print("Welcome to the best programm forever")
print("Print 3 numbers")
a = int(input('a-> '))
b = int(input('b-> '))
c = int(input('c-> '))
print('#>--Let`s choose action--<#')
action = input('Enter your action(min max avg): ')

if action == 'min':
    print(min(a, b,c))
elif action == 'max':
    print(max(a, b,c))
elif action == 'avg':
    print((a + b + c) / 3)
else:
    print("Entered wrong number/sign")