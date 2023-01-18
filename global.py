x = '글로벌'

def func1():
    x = '인클로징'
    def func2(a,b):
        x = '로컬'
        print(X)
        print(locals())
        print(globals())
    func2(2,3)

func1()