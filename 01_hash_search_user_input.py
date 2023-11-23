def search_hash(hash_file):
    # Ask the user to input the MD5 hash
    md5_hash = input("Enter the MD5 hash you are looking for: ")

    with open(hash_file, 'r') as f:  # Open the file with the MD5 hashes
        for line in f:  # Read the file line by line
            try:
                hash_, password = line.strip().split(":")  # Split the line into hash and password
                if hash_ == md5_hash:  # Check if the current hash matches the one we're searching for
                    return password  # Return the corresponding password
            except ValueError:
                # Handle the exception if a line is not as expected
                continue
    return "Password not found."  # Return a message if the hash wasn't found

# Usage
hash_file_path = 'hashed_passwords.txt'  # The path to your file with the MD5 hashes and passwords
password = search_hash(hash_file_path)
print(f"The corresponding password for the provided hash is: {password}")
