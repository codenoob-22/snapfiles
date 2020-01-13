import random
import string
import uuid

def randomString(stringLength=10):
    ''' Generate a random string of fixed len'''
    letters = string.ascii_lowercase + string.ascii_uppercase + "1234567890"
    return ''.join(random.choice(letters) for i in range(stringLength))

# instead of this i used uuid function :=> refer views.py
#  why?- because i wasnt sure that it will always produce unique tokens. 