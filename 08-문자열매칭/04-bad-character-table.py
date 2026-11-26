# 8장 43~47쪽 - Bad Character Table
def buildBCT(pattern):

    # ASCII 문자에 대한 테이블 초기화
    BCT = [-1] * 128
    m = len(pattern)

    # 각 문자의 가장 오른쪽 위치 저장
    for i in range(m):
        BCT[ord(pattern[i])] = i

    return BCT


# 8장 43쪽 - 실행 예제
pattern = "ABAAB"
BCT = buildBCT(pattern)

print("Pattern:", pattern)

print("A:", BCT[ord('A')])
print("B:", BCT[ord('B')])
print("C:", BCT[ord('C')])
print("D:", BCT[ord('D')])