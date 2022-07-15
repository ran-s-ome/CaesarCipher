def encrypt(a, shift):
    result = ""                     
    for i in range(len(a)):
        char = a[i]
        if(char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

def decrypt(a, shift):
    result = ""
    for i in range(len(a)):
        char = a[i]
        if(char.isupper()):
            result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) - shift - 97) % 26 + 97)
    return result

while True:
    print("    [+] Welcome To Text Encrypter [+]       ")
    print('''
     Your Options are the following -
            1. Encrypt
            2. Decrypt
            3. Exit\n''')
    option = int(input("Choose your desired option(1,2,3): "))
    if option == 1:
        msg = input("Enter your message: ")
        shift = int(input("Enter your desired shift of characters: "))
        print("Your message: " + msg)
        print("Your shift: " + str(shift))
        print("Encrypted Message: " + encrypt(msg, shift))
    elif option == 2:
        msg = input("Enter your message: ")
        shift = int(input("Enter your desired shift of characters: "))
        print("Your message: " + msg)
        print("Your shift: " + str(shift))
        print("Decrypted Message: " + decrypt(msg, shift))
    elif option == 3:
        print("    [+] Quitting the program!! [+]    ")
        break
    else:
        print("    [-] Error Encountered [-]    ")
        continue
