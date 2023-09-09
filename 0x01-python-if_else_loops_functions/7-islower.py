#!/usr/bin/python3
# Author-Omar Hady

def islower(c):
    """Function checks lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
