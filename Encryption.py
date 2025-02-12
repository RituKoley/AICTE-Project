import cv2
import os

# Load the image
img = cv2.imread("Stenography-main\\image.png")  # Replace with the correct image path

# Input secret message and password
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Create dictionaries for character to integer and integer to character mapping
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# Initialize variables for pixel manipulation
m, n, z = 0, 0, 0

# Embed the secret message into the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n += 1
    m += 1
    z = (z + 1) % 3

# Save the encrypted image
cv2.imwrite("Stenography-main\\encryptedImage.png", img)

# After embedding the message, save the password and message length
with open("Stenography-main\\encryption_info.txt", "w") as f:
    f.write(f"{password}\n{len(msg)}")

# Open the encrypted image (Windows)
# os.system("start Stenography-main\encryptedImage.png")

print("Encryption complete. Encrypted image saved as 'encryptedImage.png'.")