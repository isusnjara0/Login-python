print('Dobrodošli u Unidu sustav!')
print('Za prijavu upišite broj 1, za registraciju broj 2: ')

x = 0 
email=''
lozinka=''

xemail = 'korisnik@gmail.com'
xlozinka = 'lozinka'

while(not(x==1 or x==2)):
    x = int(input('unesite broj: '))

    if(x==1):
        email = input('Unesite email: ')
        lozinka = input('Unesite lozinku: ')

        if(email==xemail and lozinka==xlozinka):
            print('Uspješna prijava!')
        else:
            print('Pogrešan email ili lozinka')

    if(x==2):
        print('Registracija!')

    
    
