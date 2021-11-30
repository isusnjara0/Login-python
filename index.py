import sqlite3
import hashlib
import time
from datetime import date

def register_user(name, email, password, contact):
    today = date.today()
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    query = cur.execute("INSERT INTO user (name, email, password, contact, created_at) VALUES (?, ?, ?, ?, ?)", (name, email, password, contact, today))
    con.commit()
    con.close()

def login():
    email = input("Unesite e-mail: ")
    pwd = input("Unesite lozinku: ")
    pwd = hashing(pwd)
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    broj_prijava = 0
    for row in cur.execute('SELECT * FROM user'):
        rowEmail =  row[2]
        rowPwd = row[3]
        if(email == rowEmail and pwd == rowPwd):
            broj_prijava = int( row[4])
            broj_prijava += 1
            query = 'UPDATE user SET broj_prijava='+str(broj_prijava)+' WHERE id='+str(row[0])+';'
            cur.execute(query)
            con.commit()
            print('Uspješna prijava!')
            return
    print('Krivi email ili password!')
    return

def hashing(pwd):
    result = hashlib.sha256(pwd.encode('utf-8')).hexdigest()
    return result

def forgot_password(email):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    for row in cur.execute('SELECT id, email FROM user'):
        if (email == row[1]):
            t0 = int(time.time())
            t1 = t0 + 60*30
            datum = time.strftime("%I %M %p",time.localtime(t1))
            print(datum)
            usr_id = row[0]
            cur.execute('INSERT OR REPLACE INTO forgot_password (user_id, hash, valid_until) VALUES (?, ?, ?)', (usr_id, hashing(str(t0)), datum))
            con.commit()
            con.close()
            nova_lozinka(usr_id)

            return
    print('Email ne postoji u bazi!')
    return

def nova_lozinka(usr_id):
    print('Promjena loznike\n')
    pwd = input('Unesite novu lozinku: ')
    pwd2 = input('Potvrda lozinke: ')

    if(pwd == pwd2):
        con = sqlite3.connect('baza.db')
        cur = con.cursor()
        query = 'UPDATE user SET password="'+hashing(pwd)+'" WHERE id='+str(usr_id)+';'
        cur.execute(query)
        con.commit()
        print('Lozinka uspješno promijenjena!');
        return
    
    print('Lozinke se ne podudaraju!')
    return
        
    

print("Dobrodošli u Unidu sustav!")
print("Za prijavu upišite broj 1, za registraciju broj 2, za zaboravljenu lozinku:")
odabir = int(input("Unesite broj: "))

while odabir != 1 and odabir != 2 and odabir !=3:
    odabir = int(input("Unesite broj: "))


if odabir == 1:
    print("Dobrodošli u prijavu!")
    login()

elif odabir == 2:
    print("Dobrodošli u registraciju!")
    name = input("Unesite Vaše ime: ")
    email = input("Unesite e-mail: ")
    pwd = input("Unesite lozinku: ")
    contact = input("Unesite kontakt broj: ")
    register_user(name, email, hashing(pwd), contact)

else:
    print('Zaboravljena lozinka')
    email = input("Unesite e-mail: ")
    forgot_password(email)
    
    




    
    
