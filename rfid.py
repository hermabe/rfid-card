import serial

def reverseBytes(number):
    binary = "{0:0>32b}".format(number) # Zero-padded 32-bit binary
    byteList = [binary[i:i+8][::-1] for i in range(0, 32, 8)] # Reverse each byte
    return int(''.join(byteList), 2) # Join and convert to decimal
    # return int(''.join(["{0:0>32b}".format(number)[i:i+8][::-1] for i in range(0, 32, 8)]), 2)

def dataChecks(data, length):
    if data[-1] != 3:
        return "No stop byte"
    BCC = length
    for d in data[:-1]:
        BCC ^= d
    print(BCC)
    if BCC != 0:
        return "Parity error"

ser = serial.Serial('/dev/serial0')

print("Scanning for cards:")
while True:
    if ser.in_waiting > 0:
        byte = ser.read(1)[0]
        if byte == 2: # Startbyte
            length = ser.read(1)[0] # Total length, including start and length bytes            
            data = ser.read(length-2).hex()
            reversedEM = int(data[4:12], 16)
            EM = reverseBytes(reversedEM)
            print('EM ' + str(EM).zfill(10))
 
