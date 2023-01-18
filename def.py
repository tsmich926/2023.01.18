# def function (ham)
#     return ham
#ham은 파라미터


# argument:함수의 파라미터를 통해 전달된다.
# positional argument:자리에 맞게 값이 들어간다.
# def add(x,y):
#     retrun x+y

# Keyword Arguments
# 직접 변수의 이름으로 argu전달
# def add(x,y):
#     retrun x+y
# -add(x=1,y=5)
"""키워드 argument는 positional argument 뒤에 나와야 한다.
add(x=2,5) 불가"""

# Default Argument
# def ad(X,y=0):
#     return x+y

# 호출: add(2)
# add(2,3)도 가능

# local:함수 실행시 함수안쪽에 생성되는 스페이스
# enclosing: 중첩 조건문과 마찬가지로 함수도 중첩가능
# global:프로그램내에서 실행되는 space
# built in:

# Name space:식별자들을 기억하는 공간
# name space가 여러개이면 같은 이름이 있을 수 있다.
# LEGB 네가지 공간에 같은 이름이 있을 수 있다.
# 같은 이름중 어떤 공간에 있는 이름을 가져다 쓸 것인가?-규칙필요 scope적용
# scope:내가 찾고자 하는 변수가 존재하는 프로그램상의 범위

# 변수는 각자의 수명주기 존재
# built in:
# global: 프로그램실행시
# local:함수 호출시 생성 함수 종료시 소멸

def func1():
    print('func1 시작')

    def func2():
        print("func2시작")
        print("func2끝")
        return
    func2()
    return

func1()
