# Just practising Python, I have surely lost the link...

print "calculator\nOperators:\nMultiply ( * )\nDivide ( / )\nAdd ( + )\nSubtract ( - )\nRemainder ( % )\nPower( ** )"
print "to  get a full list, type getentirelist() [not working yet]"
print "to enter GUI mode type enterUIMode() [not working yet, requires Kivy]"
print "\n\ninput"

def getEntireList():
    print "function not ready yet"

def enterUIMode():
    print "Entering..."
    from Kivy import App


while True:
    x = raw_input(":")
    try:
        print eval (x)
    except Exception as e:
        print "'{}' gave error ({}), try something else".format(x, e)
    else:
        pass
    finally:
        print "\n"
