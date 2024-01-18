#함수의 클로저

#inner 함수의 개념
# def out_func(nout):
#     def inner_func(nin):
#         return nin * nin
#     return inner_func(nout)
# print(out_func(5))

#closures
def out_func(nout):
    def inner_func():
        return nout * nout
    return inner_func   #함수 이름만 던져주면 된다.

x = out_func(9)
print(type(x))
print(x)
print(x())