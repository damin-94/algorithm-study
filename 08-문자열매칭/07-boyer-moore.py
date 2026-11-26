# Bad Character Table
def buildBCT(pattern):
    BCT = [-1] * 128
    m = len(pattern)

    for i in range(m):
        BCT[ord(pattern[i])] = i

    return BCT


# Suffix Table
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
    GST = [m] * m
    j = 0

    # Case 1: 접두-접미 완전 일치
    for i in range(m - 1, -1, -1):
        if suffix[i] == i + 1:
            while j < m - 1 - i:
                if GST[j] == m:
                    GST[j] = m - 1 - i
                j += 1

    # Case 2: 접미-접미 일치
    for i in range(m - 1):
        GST[m - 1 - suffix[i]] = m - 1 - i

    return GST


# 8장 80~93쪽 - Boyer-Moore 문자열 검색
def boyer_moore_search(pattern, text):
    m = len(pattern)
    n = len(text)

    if m == 0:
        return 0

    BCT = buildBCT(pattern)
    suffix = buildSuffix(pattern)
    GST = buildGST(pattern, suffix)

    i = 0

    while i <= n - m:
        j = m - 1

        # 오른쪽에서 왼쪽으로 비교
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        # 모든 문자가 일치하는 경우
        if j < 0:
            return i

        # Bad Character Shift
        bad = j - BCT[ord(text[i + j])]

        # Good Suffix Shift
        good = GST[j]

        # 두 이동 거리 중 큰 값 선택
        i += max(good, bad)

    return -1


# 8장 90~91쪽 - 실행 예제
text = "BABCDEACDEAA"
pattern = "ABCDE"

print("Text:", text)
print("Pattern:", pattern)
print("검색 위치:", boyer_moore_search(pattern, text))