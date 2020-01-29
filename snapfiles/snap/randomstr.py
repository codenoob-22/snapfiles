import random
import string
import os
from django.conf import settings

def randomString(stringLength=10):
    ''' Generate a random string of fixed len'''
    letters = string.ascii_letters + string.digits
    token   = ''.join(random.choice(letters) for i in range(stringLength))
    if(os.path.exists(os.path.join(settings.BASE_DIR, token))):
        return randomString()
    return token    

