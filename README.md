

This Tool is generated for hash all leaked password or dictionary files into a file with hash and password.

So when we enter the hash it will show password in very fast.

Features:

1. Search a single md5 hash: 
   
   Python3 01_hash_search_user_input.py <MD5 Hash>

2. Search Bulk Hash and display in Windows:
  
   Need to store all hashes need to search in md5_to_search.txt

   Then you run python3 02_bulk_hash_search.py

3. Search Bulk Hash and display in Windows and store in a file:

   Need to store all hashes need to search in md5_to_search.txt

   Then you run python3 03_bulk_hash_search_store_in_file.py
  
   So it will display the matched plain text and store in found_passwords.txt

4. Create MD5 Hash file from plaintext
   
   Store the text file in large_password_file.txt

   Run python3 04_hash_create.py

5. Create MD5 Hash file from plaintext and append the hash:
   
   Store the text file in large_password_file.txt

   Run python3 05_hash_create_with_append.py


Creator:
Sabareesh VK
Penetration tester