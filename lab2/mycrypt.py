import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    s = s.ljust(1000, 'a')
    
    for c in s:
         if c.lower() in ["+", "å", "ä", "ö"]:
            raise ValueError
    for c in s:
        if c.isalpha():
            if c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            elif c.isupper():
                 c=c.lower()
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
          crypted+=digitmapping[c]

        
    return crypted[:origlen]

def decode(s):
   # if not isinstance(s,str):
    #   raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('!"#€%&/()=1234567890','1234567890!"#€%&/()='))
   # if len(s) > 1000:
    #    raise ValueError
    s = s.ljust(1000, 'a')
   # for c in s:
        # if c.lower() in ["+", "å", "ä", "ö"]:
         #    raise ValueError
    for c in s:
        if c.isalpha():
            if c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            elif c.isupper():
                 c=c.lower()
            crypted+=codecs.decode(c,'rot13')
        elif c in digitmapping:
          crypted+=digitmapping[c]

    return crypted[:origlen]
