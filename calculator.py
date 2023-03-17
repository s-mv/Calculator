#!/usr/bin/env python3

'''
author:      smv
title:       calculator lol
description: literally a calculator
more:        I really like how python still doesn't have multiline comments
             (though this works I guess)
'''

if __name__ != '__main__':
    exit(0)

import readline as rl
from eval import eval, ErrorType

# intro
print('smv\'s calculator')
print('in Python LOL I never use Python')
print('type quit or press ctrl-C to exit')

# set up readline
rl.parse_and_bind('tab: complete')
rl.parse_and_bind('set editing-mode vi')

try:
    # repl
    while True:
        # read
        print('> ', end='')
        expr = input()
        if (expr == 'quit'):
            break
        # eval
        ans = eval(expr)
        # print
        # but first check for errors
        if (type(ans) == ErrorType):
            match ans:
                case ErrorType.SYNTAX: 
                    print('syntax error')                
        else:
            print(ans)
# dirty hack to remove the pesky exit message
# I'm no pro python dev, forgive me if this is bad practice
except (KeyboardInterrupt, EOFError):
    print()
