import hashlib

def sha256_hash_gen_file(user_file):
    with open(user_file, 'rb') as f:
        return hashlib.file_digest(f, "sha256").hexdigest()

def sha256_hash_gen_str(user_str):
    return hashlib.sha256(bytes(user_str, encoding="utf-8")).hexdigest()

def prompt_user():
    print("Do you want to SHA-256 hash a file or string?")
    response = ''
    while response not in {"file", "string"}:
        response = input("Please enter file or string: ").lower()
    return response

user_response = prompt_user()

if user_response == "string":
    user_str = input("Enter the string: ")
    print(sha256_hash_gen_str(user_str))
elif user_response == "file":
    user_file = input("Enter the file name: ")
    print(sha256_hash_gen_file(user_file))