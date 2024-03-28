import os
import sys
import numpy

#homework2 by Liang Yifan
class tne:
    def __init__(self,De='off device',R='stop'):
        self.De=De
        self.R=R
    def Diesel_engine(self,x):
        if x=='on' or x=='on device':
            self.De='on device'
        elif x=='off' or x=='off device':
            self.De = 'off device'
        else:
            print('wrong command')
        print('The Diesel engine now is',self.De)
    def Power_switch(self,x):
        if x=='on' or x=='on device':
            self.De='on device'
        elif x=='off' or x=='off device':
            self.De = 'off device'
        elif x=='check' or x=='check status':
            self.De =self.De
        else:
            print('wrong command')
        print('The Power now is',self.De)
    def Robot(self,x):
        if x=='forward' or x=='f':
            self.R='forward'
        elif x=='rotate' or x=='r':
            self.R='rotate'
        elif x=='stop' or x=='s':
            self.R='stop'
        else:
            print('wrong command')
        print('The Robot now is',self.R)

T=tne()
operation = input("please input the operation (among Diesel engine, Power switch and Robot)\n")
if operation=='Diesel engine' or operation=='De':
    status = input("please input the status (among on device and off device)\n")
    T.Diesel_engine(status)
elif operation=='Power switch' or operation=='Ps':
    status = input("please input the status (among check status, on device and off device)\n")
    T.Power_switch(status)
elif operation=='Robot' or operation=='R':
    status = input("please input the status (among forward, rotate and stop)\n")
    T.Robot(status)
else:
    print('wrong command')

#example
#T.Diesel_engine('on')
#T.Power_switch('check')
#T.Robot('rotate')

