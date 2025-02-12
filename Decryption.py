import cv2

# Load the encrypted image
img = cv2.imread("Stenography-main\\encryptedImage.png")

# Load the password and message length from the file
with open("Stenography-main/encryption_info.txt", "r") as f:
    stored_password = f.readline().strip()
    msg_length = int(f.readline().strip())

# Input password for decryption
pas = input("Enter passcode for Decryption: ")

# Create dictionaries for integer to character mapping
c = {i: chr(i) for i in range(255)}

# Initialize variables for pixel manipulation
m, n, z = 0, 0, 0

# Initialize the decrypted message
message = ""

# Check if the password is correct
if pas == stored_password:
    # Extract the secret message from the image
    for i in range(msg_length):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    print("✅ Decrypted message:", message)
else:
    print("❌ Incorrect passcode! Access Denied.")