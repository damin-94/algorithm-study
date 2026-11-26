# 7장 9쪽 - 자릿수 접기(Digits Folding)
def Hash(Key, KeyLength, TableSize):
    i = 0
    HashValue = 0

    # 각 문자의 ASCII 코드값을 더함
    for i in range(KeyLength):
        HashValue += ord(Key[i])

    # 해시 테이블 크기로 나눈 나머지 반환
    return HashValue % TableSize


# 7장 9쪽 - 실행 예제
Key = "Hello"
KeyLength = len(Key)
TableSize = 12289

print("문자열:", Key)
print("ASCII 코드:", [ord(c) for c in Key])
print("HashValue:", Hash(Key, KeyLength, TableSize))