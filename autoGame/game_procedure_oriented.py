import pyautogui
import time
from autoGame import base

#面向过程的写法，结构太乱，全局变量散乱在各处

time.sleep(5)


def findAndClick(pictrue):
    path = "pic/" + pictrue
    for x in range(10): #最多尝试10次，10次都未成功就返回false
        try:
            picPos = pyautogui.locateOnScreen(path)
            c1 = pyautogui.center(picPos)
            pyautogui.moveTo(c1)
            pyautogui.click()
            return True #成功完成
        except TypeError:
            print("not find " + pictrue)
            time.sleep(1)
            continue
    return False    #未完成


def isHavePic(pic):
    path = "pic/" + pic
    for x in range(10): #最多尝试10次，10次都未成功就返回false
        try:
            pyautogui.locateOnScreen(path)
            return True #成功完成
        except TypeError:
            print("not find " + pic)
            time.sleep(1)
            continue
    return False  # 未完成


def handle0():
  r = isHavePic('4sec.PNG')
  if r == False:
      return False
  pyautogui.moveTo(x=399, y=665)
  pyautogui.click()
  time.sleep(1) #sleep 1秒，让页面反应
  return True

def handle1():
    r = findAndClick("begin.PNG")
    if r == False:
        return False
    time.sleep(1) #sleep 1秒，让页面反应
    return True

def handle2():
    r = findAndClick("fight.PNG")
    if r == False:
        return False
    time.sleep(1) #sleep 1秒，让页面反应
    return True

def handle3():
    r = findAndClick("auto.PNG")
    if r == False:
        return False
    time.sleep(45)
    return True

def handle4():
    r = findAndClick("continue.PNG")
    if r == False:
        return False
    time.sleep(1) #sleep 1秒，让页面反应
    return True

#付款页面处理
def handleMoney():
    #如果发现付款图片，就点叉
    #如果发现money图片，并且成功点击叉就返回True，其他情况返回False
    r = isHavePic("money.PNG")
    if r == True:   #发现了money图片
        cr = findAndClick("ca.PNG")
        if cr == True: #成功点击了叉
            time.sleep(1) #sleep 1秒，让页面反应
            return True
    return False

handlers = [handle0, handle1, handle2, handle3, handle4]
stepNum = 0 #指向下一步

#流程断了，从哪里断了就从哪里开始
#不知道处于哪一步，于是挨个试，如果某一步成功，那么handlerIndex就设置为它的下一步（除了handleCa）
def handleUnknow():
    global stepNum
    #这个必须成功，否则就一直循环下去
    while True:
        print("handleUnknow")
        # 看看是不是handleMoney
        r = handleMoney()
        if r == True:
            return

        #不是handleCa， 那就遍历handlers，看看是谁
        for x in range(len(handlers)):
            r = handlers[x]()
            if r == True:   #成功处理了一步
                if x == len(handlers) - 1:  #完成了最后一步，那么stepNum就得指向开头
                    stepNum = 0
                    return
                else:
                    stepNum = x + 1    #完成了第x步，那么stepNum就得指向下一步
                    return

        #没找到，可能游戏卡了，sleep 1分钟再试试
        time.sleep(60)

#总共循环次数
doNum = 0
while True:
    r = handlers[stepNum]()
    if r == False:
        handleUnknow()
        continue
    else:
        if stepNum == len(handlers) - 1: #完成一次
            stepNum = 0
            doNum += 1
            print("finish " + str(doNum))
        else:
            stepNum += 1

    if doNum >= 50:
        print("finish all and exit")
        break

