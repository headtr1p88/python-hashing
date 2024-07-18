import hashlib

def sha256_hash_file(user_file):
    with open(user_file, 'rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()
    
def sha256_hash_str(user_str):
    return hashlib.sha256(user_str.encode()).hexdigest()

def prompt_user():
    print('Do you want to hash a file or a string? ')
    response = ''
    while response not in {'file', 'string'}:
        response = input("Enter 'file' or 'string': ")
    return response

user_response = prompt_user()

if user_response == 'file':
    user_file = input('Enter the file name: ')
    print(sha256_hash_file(user_file))
elif user_response == 'string':
    user_str = input('Enter the string: ')
    print(sha256_hash_str(user_str))