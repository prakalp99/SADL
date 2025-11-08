def encrypt(msg, key):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for char in msg:
        if(char.isalpha() and char.isupper()):
            
            p=upper.index(char)
            result+=upper[(p+key)%26]
        elif(char.isalpha() and char.islower()):
            p=lower.index(char)
            result+=lower[(p+key)%26]
        else:
            result+=char
        
    return result

def decrypt(e_msg, key):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for char in e_msg:
        if(char.isalpha() and char.isupper()):
            p = upper.index(char)
            result+=upper[(26+p-key)%26]
        elif(char.isalpha() and char.islower()):
            p = lower.index(char)
            result+=lower[(26+p-key)%26]
        else:
            result+=char
    return result


msg = input("Enter the message: ")
key = int(input("Enter the Key: "))
e_msg=encrypt(msg, key)
print(e_msg)

print(decrypt(e_msg, key))


