import random
import string


def randomString(stringLength=10):
    ''' Generate a random string of fixed len'''
    letters = string.ascii_lowercase + string.ascii_uppercase + "1234567890"
    return ''.join(random.choice(letters) for i in range(stringLength))
 