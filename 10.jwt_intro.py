import jwt

payload = {"name": "Prasad"}

secret_key = "mysecretkey"

algorithm = "HS256"

my_token = jwt.encode(payload,
                      secret_key, algorithm)
print("My Token:", my_token)
# ('My Token:', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiUHJhc2FkIn0.9Dqyj6KhJhais7XNOnD9wKHnQSooGluXj086IDmq5jc')

decoded_data = jwt.decode(my_token, secret_key)
print('Decoded Data:', decoded_data)
# ('Decoded Data:', {u'name': u'Prasad'})

