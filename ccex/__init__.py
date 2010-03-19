"""
A program to taunt
"""

def taunter(prompt='>>>'):
    name = raw_input('>>>')
    print "I know you are a %s... but what am I?" %name

if __name__ == "__main__":
    taunter()
