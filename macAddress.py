import uuid
print("Your mac address is: ", end="")
print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
               for ele in range(0, 8 * 6, 8)][::-1]))