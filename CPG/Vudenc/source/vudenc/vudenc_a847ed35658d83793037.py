import sys, threading, time
from datetime import datetime
from tkinter import *
print('You need to install: tkinter')
import bane
print('You need to install: bane')
def run(self):...
from tkinter import ttk
sys.exit()
sys.exit()
ti = time.time()
print('=' * 25)
print("""
[*]Target: {}
[*]Date: {}""".format(target.get(), datetime.now().
    strftime('%d/%m/%Y %H:%M:%S')))
crl = [target.get()]
if crawl.get() == 'On':
crl += bane.crawl(target.get(), bypass=True)
pr = proxy.get()
if len(pr) == 0:
pr = None
if method.get() == 'GET':
get = True
if method.get() == 'POST':
post = False
get = False
get = True
fresh = False
post = True
post = True
if refresh.get() == 'On':
fresh = True
ck = None
c = cookie.get()
if len(c) > 0:
ck = c
for x in crl:
if stop == True:
print("""[*]Test was finished at: {}
[*]Duration: {} seconds
""".format(
    datetime.now().strftime('%d/%m/%Y %H:%M:%S'), int(time.time() - ti)))
print('[*]URL: {}'.format(x))
print('=' * 25)
bane.xss(x, payload=payload.get(), proxy=pr, get=get, post=post, user_agent
    =user_agent.get(), fresh=fresh, cookie=ck)
stop = False
def scan():...
sc().start()
def run(self):...
stop = True
def kill():...
ki().start()
main = Tk()
main.title('XSS Sonar')
main.configure(background='light sky blue')
Label(main, text='Target:', background='light sky blue').grid(row=0)
Label(main, text='Cookie: (Optional)', background='light sky blue').grid(row=1)
Label(main, text='Method:', background='light sky blue').grid(row=2)
Label(main, text='Timeout:', background='light sky blue').grid(row=3)
Label(main, text='User-Agent:', background='light sky blue').grid(row=4)
Label(main, text='Payload:', background='light sky blue').grid(row=5)
Label(main, text='HTTP Proxy:', background='light sky blue').grid(row=6)
Label(main, text='Refresh:', background='light sky blue').grid(row=7)
Label(main, text='Crawl', background='light sky blue').grid(row=8)
Label(main, text='', background='light sky blue').grid(row=9)
Label(main, text='', background='light sky blue').grid(row=10)
ua = ['']
ua += bane.ua
li = bane.read_file('xss.txt')
pl = []
for x in li:
pl.append(x.strip())
prox = ['']
prox += bane.http(200)
target = Entry(main)
target.insert(0, 'http://')
cookie = Entry(main)
method = ttk.Combobox(main, values=['GET & POST', 'GET', 'POST'])
timeout = ttk.Combobox(main, values=range(1, 61))
timeout.current(14)
user_agent = ttk.Combobox(main, values=ua)
user_agent.current(1)
payload = ttk.Combobox(main, values=pl)
payload.current(0)
proxy = ttk.Combobox(main, values=prox)
refresh = ttk.Combobox(main, values=['On', 'Off'])
crawl = ttk.Combobox(main, values=['On', 'Off'])
target.grid(row=0, column=1)
target.config(width=30)
cookie.grid(row=1, column=1)
cookie.config(width=30)
method.grid(row=2, column=1)
method.current(0)
method.config(width=30)
timeout.grid(row=3, column=1)
timeout.config(width=30)
user_agent.grid(row=4, column=1)
user_agent.config(width=30)
payload.grid(row=5, column=1)
payload.config(width=30)
proxy.grid(row=6, column=1)
proxy.current(0)
proxy.config(width=30)
refresh.grid(row=7, column=1)
refresh.current(1)
refresh.config(width=30)
crawl.grid(row=8, column=1)
crawl.current(0)
crawl.config(width=30)
Button(main, text='Quit', command=main.destroy).grid(row=11, column=0,
    sticky=W, pady=4)
Button(main, text='Stop', command=kill).grid(row=11, column=2, sticky=W, pady=4
    )
Button(main, text='Scan', command=scan).grid(row=11, column=4, sticky=W, pady=4
    )
Label(main, text=
    """

Coder: Ala Bouali
Github: https://github.com/AlaBouali
E-mail: trap.leader.123@gmail.com

Disclaimer:
This tool is for educational purposes only!!!


"""
    , background='light sky blue').grid(row=12, column=1)
mainloop()
