passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()
print('Enter Your Password.')
typedPassword = input()
if typedPassword == secretPassword:

    print('Access granted')
elif typedPassword == 'YougotGot':
        print('That password is one that an idiot puts on their luggage!')
else: 
    print('Access denied')