from concurrent.futures import ThreadPoolExecutor

def search_hash_segment(target_hashes, lines):
    found_passwords = {}
    for line in lines:
        try:
            hash_, password = line.strip().split(":")
            if hash_ in target_hashes:
                found_passwords[hash_] = password
        except ValueError:
            continue  # Skip lines that don't fit the format
    return found_passwords  # Return a dictionary of found passwords

def search_hashes(hash_file, target_hashes):
    num_threads = 4  # Define the number of threads
    segment_results = []

    with open(hash_file, 'r') as file:
        lines = file.readlines()  # Read all lines into memory

    lines_per_thread = len(lines) // num_threads  # Determine how to divide the work

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for i in range(num_threads):
            start_index = i * lines_per_thread
            end_index = None if i == num_threads - 1 else (i + 1) * lines_per_thread
            segment = lines[start_index:end_index]
            future = executor.submit(search_hash_segment, target_hashes, segment)
            segment_results.append(future)

    found_passwords = {}
    for future in segment_results:
        found_passwords.update(future.result())

    return found_passwords

# Path to your file with the MD5 hashes and passwords
hash_db_file_path = 'hashed_passwords.txt'
# Path to the file containing MD5 hashes to be searched
md5_hashes_file_path = 'md5_to_search.txt'
# Read the MD5 hashes to search from the file
with open(md5_hashes_file_path, 'r') as file:
    md5_to_search = [line.strip() for line in file.readlines()]

# Call the search_hashes function and provide the file paths and hashes list
found = search_hashes(hash_db_file_path, md5_to_search)

# Output the result
for md5_hash in md5_to_search:
    password = found.get(md5_hash, "Password not found.")
    print(f"The corresponding password for the hash '{md5_hash}' is: {password}")
