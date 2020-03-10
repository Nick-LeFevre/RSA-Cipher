def main():
    z = int(input("Choose\n1) Encryption\n2) Decryption\n> "))
    if z == 1:
        pt = input("Enter plaintext: >")
        p = int(input("Enter 2 Prime Numbers > "))
        q = int(input("> "))
        e = int(input("Enter exponent 'e' relatively prime to n > "))
        if isPrime(p) and isPrime(q) and coprime(e,(p-1)*(q-1)):
            print(encrypt(pt,p,q,e))
        else:
            print("Invalid Keys")
    elif z == 2:
        ct = input("Enter ciphertext > ")
        p = int(input("Enter 2 Prime Numbers > "))
        q = int(input("> "))
        e = int(input("Enter exponent 'e' relatively prime to n > "))
        if isPrime(p) and isPrime(q) and coprime(e,(p-1)*(q-1)):
            print(encrypt(ct,p,q,e))
        else:
            print("Invalid Keys")
    else:
        print("Invalid Input")
    main()

def encrypt(pt,p,q,e): #encrypt function
    decimal = dec(pt)
    m = p*q
    n = (p-1)*(q-1)
    d = imod(e,n)
    return text((decimal**e)%m)

def decrypt(ct,p,q,e): #decrypt function
    decimal = dec(ct)
    m = p*q
    n = (p-1)*(q-1)
    d = imod(e,n)
    return text((decimal**e)%m)

def text(num): #converts the decimal to a text
    i = 0
    x = []
    while(num > 0):
        x.append(chr((num%26)+97))
        num = num//26
        i += 1
    x.reverse()
    return "".join(x)

def dec(text): #converts the text to a decimal
    tot = 0
    z = len(text)-1
    for i in text:
        t = ord(i)-97
        tot = tot + (t*26**z)
        z -= 1
    return tot

def gcd(a,b): #GCD function that is used in the coprime function
    while b != 0:
        a,b = b, a % b
    return a

def coprime(a,b): #checks if it is relatively prime
    return gcd(a,b) == 1

def isPrime(n): #checks if the number is prime
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def imod(e,m): #inverse mod function
    for i in range(1,m):
        if (m*i + 1) % e == 0:
            return (m*i + 1) // e
    return None
main()
