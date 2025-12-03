from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

print(private_key)
print(public_key)

def encrypt(data):
    encrypted = public_key.encrypt(data.encode(), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                               algorithm=hashes.SHA256(),
                                                               label=None))
    return encrypted

encrypted_data = encrypt("привет!")

def decrypt(encrypted_data):
    decrypted = private_key.decrypt(encrypted_data, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                               algorithm=hashes.SHA256(),
                                                               label=None))
    return decrypted.decode()

print(encrypted_data)
print(decrypt(encrypted_data))