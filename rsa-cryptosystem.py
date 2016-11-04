from decimal import * 
getcontext().prec = 300

def encrypt_decrypt(data,exponent, modulus):
	result= pow(data,exponent,modulus)
	return result

def encrypt_module():
	plain_text = input("Enter Plain Text : ")
	key = int(input("Enter Public Key : "))
	exponenet = int(input("Enter Public Exponent : "))
	
	padded_text = plain_text
	padded_bytes = bytes(padded_text,"UTF-8")
	
	result =0
	for byte_data in padded_bytes:
		result = result*1000+ byte_data
	
	cipher_text = encrypt_decrypt(result,exponenet,key)
	print("\nResult\nCipher Text : ", cipher_text)
	
def decrypt_module():
	inp_cipher_text = int(input("Enter Cipher Text : "))
	pub_key = int(input("Enter Public Key : "))
	private_exp = int(input("Enter private exponent : "))
	
	plain_text = encrypt_decrypt(inp_cipher_text,private_exp,pub_key)
	
	ascii_list = []
	while plain_text !=0:
		rem = plain_text%1000
		ascii_list.insert(0,rem)
		plain_text = plain_text//1000
	
	print ("Decrypted Message : ", bytes(ascii_list).decode())
		
while(True):
	print("\nRSA Crypto System\nSelect a choice")
	print("1. Encrypt")
	print("2. Decrypt")
	print("3. Exit")
	choice = int(input("Choice : "))
	if choice ==1:
		encrypt_module()
	elif choice==2:
		decrypt_module()
	elif choice==3:
		break;
	else:
		print("Invalid Entry. Try again..")
	