import hashlib
from concurrent.futures import ThreadPoolExecutor
import codecs

def hash_password(password):
    password = password.strip()
    hash_object = hashlib.md5(password.encode())
    return f"{hash_object.hexdigest()}:{password}\n"

def hash_passwords(input_file, output_file):
    with codecs.open(input_file, 'r', encoding='utf-8', errors='replace') as f_in, open(output_file, 'a') as f_out:
        with ThreadPoolExecutor() as executor:
            # Map the hash_password function over the lines of the input file
            results = executor.map(hash_password, f_in)
            # Write the results to the output file
            f_out.writelines(results)

# Usage
hash_passwords('large_password_file.txt', 'hashed_passwords.txt')
