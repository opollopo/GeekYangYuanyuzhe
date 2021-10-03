import time
import pyttsx3


class P(object):
    def __init__(self):
        self.birthday = "2021-09-12 10:33:39"
        self.name = "P100000001"


    def eat(self):
        pass

    def speak(self):
        def speak(goalStr):
            engine = pyttsx3.init()   # 初始化
            engine.setProperty('voice', "com.apple.speech.synthesis.voice.sin-ji")  #设置发音人，不过我电脑似乎不起作用
            # engine.setProperty('voice', "com.apple.speech.synthesis.voice.mei-jia")
            rate = engine.getProperty('rate')  # 改变语速  范围为0-200   默认值为200
            engine.setProperty('rate', rate-40)
            engine.setProperty('volume', 0.7)  # 设置音量  范围为0.0-1.0  默认值为1.0
            engine.say(goalStr)   # 预设要朗读的文本数据
            engine.runAndWait()   # 读出声音
        jianjie = "我是%s,我出生在%s"%(self.name, self.birthday)
        jianjie = "123456"
        speak(jianjie)



a = time.strftime("%Y-%m-%d %H:%M:%S")
print(type(a))
p = P()
p.speak()
