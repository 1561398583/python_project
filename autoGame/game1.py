from autoGame import base
import time

time.sleep(5)

autoPlay = base.AutoPlay(secPic='4sec.PNG',secX=252, secY=437, fightTime=50, fightNum=100)
autoPlay.run()