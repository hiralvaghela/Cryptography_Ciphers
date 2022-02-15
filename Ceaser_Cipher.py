def encrypt(t,s):
    text=''
    for i in t:
        if(i.isupper()):
            text=text+chr((ord(i)+s-65)%26+65)
        else:
            text=text+chr((ord(i)+s-97)%26+97)
    print('Encrypted Text: '+text)
    return text

def decypt(t,s):
    dtext=''
    for i in t:
        if(i.isupper()):
            dtext=dtext+chr((ord(i)-s-65)%26+65)
        else:
            dtext=dtext+chr((ord(i)-s-97)%26+97)
    print('decrypted Text: '+dtext)
    return dtext        

text=input('Enter message: ')
shift=int(input('Enter Shift: '))
print('Plain Text: '+text)
decypt(encrypt(text,shift),shift)