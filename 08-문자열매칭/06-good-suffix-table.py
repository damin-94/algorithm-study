# 8장 54~67쪽 - Suffix Table
def buildSuffix(pattern):

    m = len(pattern)
    suffix = [0] * m

    for i in range(m):
        j = i
        k = m - 1

        while j >= 0 and pattern[j] == pattern[k]:
            suffix[i] += 1
            j -= 1
            k -= 1

    return suffix


# 8장 75쪽 - Good Suffix Table
def buildGST(pattern, suffix):

    m = len(pattern)
    GST = [0] * m

    # 초기값 설정
    for i in range(0, m, 1):
        GST[i] = m

    # Case 1: 접두-접미 완전 일치
    j = 0

    for i in range(m - 1, -1, -1):
        if suffix[i] == i + 1:
            while j < m - 1 - i:
                if GST[j] == m:
                    GST[j] = m - 1 - i

                j += 1

    # Case 2: 접미-접미 일치
    for i in range(0, m - 1, 1):
        GST[m - 1 - suffix[i]] = m - 1 - i

    return GST


# 8장 76~79쪽 - 실행 예제
pattern = "GCAGAGAG"

suffix = buildSuffix(pattern)
GST = buildGST(pattern, suffix)

print("Pattern:", pattern)
print("Suffix Table:", suffix)
print("Good Suffix Table:", GST)