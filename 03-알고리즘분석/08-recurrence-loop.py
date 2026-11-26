# 3장 54쪽 - 반복문이 있는 재귀함수
def FUNCTION(LST):
    if LST == []:
        return

    for x in LST:
        print(x, end=" ")  # PPT의 Do Something

    print()  # 재귀 단계마다 줄바꿈
    FUNCTION(LST[1:])


# 추가 테스트
FUNCTION([1, 2, 3, 4])