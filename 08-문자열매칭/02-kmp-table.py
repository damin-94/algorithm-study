# 8장 32쪽 - KMP 테이블 만들기
def make_kmp_table(pattern):

    m = len(pattern)
    border = [-1] * (m + 1)
    i = 0
    j = -1

    while i < m:

        # 문자가 일치하지 않으면 이전 border 값으로 이동
        while j >= 0 and pattern[i] != pattern[j]:
            j = border[j]

        i += 1
        j += 1

        # 일치하는 prefix의 최대 길이 저장
        border[i] = j

    return border


# 8장 16~20쪽 - 실행 예제
pattern = "BAABABAA"

border = make_kmp_table(pattern)

print("Pattern:", pattern)
print("KMP Table:", border)