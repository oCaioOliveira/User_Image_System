import pytest
from contextlib import closing

from random import randint, SystemRandom
from string import ascii_letters, digits
from base64 import b64encode

ids = list(range(0,randint(50,500)))
images = [b64encode(bytes(''.join(SystemRandom().choice(ascii_letters + digits) for _ in range(randint(500,5000))), 'utf-8'))] * len(ids)


print(len(images), len(ids))
print(images[0], ids[0])