a = int(input("a-> "))

print('#>------------------------<#')
print('Action 1 - meters in miles')
print('Action 2 - meters in inches')
print('Action 3 - meters in yards')
print('#>------------------------<#')

action = input('Enter your action(1 2 3): ')

if action == '1':
    res = a * 0.000621
    print("Ur result in miles" + " " + str(res))
elif action == '2':
    res = a * 39.37
    print("Ur result in inches" + " " + str(res))
elif action == '3':
    res = a * 1.09
    print("Ur result in yards" + " " + str(res))
else:
    print("Command not found")
print("Good luck !")

