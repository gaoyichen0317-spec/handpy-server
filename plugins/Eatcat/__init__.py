# Eatcat!!
import random
from mpython import *
from TaoLiSystem.core import utils
from TaoLiSystem.core import sysgui
from TaoLiSystem.core import config

# 变量
notesQueue = 0
dispScore = 0
highScore = 0
touch_threshold = {'P': 400, 'Y': 400, 'T': 400, 'H': 400, 'O': 400, 'N': 400}
choosed = 0
control = 0

# 自定义函数
def draw():
    global notesQueue, dispScore
    oled.fill(0)
    oled.vline(0, 0, 64, 1)
    oled.vline(15, 0, 64, 1)
    oled.vline(31, 0, 64, 1)
    oled.vline(63, 0, 64, 1)
    oled.vline(127, 0, 64, 1)
    oled.fill_rect((((notesQueue[0]) * 16) - 1),15,32,16,1)
    oled.fill_rect((((notesQueue[1]) * 16) - 1),31,32,16,1)
    oled.fill_rect((((notesQueue[2]) * 16) - 1),47,32,16,1)
    oled.fill_rect((((notesQueue[3]) * 16) - 1),63,32,16,1)
    if bool(dispScore):
        oled.text(str(score),52,0) # 显示分数
    oled.show()
def updateQueue():
    global notesQueue
    notesQueue.pop(0)
    notesQueue.append((random.randint(1, 4)))
def getControlKey(RAIL):
    global control
    return eval("touchPad_"+control[RAIL]+".read()") < touch_threshold[control[RAIL]]
def work():
    global touch_threshold
    while not ((touchPad_P.read() < touch_threshold['P'] or (touchPad_Y.read() < touch_threshold['Y'] or (touchPad_T.read() < touch_threshold['T'] or (touchPad_H.read() < touch_threshold['H'] or (touchPad_O.read() < touch_threshold['O'] or touchPad_N.read() < touch_threshold['N'])))))):
        pass
    if touchPad_P.read() < touch_threshold['P']:
        while not ((not (touchPad_P.read() < touch_threshold['P'] or (touchPad_Y.read() < touch_threshold['Y'] or (touchPad_T.read() < touch_threshold['T'] or (touchPad_H.read() < touch_threshold['H'] or (touchPad_O.read() < touch_threshold['O'] or touchPad_N.read() < touch_threshold['N']))))))):
            pass
        return (str("P"))
    elif touchPad_Y.read() < touch_threshold['Y']:
        while not ((not (touchPad_P.read() < touch_threshold['P'] or (touchPad_Y.read() < touch_threshold['Y'] or (touchPad_T.read() < touch_threshold['T'] or (touchPad_H.read() < touch_threshold['H'] or (touchPad_O.read() < touch_threshold['O'] or touchPad_N.read() < touch_threshold['N']))))))):
            pass
        return (str("Y"))
    elif touchPad_T.read() < touch_threshold['T']:
        while not ((not (touchPad_P.read() < touch_threshold['P'] or (touchPad_Y.read() < touch_threshold['Y'] or (touchPad_T.read() < touch_threshold['T'] or (touchPad_H.read() < touch_threshold['H'] or (touchPad_O.read() < touch_threshold['O'] or touchPad_N.read() < touch_threshold['N']))))))):
            pass
        return (str("T"))
    elif touchPad_H.read() < touch_threshold['H']:
        while not ((not (touchPad_P.read() < touch_threshold['P'] or (touchPad_Y.read() < touch_threshold['Y'] or (touchPad_T.read() < touch_threshold['T'] or (touchPad_H.read() < touch_threshold['H'] or (touchPad_O.read() < touch_threshold['O'] or touchPad_N.read() < touch_threshold['N']))))))):
            pass
        return (str("H"))
    elif touchPad_O.read() < touch_threshold['O']:
        while not ((not (touchPad_P.read() < touch_threshold['P'] or (touchPad_Y.read() < touch_threshold['Y'] or (touchPad_T.read() < touch_threshold['T'] or (touchPad_H.read() < touch_threshold['H'] or (touchPad_O.read() < touch_threshold['O'] or touchPad_N.read() < touch_threshold['N']))))))):
            pass
        return (str("O"))
    elif touchPad_N.read() < touch_threshold['N']:
        while not ((not (touchPad_P.read() < touch_threshold['P'] or (touchPad_Y.read() < touch_threshold['Y'] or (touchPad_T.read() < touch_threshold['T'] or (touchPad_H.read() < touch_threshold['H'] or (touchPad_O.read() < touch_threshold['O'] or touchPad_N.read() < touch_threshold['N']))))))):
            pass
        return (str("N"))
    return (str("P"))


# 主程序开始
sysgui.tipBox("别踩黑块", 1)

while True:
    highScore = config.Config.read((str("Eatcat")), (str("score")), 0)
    oled.fill(0)
    oled.DispChar("别踩黑块", 0, (1-1)*16, 1)
    oled.vline(0, 15, 128, 1)
    oled.DispChar((str("最高分") + str(highScore)), 0, (2-1)*16, 1)
    oled.DispChar("<A>开始 <B>退出", 0, (3-1)*16, 1)
    oled.DispChar("[P]设置", 0, (4-1)*16, 1)
    oled.show()
    while not ((button_a.value() == 0 or (button_b.value() == 0 or touchPad_P.read() < touch_threshold['P']))):
        pass
    if button_a.value() == 0:
        while not ((not (button_a.value() == 0 or (button_b.value() == 0 or touchPad_P.read() < touch_threshold['P'])))):
            pass
        notesQueue = (random.randint(1, 4))
        score = 0
        while True:
            draw()
            while not (getControlKey(0) or getControlKey(1) or getControlKey(2) or getControlKey(3)):
                pass
            if (not getControlKey(notesQueue[0] - 1)) or getControlKey(notesQueue[1] - 1) or getControlKey(notesQueue[2] - 1) or getControlKey(notesQueue[3] - 1):
                break
            else:
                updateQueue()
                score += 1
        oled.fill(0)
        oled.DispChar("游戏结束!",0,0,1)
        oled.DispChar("分数:"+str(score),0,16,1)
        oled.DispChar("最高分:"+str(highScore),0,32,1)
        oled.DispChar("<A>好",0,48,1)
        oled.show()
        while not (button_a.value() == 0):
            pass
    elif button_b.value() == 0:
        break
    elif touchPad_P.read() < touch_threshold['P']:
        while not ((not (button_a.value() == 0 or (button_b.value() == 0 or touchPad_P.read() < touch_threshold['P'])))):
            pass
        choosed = 0
        while True:
            choosed = sysgui.itemSelector((str("设置")), [(str("控制方式")),(str((dispScore ? "[√]" : "[×]")+("显示分数"))),(str("清除数据"))], 0)
            if (choosed==None):
                break
            elif (choosed==0):
                control = (str(""))
                oled.fill(0)
                oled.DispChar("触摸1轨的按键", 0, (1-1)*16, 1)
                oled.show()
                control = (str(control) + str(work()))
                oled.fill(0)
                oled.DispChar("触摸2轨的按键", 0, (1-1)*16, 1)
                oled.show()
                control = (str(control) + str(work()))
                oled.fill(0)
                oled.DispChar("触摸3轨的按键", 0, (1-1)*16, 1)
                oled.show()
                control = (str(control) + str(work()))
                oled.fill(0)
                oled.DispChar("触摸4轨的按键", 0, (1-1)*16, 1)
                oled.show()
                control = (str(control) + str(work()))
                sysgui.messageBox((str("控制方式已更改为:") + str(control)), "OK", None, False, None)
            elif (choosed==1):
                dispScore = (not bool(dispScore))
            elif (choosed==2):
                if sysgui.messageBox("确认清除数据?", "是", "否", False, None):
                    config.Config.write("Eatcat", "score", "0")
                    sysgui.tipBox("成功", 1)
