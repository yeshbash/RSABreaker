import math
from decimal import *
import datetime

getcontext().prec = 300
square_residue = [0,1,4,5,9,16]

#Checks if 'number' is a perfect square or not
def isPerfectSquare(number):
	if(number%20 in square_residue):
		x = Decimal(number).sqrt()
		ceil = math.ceil(x)
		floor = math.floor(x)
		if(floor == ceil):
			return True
	return False

#Calculates RSA private key from e(exponent) and totien(n)
#Uses Extended Euclidean algorithm to find private_key (d)
def private_key(e, totient):
    z,x,c,v=0,1,1,0
    while e != 0:
        q = totient//e
        r = totient%e
        m = z-c*q
        n = x-v*q
        totient,e=e,r
        z,x = c,v
        c,v =  m,n
        gcd = totient
    return z

#Decrypts cipher text from private_key -d and public key N
def decrypt_cipher_text(ct,d,N):
        plain= pow(ct,d,N)
        return plain

#Converts binary data to ascii string
def bin_to_ascii(bin_data):
	step =8
	data_len = len(bin_data)
	#processes input binary string as groups of 8 bits
	int_ascii_data = bytes(int(bin_data[start:start+step],2) for start in range(0,data_len,step))
	return int_ascii_data.decode()
		
def fermat_factorization(number):
	xPart = int(math.ceil(Decimal(key).sqrt()))
	y2Part = xPart**2 - key
	while(isPerfectSquare(y2Part) ==False):
		y2Part = y2Part+2*xPart+1
		xPart = xPart+1
	yPart = int(Decimal(y2Part).sqrt())
	return xPart+yPart,xPart-yPart
	
		
#Main Logic
start_time = datetime.datetime.now()
print("RSA Breaker")
print("="*15)

cipher_text = int(input("Enter the cipher text : "))
key = int(input("Public Key : "))
e = int(input("Public Exponent: "))

print("Breaking the key...")
#Key factorization and totient calculation
p, q = fermat_factorization(key)
N = p*q
if(N == key):
	print("\n====RSA private key cracked!======")
	totient=(p-1)*(q-1)

	#Private Key calcuation and Decryption
	d= private_key(e,totient)
	padded_plain_text=decrypt_cipher_text(cipher_text,d,N)

	#Padding data strip and ascii conversion
	bin_plain_text = bin(padded_plain_text)[-200:]
	plain_text = bin_to_ascii(bin_plain_text)
	
	time_taken = datetime.datetime.now() - start_time
	
	print("\nKey Summary:\nP : ",p,"\nQ : ",q,"\nPrivate Exponent d : ",d)
	print("\nPlain Text : ", plain_text)
	print("\nTime Taken [Days:Seconds] : [",time_taken.days,":",time_taken.seconds,"]")
else:
	print("Breaking RSA instance failed")