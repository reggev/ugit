import hashlib
import os

GIT_DIR = '.ugit'


def init():
    os.makedirs(GIT_DIR, exist_ok=True)
    os.makedirs(f'{GIT_DIR}/objects', exist_ok=True)


def hash_object(data):
    oid = hashlib.sha1(data).hexdigest()
    with open(f'{GIT_DIR}/objects/{oid}', 'wb') as out:
        out.write(data)
    return oid


def get_object(oid):
    with open(f'{GIT_DIR}/objects/{oid}', 'rb') as f:
        return f.read()
