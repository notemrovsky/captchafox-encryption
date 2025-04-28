import json
import gzip

def encrypt_data(data):
    json_str = json.dumps(data)
    
    compressed = gzip.compress(json_str.encode('utf-8'))
    
    obfuscated = bytearray(len(compressed))
    
    for i in range(len(compressed)):
        obfuscated[i] = (compressed[i] ^ ((i + 4) % 256)) % 256
    
    encrypted_data = bytearray([1, 4]) + obfuscated
    
    return encrypted_data

def decrypt_data(encrypted_data):
    encrypted_data = bytes(value % 256 for value in encrypted_data)

    deobfuscated = bytearray(len(encrypted_data) - 2)
    
    for i in range(2, len(encrypted_data)):
        deobfuscated[i - 2] = (encrypted_data[i] ^ ((i - 2 + 4) % 256)) % 256
    
    decompressed = gzip.decompress(bytes(deobfuscated))
    
    json_str = decompressed.decode('utf-8')
    
    return json.loads(json_str)

if __name__ == "__main__":
    decrypted = encrypt_data(json.loads(open("fingerprint.json","r").read()))
    print(decrypted)

    
    encrypted = decrypt_data(decrypted)
    print(encrypted)

