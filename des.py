# pip install pycryptodome
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Function to encrypt using DES
def des_encrypt(plaintext, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext.encode(), DES.block_size)  # Padding plaintext to fit block size
    encrypted_text = des.encrypt(padded_text)
    return encrypted_text

# Function to decrypt using DES
def des_decrypt(ciphertext, key):
    des = DES.new(key, DES.MODE_ECB)
    decrypted_text = unpad(des.decrypt(ciphertext), DES.block_size)
    return decrypted_text.decode()

# Example usage
if __name__ == "__main__":
    print("\nTest 1")

    # 8-byte (64-bit) DES key
    key1 = get_random_bytes(8)  

    # Original plaintext message
    text1 = "Heavy is the crown"

    # Encrypting the plaintext
    ciphertext1 = des_encrypt(text1, key1)
    print(f"Encrypted: {ciphertext1}")

    # Decrypting the ciphertext
    decrypted_text = des_decrypt(ciphertext1, key1)
    print(f"Decrypted: {decrypted_text}")

    print("\n\nTest 2")
    key2 = get_random_bytes(8)
    text2 = "yaaaayyy"
    ciphertext2 = des_encrypt(text2, key2)
    print(f"Encrypted: {ciphertext2}")

    # Decrypting the ciphertext
    decrypted_text = des_decrypt(ciphertext2, key2)
    print(f"Decrypted: {decrypted_text}")
    
