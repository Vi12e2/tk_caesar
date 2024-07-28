from au_functions import rus_, eng_

def encrypt(msg, shift):
    rus = rus_()
    eng = eng_()
    rs = ""

    for c in msg:
        if c.isalpha():
            if c in eng:
                a = ord('A') if c.isupper() else ord('a')
                rs += chr(a + (ord(c) + shift - a) % 26)
            elif c in rus:
                a = ord('А') if c.isupper() else ord('а')
                rs += chr(a + (ord(c) + shift - a) % 32)
        else:
            rs += c
    return rs
