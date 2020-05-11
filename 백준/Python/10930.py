import hashlib

inputdata='a'
encodedata=inputdata.encode()
print(encodedata)
result=hashlib.sha256(encodedata).hexdigest()
print(hashlib.sha256(encodedata))
print(result)
