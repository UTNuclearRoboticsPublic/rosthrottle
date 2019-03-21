from rosthrottle import MessageThrottle

import time

if __name__=='__main__':
    intopic = 'chatter'
    outtopic = 'chatter_throttle'
    rate = 1.0
    t = MessageThrottle(intopic, outtopic, rate)
    pid = t.start()
    time.sleep(10)
    t.stop()
