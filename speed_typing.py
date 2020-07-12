#coding: utf-8








"""
MAU APA BRO? NYONTEK YA?
ATO MAU RECODE?

KASIAN YA JADI KAMU BISANYA NYONTEK IDE / KODE ORANG


BELAJAR LAGI CODING YA BROO WKWKWKWK



KALO EMANG GA MAMPU YA JANGAN RECODE
SINI GW AJARIN KALO GA MAMPU

WA : 0896 8200 9902



"""







from __future__ import division
import curses,time,random
text = random.choice(open("word_list.txt").read().splitlines())
c = curses.initscr()
curses.cbreak(1)
c.refresh()
maxlen = len(text)-1
asu = 0
userinput = []
miss = 0

def calculate(text,miss):
    if miss == 0:
       return 100.0
    else:
       return 100 - ((miss * 100) / text)

c.addstr(0,0,"Write text above you\nReady? Press any key to start")
c.refresh()
inpud = c.getch()


start_time = time.time()
while maxlen >= asu:
   c.addstr(0,0,"\r"+text+"\n\nInput : "+"".join(userinput))
   c.keypad(1)
   c.refresh()
   c.refresh()
   inpud = c.getch()
   if chr(inpud) == text[asu]:
      userinput.append(chr(inpud))
      asu -=-1
   else:
      miss += 1
   c.addstr(0,0,"\r"+text+"\n\nInput : "+"".join(userinput))
   c.refresh()

end_time = time.time()
c.addstr(0,0,"Text : {}\nTime : {}\nAccuracy : {} %\nMiss : {}\nSpeed : {} Huruf/s\n\nPress anything to exit...".format(text,(end_time - start_time),calculate(len(text),miss),miss,int(len(text) / (end_time - start_time))))
c.refresh()
c.getch()
curses.endwin()
