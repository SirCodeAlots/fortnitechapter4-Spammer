import webbrowser
import sys
import random
import time


final = [""]
count= 1

while count < 10:
    for x in range(4):
        randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
        numb=(random.randint(0,9))
        final.append(numb)
        final.append(randomUpperLetter)
        
        print (final)
        
    s = ''.join(str(x) for x in final)
    print(s)


    
    link = "https://www.fortnitechapter4.com/" + s + "/"
    webbrowser.open_new(link)
    
    count += 1
    final.clear()
time.sleep(100)
print("Done")