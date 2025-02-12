# AICTE-Project
# Image-Based Steganography with Password Protection

This project demonstrates a simple yet effective **image-based steganography** technique to securely hide and retrieve messages within an image. It uses pixel manipulation to embed a secret message and allows decryption only with the correct password.

---

## **Features**
- **Embed Secret Message**: Hide a message inside an image by modifying pixel values.
- **Password Protection**: Only the correct password allows access to the hidden message.
- **Lightweight and Fast**: Efficient and resource-friendly encryption and decryption process.
- **No Database Needed**: Stores encryption details in a text file.
- **Cross-Compatible**: Works with multiple image formats supported by OpenCV.

---

## **Technologies Used**
- **Programming Language**: Python(V3.12)
- **Libraries**:  
  - `OpenCV (cv2)` for image manipulation
  - `os` for file handling
- **IDE/Editor**: VS Code (Visual Studio Code)
- **Platform**: Windows (can be adapted for Linux/macOS)

---

## **Getting Started**

### **1. Prerequisites**
Ensure you have Python 3.x installed on your system. You will also need to install OpenCV.

To install OpenCV:
```bash
pip install opencv-python
```

### **2. Running the Project**
1. **Encrypt a Message**:
   - Place the image file (`image.png`) you want to hide the message in.
   - Run the script to input a secret message and password. The message will be embedded into the image, and an encrypted image (`encryptedImage.png`) will be generated.

2. **Decrypt the Message**:
   - Run the decryption script and input the correct password to retrieve the secret message from the encrypted image.

---

## **File Structure**

```
AICTE-Project/
│
├── image.png                  # Original image to hide the message
├── encryptedImage.png         # Encrypted image with hidden message
├── encryption_info.txt        # Stores the password and message length
└── README.md                  # Project documentation
```

---

## **Usage Example**

**Encryption Script**:
```python
Enter secret message: Hello, World!
Enter a passcode: 1234
Encryption complete. Encrypted image saved as 'encryptedImage.png'.
```

**Decryption Script**:
```python
Enter passcode for Decryption: 1234
✅ Decrypted message: Hello, World!
```

---
