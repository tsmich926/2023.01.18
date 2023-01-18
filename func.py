# my_list=[1,2,3,4]

# def func1():
#     my_list=[5,6,7]
#     # my_list[1]=5554

# func1()
# print(my_list)


# def func1():
#     x=2
    
#     def func2():
#         nonlocal x
        
#         x=20

#     func2()
#     print(x)

# func1()
# print(X)


#함수내에서 필요한 상위scope변수는 argument로 넘기기
x=1
y=2

def a():
    global x
