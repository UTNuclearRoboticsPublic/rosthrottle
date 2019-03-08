import threading
from throttle import throttle_messages

if __name__=='__main__':
    intopic = 'chatter'
    outtopic = 'chatter_throttle'
    outtopic2 = 'chatter_throttle_2'
    rate = 1.0
    t1 = threading.Thread(target=throttle_messages, args=[intopic, outtopic, rate])
    t2 = threading.Thread(target=throttle_messages, args=(intopic, outtopic2, rate))