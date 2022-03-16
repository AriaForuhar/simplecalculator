def jam(x, y):
    return x + y


def tafrigh(x, y):
    return x - y


def zarb(x, y):
    return x * y


def taghsim(x, y):
    return x / y


x = int(input('enter x:'))
y = int(input('enter y'))
opr = input('enter oprator')

if opr == '+':
    print(f'jam:{jam(x, y)}')
if opr == '-':
    print(f'tafrigh:{tafrigh(x, y)}')
if opr == '*':
    print(f'zarb:{zarb(x, y)}')
if opr == '/':
    print(f'taghsim:{taghsim(x, y)}')
