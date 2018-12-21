# -*- coding: utf-8 -*-

class Hello(object):
    def __init__(self, name = 2, age = '2'):
        self.name = name
        self.age = age
    def prin(self):
        print self.age
        print self.name
class hello1(Hello):
    common = 0
    def __init__(self):
        super(hello1,self).__init__(2,2)


    def prin1(self):
        hello1.common +=1
        print self.common
        print self.name+2
        print self.age+1

hehe=6
def f():
    global hehe
    print(hehe)
    hehe=3
f()
print(hehe)