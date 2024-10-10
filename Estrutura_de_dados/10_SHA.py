import hashlib

def criptografar(texto):
   
    hash_sha256 = hashlib.sha256()
    hash_sha256.update(texto.encode())
    
    return hash_sha256.hexdigest()

texto = "Senha123"
texto2 = "senha123"
valorHash = criptografar(texto)
valorHash2 = criptografar(texto2)
print(f"O hash SHA-256 da mensagem '{texto}' é: {valorHash}")
print(f"O hash SHA-256 da mensagem '{texto2}' é: {valorHash2}")
