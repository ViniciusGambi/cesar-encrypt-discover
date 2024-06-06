import sys
from base64 import b64encode, b64decode
from Cryptodome.Cipher import AES
from Cryptodome.Hash import BLAKE2s

def encrypt_aes_gcm(plaintext, password):
    key = BLAKE2s.new(digest_bits=128, key=password).digest()
    cipher = AES.new(key, AES.MODE_GCM)
    nonce = cipher.nonce
    ct_bytes, tag = cipher.encrypt_and_digest(plaintext)
    
    nonce_b64 = b64encode(nonce).decode('utf-8')
    ct_b64 = b64encode(ct_bytes).decode('utf-8')
    tag_b64 = b64encode(tag).decode('utf-8')
    
    return nonce_b64, ct_b64, tag_b64

def decrypt_aes_gcm(ciphertext_b64, nonce_b64, tag_b64, password):
    ciphertext = b64decode(ciphertext_b64)
    nonce = b64decode(nonce_b64)
    tag = b64decode(tag_b64)
    
    key = BLAKE2s.new(digest_bits=128, key=password).digest()
    
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    
    return plaintext.decode('utf-8')

def main():
    plaintext = "CESAR School"
    password = "SuaSenha"


    # Criptografar
    plaintext_bytes = plaintext.encode('utf-8')
    password_bytes = password.encode('utf-8')
    
    nonce_b64, ct_b64, tag_b64 = encrypt_aes_gcm(plaintext_bytes, password_bytes)
    print("Nonce: ", nonce_b64)
    print("Texto cifrado: ", ct_b64)
    print("Tag: ", tag_b64)
    
    # Descriptografar
    decrypted_text = decrypt_aes_gcm(ct_b64, nonce_b64, tag_b64, password_bytes)
    print("Texto descriptografado: ", decrypted_text)

if __name__ == "__main__":
    main()
