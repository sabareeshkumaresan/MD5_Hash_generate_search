import hashlib
from concurrent.futures import ThreadPoolExecutor

def hash_password(password):
    password = password.strip()
    hash_object = hashlib.md5(password.encode())
    return f"{hash_object.hexdigest()}:{password}\n"

def hash_passwords(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        with ThreadPoolExecutor() as executor:
            # Map the hash_password function over the lines of the input file
            results = executor.map(hash_password, f_in)
            # Write the results to the output file
            f_out.writelines(results)

# Usage
hash_passwords('large_password_file.txt', 'hashed_passwords.txt')
