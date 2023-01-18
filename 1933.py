
#?정수 N의 약수 구해서 오름차순으로 출력
#?정수 하나를 받고,약수가 입력된 list와 합을 리턴해주는 함수
# N= int(input())

#x=1을 넣으면 약수에 1이 디폴트
def getDiv(N,x=1):
    lst = [x]
    for i in range(1,N):
        if N % i == 0:
            lst.append(i)
    return lst

# print(getDiv(10))

for i in range(15,21):
    print(getDiv(i,1)) #? 15부터 20까지의 약수출력

# getDiv(N=100,x=10) #이름을 붙여주면 순서를 바꿔도 괜찮음,벗 디버깅어려움

# N= int(input())
# lst=[]
# for i in range(N):
#     if N % i ==0:
#         lst.append(i)
# print(lst)

def getDiv(N,sumV):
    lst = [x]
    for i in range(1,N):
        if N % i == 0:
            lst.append(i)
    
    #리스트를 받아서 리스트의 값들의 합을 리턴
    def mysum(lst,sumV):
        #global sumV
        for value in lst:
            sumV += value
        return sumV

    ret = mysum(lst,sumV)
    print(sumV)
    return lst,ret

sumV = 0
for i in range(15,21):
    print(getDiv(i,sumV))

