import os


def prepare():
    if not os.path.exists('./logs'):
        os.makedirs('./logs')
    if not os.path.exists('./media'):
        os.makedirs('./media')
