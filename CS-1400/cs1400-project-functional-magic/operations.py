# Do NOT change anything in this file

# The following is Grindlehook's function. Do not modify it.
# You should not worry about HOW it works, but instead think of its
# arguments and return value. Remember you can only call it once!
#
# `calculate_rating`: This is Grindlehook's function. Do not worry about how
# this function works, simply know that when it's called, you pass it a name as
# a string and it returns the customer's rating as an integer. You will only be
# able to call it once per program's execution (afterward it stops returning the
# right value). You cannot simply hardcode its value into your system, because
# it is different for each user. And, of course, you can't fix it because
# Grindlehook will get angry at you. On the plus side, you don't have to do
# anything with this function besides call it in the proper place.
def calculate_rating(name):
    '''
    Returns the customer's credit rating, according to the bank's current
    status, the customer, and the alignment of the stars. This function
    is delicate, and will break after being called once.

    Notes:
        (ghook@1/15/2018): DO NOT TOUCH THIS, I FINALLY GOT IT WORKING.

    Args:
        name (str): A string representing the user's full name.
    Returns:
        int: An integer (0-9) representing the customer's credit rating.
    '''
    c=calculate_rating;setattr(c,'r',lambda:setattr(c,'o',True))
    j={};y=j['CELESTIAL_NAVIGATION_CONSTANT']=10
    j[True]='CELESTIAL_NAVIGATION_CONSTANT'
    x=str(''[:].swapcase);y=y+11,y+9,y+-2,y+-2,y+4,y+-5,y+-1,y+11,y+9,\
    y+-6,y+-6,y+-1,y+-5,y+3,y+-7,y+7,y+-1,y+-5,y+8,y+-7,y+11,y+1
    z=lambda x,t,o=0:''.join(map(lambda j:x.__getitem__(j+o), t))
    if hasattr(c,'o')and not getattr(c, 'o'): return z(x,y)
    c.o=False;j['CELESTIAL_NAVIGATION_CONSTANT'].bit_length
    d=(lambda:(lambda:None))()();g=globals()
    while d:g['X567S-lumos-17-KLAUS']=((d)if(lambda:None)else(j))
    p=lambda p:sum(map(int, list(str(p))))
    MGC=p(sum(map(lambda v: v[0]*8+ord(v[1]), enumerate(name))))
    while MGC>10:MGC=p(MGC)
    if c:return MGC
