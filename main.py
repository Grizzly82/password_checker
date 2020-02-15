#program is checking the lengh of the users password

username = input('enter your username: ')
password = input('enter your password: ')

password_ = '*' * len(password)

print(f'Hello {username}, your password {password_} is {len(password)} long')