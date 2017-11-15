"""When your scripts start to become very large, you may tend to notice that you are repeating code more often in your scripts.
   You have the ability to create functions inside of your script to help with code reuse"""

import sys

logLevel = int(sys.argv[1])

def logit(level, msg):
    if level >= logLevel:
        print 'MSG' + str(level) + ':', msg

def getUser():
    logit(2, 'Entering Function getUser()...')
    user = raw_input('Enter User Name: ')
    logit(1, 'Leaving Function getUser()...')
    return user

logit(3, 'Starting Script...')
logit(3, 'User Entered: ' + getUser())
logit(3, 'Ending Script.')