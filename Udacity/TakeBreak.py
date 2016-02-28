import webbrowser
import time

total_breaks = 3
break_count = 0

print('Your break time started: ' +time.ctime())
while(break_count < total_breaks):
    time.sleep(7) # in seconds # for 2 hrs use (2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=G94G0Gxh1cU")
    break_count = break_count + 1


