import os
import sys
import numpy

#homework1 by Liang Yifan
def appli(num,lan):
    for i in range(0,num):
        if (lan=="English")or(lan=="english"):
            print("hello")
        elif (lan=="Chinese")or(lan=="chinese"):
            print("ni hao")
        elif (lan=="Russian")or(lan=="russian"):
            print("privet")
        else:
            print("Language wrong!")
            break

language = input("please input the Language (among English, Chinese and Russian)\n")
number = int(input("please input the output times\n"))
appli(number,language)
#appli(2,chinese) as example