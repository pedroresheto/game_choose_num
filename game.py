import random

secret = random.randint(1, 50)

chanses = 5

while (chanses > 0):
    #working
    user = int(input('Choose the number:'))
    print('your number is ', user)
    if(user == secret):
        print('You are win!')
        break
    else:
        print('wrong number, you also have ', chanses, 'chanses')
        if(user > secret):
            print('your number is bigger than secret')
        else:
            print('your number is less than secret')
        chanses -= 1
else:
    print('You are lose!')