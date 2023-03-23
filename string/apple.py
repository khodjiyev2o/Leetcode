
identity_token = 'eyJraWQiOiJZdXlYb1kiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL2FwcGxlaWQuYXBwbGUuY29tIiwiYXVkIjoiaG9zdC5leHAuRXhwb25lbnQiLCJleHAiOjE2Nzk2MDEwOTksImlhdCI6MTY3OTUxNDY5OSwic3ViIjoiMDAxMDYzLjUzZTc3MDAzNTFmMzQ3MjRiMjRmZWE3MDI0NzgwOTkzLjEzMDgiLCJjX2hhc2giOiJkV1dvY3RRU3hkcnhqTE5odlBoeEZ3IiwiZW1haWwiOiJvY2lvMjhAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOiJ0cnVlIiwiYXV0aF90aW1lIjoxNjc5NTE0Njk5LCJub25jZV9zdXBwb3J0ZWQiOnRydWV9.SEh6mGaMddYU2uE6ArEP-65MmbaT1m4tdsjSDOC62YTmbXcR1SjfgD7XLNBkuBJo6OHMuC2R5HE7lYkgoolQKVjKYflLp0eNWQ_6VzLdY6624QfR5YrrC6cUfJIQrAEzJ7IJc-xtSYXY6RWMAF4wimP4bUt6LhqYi6RMRrZiNEhgx-b4d-vQKQe1mdHTE8BlfibGUY96Th0RAImebWpsvrofvcO2zg4ljjlKHa5enarQEUd4jnGIYWmdwxYmBORyT1PklzEbSSNvRvHS0pbeEjBhynW9vFBGELziX4eCtgk6o41BRdup-ww1hDJ1YXOrNEYcGBMxH53LH2ItJ6XvyQ'
SOCIAL_AUTH_APPLE_PRIVATE_KEY = """
-----BEGIN PRIVATE KEY-----
MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgYz7J19mzInV3SJYf
4p/Wwc0J0vW1VZA65gXaQpLa/ZCgCgYIKoZIzj0DAQehRANCAASzKuKMA6qr26+Z
qtR8Z8ZfxMoD2g/kdMpeQ3LoE7c56p6Q4qw6psS2fQrCe8AIvz4/x3UBx1yqFaMV
TdoDzLzR
-----END PRIVATE KEY-----
"""




import jwt
import requests

issuer = 'https://appleid.apple.com'
user="001063.53e7700351f34724b24fea7024780993.1308"
encoded_token = jwt.decode(identity_token,options={"verify_signature": False})
header = jwt.get_unverified_header(identity_token)
print("Body :", encoded_token)
print("Header :",header)
public_key = header['kid']
apple_keys = requests.get('https://appleid.apple.com/auth/keys').json()
key = ([i['kid'] for i in apple_keys['keys'] if i['kid'] == public_key][0])
print(key)
if key is None:
    print("no key")

allowed_algorithms = ['RS256']

try:
    # Verify the token using the key and allowed algorithms
    decoded_token = jwt.decode(identity_token, key, algorithms=allowed_algorithms, options={"verify_signature": False})
    print('Token verified successfully!')
    print(decoded_token)
    print(decoded_token['sub'] == user and decoded_token['iss'] == 'https://appleid.apple.com')
except jwt.exceptions.InvalidTokenError as e:
    print('Token verification failed.')
    print(e)