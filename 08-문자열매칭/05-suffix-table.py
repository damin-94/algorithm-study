# 8장 54~67쪽 - Suffix Table 만들기
def buildSuffix(pattern):

    m = len(pattern)
    suffix = [0] * m

    for i in range(m):
        j = i
        k = m - 1

        # 오른쪽에서 왼쪽으로 문자 비교
        while j >= 0 and pattern[j] == pattern[k]:
            suffix[i] += 1
            j -= 1
            k -= 1

    return suffix


# 8장 67쪽 - 실행 예제
pattern = "GCAGAGAG"

suffix = buildSuffix(pattern)

print("Pattern:", pattern)
print("Suffix Table:", suffix)