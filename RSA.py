from random import randint
 
def GenPrime():

    small_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                   37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
                   79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
                   131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
                   181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251]

    while True:

        PotentialPrime = True

        num = randint(1999, 4999)

        if num % 2 == 0:
            num += 1

        for pr in small_primes:
            if num % pr == 0:
                PotentialPrime = False
                break

        if not PotentialPrime:
            continue

        n = num - 1

        s, d = 0, 0
        while True:
            if n % 2 == 0:
                n //= 2
                s += 1
            else:
                d = n
                n = num - 1
                break

        for i in range(5):

            a = randint(1, n)
            PotentialPrime = False

            for j in range(s):
                test = pow(a, 2 ** j * d, num)
                if test == 1 or test == n:
                    PotentialPrime = True
                    break

            if not PotentialPrime:
                break

        if PotentialPrime:
            return num

def gcd(a, b):

    if (a == 0):
        return b
    else:
        return gcd(b % a, a)

def ChooseE(u):

    while True:
        num = randint(3, u-1)
        if gcd(num, u) == 1:
            return num

def xgcd(a, b):
    
    x, old_x = 0, 1
    y, old_y = 1, 0

    while (b != 0):
        quotient = a // b
        a, b = b, a - quotient * b
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    return a, old_x, old_y


p, q = GenPrime(), GenPrime()
print("p = ", p)
print("q = ", q)

n = p * q
print("n = ", n)

u = (p - 1) * (q - 1)
print("u = ", u)

e = ChooseE(u)
print("e = ", e)

gcd, x, y = xgcd(e, u)

if (x < 0):
    d = x + u
else:
    d = x

print("d = ", d)

private_key = (d, n)
public_key = (e, n)
print("Секретный ключ - (", d, ',', n, ')', sep = '')
print("Публичный ключ - (", e, ',', n, ')', sep = '')


Bob_message = "This is a message"
print("Сообщение Боба: ", Bob_message)

Bob_crypted_message = list()

print("Зашифрованное сообщение Боба:")
for i in range(len(Bob_message)):
    Bob_crypted_message.append(pow(ord(Bob_message[i]), public_key[0], public_key[1]))
    print(Bob_message[i], '\t', ord(Bob_message[i]), '\t', Bob_crypted_message[i])

Bob_decrypted_message = str()

for i in range(len(Bob_crypted_message)):
    Bob_decrypted_message += chr(pow(Bob_crypted_message[i], private_key[0], private_key[1]))
    print(Bob_crypted_message[i], '\t', ord(Bob_decrypted_message[i]), '\t', Bob_decrypted_message[i])

print("Расшифрованное Алисой сообщение: ", Bob_decrypted_message)