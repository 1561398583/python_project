import pyautogui
import time

#获取当前鼠标坐标
#time.sleep(5)
#pos = pyautogui.position()
#print(pos)

#获取图片坐标
#picPos = pyautogui.locateOnScreen("a.png")
#picPos中间坐标
#c1 = pyautogui.center(picPos)

#鼠标移动到c1
#pyautogui.moveTo(c1)
#点击
#pyautogui.click()



class AutoPlay:
    """"
    segPic:第几章的图片
    secX, secY: 找到segPic之后点击哪里
    fightTime:每次战斗时间（秒）
    fightNum:战斗次数
    """
    def __init__(self, secPic, secX, secY, fightTime, fightNum):
        self.handlers = [self.handle0, self.handle1, self.handle2, self.handle3, self.handle4]
        self.secPic = secPic
        self.fightTime = fightTime
        self.fightNum = fightNum
        self.secX = secX
        self.secY = secY
        self.stepIndex = 0  # 指向下一步

    def run(self):
        finishFightNum = 0
        while True:
            r = self.handlers[self.stepIndex]()
            if not r:   #r==false,说明这一步失败了
                self.handleUnknow()
                continue
            else:   #这一步成功完成
                if self.stepIndex == len(self.handlers) - 1:  # 完成了最后一步，于是从头开始
                    self.stepIndex = 0
                    finishFightNum += 1  #完整的战斗次数加1
                    print("finish " + str(finishFightNum))
                else:   # 完成了中间某一步，于是指向下一步
                    self.stepIndex += 1

            if finishFightNum >= self.fightNum:     #战斗次数已完成？
                print("finish all and exit")
                break   #跳出循环，结束


    #在屏幕中找到并点击图片，成功返回True，失败返回False
    def findAndClick(self, pictrue):
        path = "pic/" + pictrue
        for x in range(10):  # 最多尝试10次，10次都未成功就返回false
            loc = pyautogui.locateOnScreen(path)
            if loc is None:  # 在屏幕中未找到图片
                print("not find " + pictrue)
                time.sleep(1)
                continue
            #找到之后，鼠标移至图片中间，点击
            c1 = pyautogui.center(loc)
            pyautogui.moveTo(c1)
            pyautogui.click()
            return True  # 成功完成

        return False  # 未完成


    # 在屏幕中找到图片，成功返回True，失败返回False
    def isHavePic(self, pic):
        path = "pic/" + pic
        for x in range(10):  # 最多尝试10次，10次都未成功就返回false
            loc = pyautogui.locateOnScreen(path)
            if loc is None: #在屏幕中未找到图片
                print("not find " + pic)
                time.sleep(1)
                continue
            return True  # 成功完成
        return False  # 未完成

    def handle0(self):
        r = self.isHavePic(self.secPic)
        if r == False:
            return False
        pyautogui.moveTo(x=self.secX, y=self.secY)
        pyautogui.click()
        time.sleep(1)  # sleep 1秒，让页面反应
        return True

    def handle1(self):
        r = self.findAndClick("begin.PNG")
        if r == False:
            return False
        time.sleep(1)  # sleep 1秒，让页面反应
        return True

    def handle2(self):
        r = self.findAndClick("fight.PNG")
        if r == False:
            return False
        time.sleep(1)  # sleep 1秒，让页面反应
        return True

    def handle3(self):
        r = self.findAndClick("auto.PNG")
        if r == False:
            return False
        time.sleep(45)
        return True

    def handle4(self):
        r = self.findAndClick("continue.PNG")
        if r == False:
            return False
        time.sleep(1)  # sleep 1秒，让页面反应
        return True

    # 付款页面处理
    def handleMoney(self):
        # 如果发现付款图片，就点叉
        # 如果发现money图片，并且成功点击叉就返回True，其他情况返回False
        r = self.isHavePic("money.PNG")
        if r == True:  # 发现了money图片
            cr = self.findAndClick("ca.PNG")
            if cr == True:  # 成功点击了叉
                time.sleep(1)  # sleep 1秒，让页面反应
                return True
        return False

    # 流程断了，从哪里断了就从哪里开始
    # 不知道处于哪一步，于是挨个试，如果某一步成功，那么handlerIndex就设置为它的下一步（除了handleMoney）
    def handleUnknow(self):
        # 这个必须成功，否则就一直循环下去
        while True:
            print("handleUnknow")
            # 看看是不是handleMoney
            r = self.handleMoney()
            if r == True:
                return

            # 不是handleMoney， 那就遍历handlers，看看是谁
            for x in range(len(self.handlers)):
                r = self.handlers[x]()
                if r == True:  # 成功处理了一步
                    if x == len(self.handlers) - 1:  # 完成了最后一步，那么stepIndex就得指向开头
                        self.stepIndex = 0
                        return
                    else:
                        self.stepIndex = x + 1  # 完成了第x步，那么stepIndex就得指向下一步
                        return

            # 没找到，可能游戏卡了，sleep 1分钟再试试
            time.sleep(60)