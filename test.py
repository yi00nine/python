import uuid
import time
import hashlib

uuid_str = uuid.uuid4().hex
signTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
AK = 'super-user'
SK = '59005119-88cf-11e8-8227-90e2ba1fdc4b'
json_body = ''

print(uuid_str,json_body,signTime)

signature = json_body + SK + uuid_str + signTime 
token = hashlib.sha256(bytes(signature, encoding='utf-8')).hexdigest()
# sha256_hash.update(signature.encode('utf-8'))
# sha256_hex = sha256_hash.hexdigest()
print(token)
