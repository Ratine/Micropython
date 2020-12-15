#boot.py
from machine import Pin,Timer
import time
led=Pin(2,Pin.OUT)  #2号灯
tim = Timer(1)  #开启计时器1
def blink(t): #定义blink，闪烁
  led.value(not led.value())#反转状态
#初始化，间隔为500ms，模式选为循环,循环函数blink
tim.init(period=500,mode=Timer.PERIODIC, callback=blink)
#time.sleep(5)#5秒后开始连接


import web
web.do_connect()
tim.deinit()#结束闪烁
led.value(1)#关闭灯
