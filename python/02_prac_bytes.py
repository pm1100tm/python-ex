"""
bytes 는 유니코드가 아닌 문자열을 사용하는 것과 유사함.
bytes 는 원시 이진 데이터로 사용되어지거나 1바이트 문자로 고정을 위해 사용되어집니다.
bytes HTTP 응답과 같은 파일과 네트워크 리소스는 바이트 스트림으로 전송되기 때문에 이해하는 것이 중요.
반면에 우리는 유니 코드 문자열의 편의성을 선호하여, 상호변환을 하는 경우가 많다.
"""
# 1. 바이트 사용
# 문자열 앞에 b를 입력
a = b'test'
print(type(a)) # <class 'bytes'>

a = b'test, test, test'
for x in a.split():
    print(type(x)) # <class 'bytes'>


# 2. str -> bytes, bytes -> str
s = 'Vi er så glad for å høre og lære om Python!'
a = s.encode()
print(type(a)) # <class 'bytes'>

a = a.decode()
print(type(a)) # <class 'str'>
