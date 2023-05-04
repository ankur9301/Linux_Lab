import sys

#This function encrypts the message with a ceaser key.
def encode(message: str, key: int)-> str:
    message = message.upper()
    cip_message = ""
    count = 0
    for c in message:
        ordd = ord(c)
        if ordd < 65 or ordd > 90:
            continue
        if count%50 == 0 and len(cip_message) != 0:
            cip_message += "\n"
        elif count%5 == 0 and len(cip_message) != 0:
            cip_message += " "
        cip_message += chr(65 + (ord(c)-65+key) % 26)
        count += 1
    return cip_message


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv)>3:
        print("invalid input")
        sys.exit(1)
    
    key = int(sys.argv[1])
    
    if len(sys.argv) == 3:
        message = sys.argv[2]
    else:
        message = sys.stdin.read()

    print(encode(message,key))
    sys.exit(0)
