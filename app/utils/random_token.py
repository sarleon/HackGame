import random

#generate random token to specific identity
def random_token(length=16,seed_conf=6):
    seeds=[
        '0123456789',
        'abcdefghijklmnopqrstuvwxyz',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        '+-_*$#=',
        'abcdefghijklmnopqrstuvwxyz0123456789',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-_*$#='
    ]

    seed=seeds[seed_conf]
    seed_length=len(seed)
    token=""
    for i in range(length):
        token+=seed[random.randint(0,seed_length-1)]
    print "token"+token
    return token


