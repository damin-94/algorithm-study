# 8장 32쪽 - KMP 테이블 만들기
def make_kmp_table(pattern):

    m = len(pattern)
    border = [-1] * (m + 1)
    i = 0
    j = -1

    while i < m:
        while j >= 0 and pattern[i] != pattern[j]:
            j = border[j]

        i += 1
        j += 1
        border[i] = j

    return border


# 8장 33쪽 - KMP 문자열 검색
def kmp_search(pattern, border, text):

    m = 0
    i = 0
    t_len = len(text)
    p_len = len(pattern)

    while m + i < t_len:

        # 문자가 일치하는 경우
        if pattern[i] == text[m + i]:
            if i == p_len - 1:
                return m

            i += 1

        # 문자가 일치하지 않는 경우
        else:
            if border[i] > -1:
                m = m + i - border[i]
                i = border[i]

            else:
                i = 0
                m += 1

    return -1


text = "BAABAABAB"
pattern = "BAABAB"

border = make_kmp_table(pattern)

print("Text:", text)
print("Pattern:", pattern)
print("KMP Table:", border)
print("검색 위치:", kmp_search(pattern, border, text))