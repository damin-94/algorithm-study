# 8장 8쪽 - Brute Force Search
def BruteForce(Text, TextSize, Start, Pattern, PatternSize):
    i = 0
    j = 0

    # 검색 시작 위치부터 순차적으로 탐색
    for i in range(Start, TextSize - PatternSize + 1):

        # 패턴의 문자와 본문의 문자를 비교
        for j in range(PatternSize):
            if Text[i + j] != Pattern[j]:
                break
        else:
            # 패턴의 모든 문자가 일치하면 위치 반환
            return i

    # 검색 실패
    return -1


# 8장 5~7쪽 - 실행 예제
Text = "boboycatsoaropt"
Pattern = "soar"

TextSize = len(Text)
PatternSize = len(Pattern)
Start = 0

print("본문:", Text)
print("패턴:", Pattern)
print("검색 위치:", BruteForce(Text, TextSize, Start, Pattern, PatternSize))