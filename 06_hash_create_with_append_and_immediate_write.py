import hashlib
from concurrent.futures import ThreadPoolExecutor

def hash_password(password):
    password = password.strip()
    hash_object = hashlib.md5(password.encode())
    return f"{hash_object.hexdigest()}:{password}\n"

def hash_passwords(input_file, output_file):
    with open(input_file, 'rb') as f_in, open(output_file, 'a') as f_out:
        counter = 0
        hashes = []
        with ThreadPoolExecutor() as executor:
            for line in f_in:
                try:
                    password = line.decode('utf-8').strip()
                except UnicodeDecodeError:
                    password = line.decode('utf-8', errors='replace').strip()
                result = hash_password(password)
                hashes.append(result)
                counter += 1
                if counter == 100:
                    f_out.writelines(hashes)
                    counter = 0
                    hashes = []
                    f_out.flush()  # flush the buffer to ensure immediate write
            # Write the remaining hashes to the output file
            f_out.writelines(hashes)
            f_out.flush()  # flush the buffer to ensure immediate write

# Usage
hash_passwords('large_password_file.txt', 'hashed_passwords.txt')
