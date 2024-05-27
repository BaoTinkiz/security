import os

# Hàm giải mã tệp
def decrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as f:
            ciphertext = f.read()

        plaintext = bytearray(ciphertext)
        for i in range(len(plaintext)):
            plaintext[i] ^= key

        with open(file_path[:-10], 'wb') as f: # Loại bỏ phần mở rộng .encrypted
            f.write(plaintext)
        
        os.remove(file_path)
    except Exception as e:
        print("Error:", str(e))

# Khóa mã hóa
key = 0x42

# Thư mục mục tiêu
target_directory = r"C:\Users\asus\Desktop\cc"

# Giải mã tất cả các tệp đã mã hóa trong thư mục
for root, dirs, files in os.walk(target_directory):
    for file in files:
        if file.endswith(".encrypted"):
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

