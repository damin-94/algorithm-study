# 7장 10쪽 - 개선된 자릿수 접기
def Hash(Key, KeyLength, TableSize):
    i = 0
    HashValue = 0

    # 왼쪽으로 3비트 이동한 후 ASCII 코드값 더하기
    for i in range(KeyLength):
        HashValue = (HashValue << 3) + ord(Key[i])

    # 해시 테이블 크기로 나눈 나머지 반환
    return HashValue % TableSize


# 실행 예제
Key = "Hello"
KeyLength = len(Key)
TableSize = 12289

print("문자열:", Key)
print("HashValue:", Hash(Key, KeyLength, TableSize))