# def func1():
#     print(x)

# x=10
# func1()
#?로컬-e-글로벌O


# def func1():
#     x=100
#     print(x)

# x=10
# func1()
#?로컬O

# def func1():
#     global x #?앞으로 x는 글로벌로 쓰기
#     x=100 #?글로벌의 x 값을 바꿔준다.
#     print(x)

# x=10
# func1()
#?100출력



# def func1():
#     lst[1] = 500
#     print(lst)

# lst=[1,2,3,4]
# func1()
# print(lst)


# def func1():
#     lst = [4,5,6]
#     print(lst)

# lst=[1,2,3,4]
# func1()
# print(lst)

# x=10
# y=x
# z=20
# print(x,y,z)

# xlst = [1,2,3]
# ylst=xlst #? 리스트의 경우 값이 아니라 id가 넘어간다
# ylst[1]=100
# print(xlst,ylst)
#? x와 y의 값이 모두 바뀐다. (참조 레퍼런스)


