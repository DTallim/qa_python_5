import random

def generates_email(email_char_num):
    email=''.join(random.choice(list('1234566789qwerty'))for i in range(email_char_num))
    return f'{email}@yandex.ru'

def generates_password(psw_char_num):
    psw =''.join(random.choice(list('123456789qwertyQWERTY')) for x in range(psw_char_num))
    return psw
