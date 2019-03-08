import subprocess 
import time
import signal

def throttle_messages(intopic, outtopic, rate, wall_clock=False, unreliable=False, lazy=False):
    command = ['rosrun', 'topic_tools', 'throttle', 'messages', intopic, str(rate), outtopic]
    runner = subprocess.Popen(command)
    print('Running on: %d'%runner.pid)
    print('Waiting 5 seconds...')
    time.sleep(5)
    print('Killing runner...')
    runner.send_signal(signal.SIGINT) 
    runner.wait()
    print('Return code: ' + str(runner.returncode))