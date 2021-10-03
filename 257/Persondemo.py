import win32com.client
import time

def speak(goalStr):
    # Dispatch("APPs") 需要app 注册COM服务， 且APPs是注册的名字
    speak_out = win32com.client.Dispatch('SAPI.SPVOICE')  #连接到SAPI.SpVoice COM服务
    value = goalStr.split(',')
    for  value_str in value :
        speak_out.Speak(value_str)
        time.sleep(1)

if __name__ == '__main__':
    strValue ="昆明的天气情况如下, 日期: 08月18日(星期二), 天气: 雨, 温度: 20℃, PM2.5: 20, 相对湿度: 92%"
    speak(strValue)