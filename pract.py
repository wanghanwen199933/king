# def func(name):
#     dic = {}
#     def bite():
#         print(dic['name'])
#     dic['bite'] = bite
#     dic['name'] = name
#     return dic
#
# inn1 = func('alex')
# inn2 = func('egon')
# inn1['bite']()
# inn2['bite']()


#
# class Person:    # 类
#     COUNTRY = '牧师'       # 静态属性\类属性 属于类的 所有属于这个类的对象都共同的属性
#     def __init__(self,name,sex,hp,mp,ad):
#         self.name = name   # 属性 属于对象的值 - 对象属性
#         self.sex = sex
#         self.hp = hp
#         self.mp = mp
#         self.ad = ad
#     def attack(self):
#         print('%s发起了攻击'%self.name)
# class Dog:
#     def __init__(self,name,kind,hp,ad):
#         self.name = name
#         self.kind = kind
#         self.hp = hp
#         self.ad = ad
#
# # 实例化一些对象
# alex = Person('alex',None,10,10,0.1)
# haha = Dog('haha','金毛',9999,998)
# # 扩展\了解的知识点
# print(alex.__dict__)
# alex.__dict__['name'] = 'alex_sb'
# print(alex.name)




#
# class A:
#     def func(self):print('A')
#
# class B(A):
#     def func(self):
#         super().func()
#         print('B')

# class C(A):
#     def func(self):
#         super().func()
#         print('C')
#
# class D(B,C):
#     def func(self):
#         super().func()
#         print('D')

# b = D()
# b.func()
# d = D()
# d.func()


# class Dog:
    # dog_sum = 0         # 不安全,因为这个属性可以在类的外部被随便修改
    # __dog_sum = 0         # 安全,通过dog_sum方法和__变量名让属性变成只能看不能改的值
    # def __init__(self):
        # self.count()
    # def count(self):
        # Dog.__dog_sum += 1 # 可以从一个类的内部使用__dog_sum的属性
    # def dog_sum(self):
        # return Dog.__dog_sum

# print(Dog.__dict__)
# alex = Dog()
# print(Dog.__dict__)
# print(Dog.__dog_sum)    # 不可以从外部直接使用这个变量
# print(alex.dog_sum())






# print( i % 2 for i in range(10) )

'''如何实现 “1,2,3” 变成 [‘1’,’2’,’3’]'''

# str = "1,2,3"
# str_re = str.replace(",","")
# print(list(str_re))
#
# a = str.split(",")
# print(a)
# list1=[]
# list = ['1','2','3']
# for i in list:
    # print(i)
    # list1.append(int(i))
# print(list1)

# b = [int(i) for i in list]
# print(b)
#
# '''45. 如何用一行代码生成[1,4,9,16,25,36,49,64,81,100] ? '''
# print([ i**2 for i in range(1,11)])


# print([lambda i:i**2 for i in range(11)])

# '''一个列表A=[2，3，4]，Python如何将其转换成B=[(2,3),(3,4),(4,2)]？'''
# B = zip(A, A[1:]+A[:1])

# A=[2,3,4]
# print(A[:2])

# a = [1,2,1,2,3,4,5,6,6]
# print(list(set(a)))


# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # print(len(li))
#
# def search(a, li):
#     length = int(len(li) / 2)
#     if length == a:
#
#
# search(3, li)
'''
"223456"
2   22  23  4 5 6
2 2 3 4 5 6
2 23 4 5 6
22 3 4 5 6
'''
'''
def search(l,aim,start=0,end=None):
    if not end:end = len(l)-1
    if  start<=end:
        mid = start + (end-start)//2   # 12                  5
        print(mid)
        mid_value = l[mid]             # l[12] = 41          l[18] = 67
        if aim > mid_value:            # 67 > 41
            start = mid+1              # 13
            ret = search(l,aim,start,end)    # search(l,aim,13,24)
            return ret
        elif aim < mid_value:          # 16 < 41
            end = mid-1                # end = 12-1=11
            ret = search(l,aim,start,end)    # search(l,aim,0,11)
            return ret
        else:                                                # 16 = 16
            return mid                                       # return 16
    else:# 找不到的情况
        pass
l = [15,72,76,82,83,88]   # 44/46
ret = search(l,15)
print(ret)

'''

# def search(l,aim,start=0,end=None):
#     if  not end:end = len(l)-1
#     if start <= end:
#         mid = start + (end-start)//2
#         mid_value = l[mid]
#         if  aim > mid_value:
#             start = mid + 1
#             ret = search(l,aim,start,end)
#             return ret
#         elif aim < mid_value:
#             end = mid - 1
#             ret = search(l,aim,start,end)
#             return ret
#         else:
#             return mid
#     else:
#         return "找不到情况"
# l = [22,33,44,55,66,77,88,99]
# aa=search(l,88)
# print(aa)


# def foo():
#     m = 3
#     n = 4
#     def inner():
#         ret = m + n
#         return ret
#     return inner
# aa = foo()
# ret = inner()

# def foo():
#     m = 3
#     n = 5
#     def bar():
#         a = 4
#         return m + n + a
#     return bar
#
# bar = foo()
# print(bar())


# def mapfunc(x):
#     return x*x
# n = [1,2,3,4]
# # ret = list(map(mapfunc,n))
# ret = map(mapfunc,n)
# for i in ret:
#     print(i)

# a = 2
# print(isinstance(a,int))

# class A:
#     pass
#
# class B(A):
#     pass
#
# print("isinstance",isinstance(A(),A))   # isinstance True
# print("type",type(A())  == A)    # type True
#
# print('isinstance',isinstance(B(),A) )   # isinstance True
# print('type',type(B()) == A)

# a = 'asd'
# ret = "0".join(a)
# print(ret)

# print('\n'.join([' '.join(["%2s *%2s=%2s"%(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))

# print(["/n".join ([ ' '.join('%s*%s=%s'% (j,i,j*i))  for j in range(1,i+1)]) for i in range(1,10)])

# print("\n".join([' '.join([ '%s* %s=%s'%(j,i,j*i) for j in range(1,i+1)]) for i in range(1,10)]))



# print([i for i in range(1,10)])


# '''一个列表A=[2，3，4]，Python如何将其转换成B=[(2,3),(3,4),(4,2)]'''
# A=[2,3,4]
# print(list(zip(A,A[1:]+A[:1])))
# print(type(A[:1]))
# print(type(A[1]))

# a = [1,2,3,4,5,6,7,8]
# b= [4,5,6]
# print(a[-1:-2])

#
# x=2
# def func():
#     global x
#     x = 1
#     return x
# func()
# 1,2,3,4,5
'''
def func(n,aim,start=0,end=None):
   if not end: end = len(n)-1
   if start <=end:
       mid = start+(end-start)//2
       midva = n[mid]
       if aim < midva:
           end = mid+1
           return func(n,aim,start,end)
       elif aim > midva:
           start =mid -1
           return func(n,aim,start,end)
       else:
           return mid
   else:
       return "情况不存在"

n = [11,22,33,44,55,66,77,88,99]
ret = func(n,33)
print(ret)
'''
#
# def func1():
#     s = 1
#     def inner():
#         return(s+1)
#     return inner
# inn = func1()
# print(inn)
# print(inn())
# print(ret)
# inner()
# import random
# print(random.randint(1,10))

# print(random.random())
'''
继承:将多个类的共同方法和属性封装到一个父类下面,然后在用这些类来继承这个父类的属性和方法
封装:   将有共同的属性和方法封装在同一个类下面
        第一层面:创建类和对象会分别创建二者的名称空间,我么只能用类名,或者obj的方式去访问里面的名字这本身就是一种封装
多态:python处处存在多态,天生支持多态,指的是基类的同一个方法在不同的派生类中有着不同的功能

'''

'''经典类  新式类
'''
# import itertools
# print(len(list(itertools.permutations('12345',3))))

class A:
    def func(self):print('A')

class B(A):
    def func(self):
        super().func()
        print('B')

class C(A):
    def func(self):
        super().func()
        print('C')

class D(B,C):
    def func(self):
        super().func()
        print('D')
# d = D()
print(D.__mro__)
# print(__mro__(D))













































