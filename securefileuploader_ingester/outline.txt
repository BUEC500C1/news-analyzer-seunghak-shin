Entity-based

OPERATIONS

- Browse
- Search
- Upload


DATA

For each file: name, size, type, upload date and time


STATUS

Uploading...
Upload successful
Upload failed (reason)

reason (pick one or more): files are too large, invalid file type, database connection error


Stub-APIs

database_connect() => boolean
browse() => list
search(word or phrase) => results
encryption(files) => files_enc, key
upload(files_enc) => boolean
decryption(files_enc, key) => files_dec
