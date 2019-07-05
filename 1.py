import json
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

null = None
true = True
false = False

def recursive_print(src, dpth = 0, key = ''):
    """ Recursively prints nested elements."""
    tabs = lambda n: ' ' * n * 4 # or 2 or 8 or...

    if isinstance(src, dict):
        for key, value in src.items():
            print(tabs(dpth) + key)
            recursive_print(value, dpth + 1, key)
    elif isinstance(src, list):
        k = ''
        for litem in src:
            recursive_print(litem, dpth + 2)
        print()
    else:
        if key:
            # print(tabs(dpth) + '%s = %s' % (key, src.__class__.__name__))
            # print(tabs(dpth) + '%s: %s, depth: %s' % (key, src.__class__.__name__, dpth))
             print(tabs(dpth) + '%s, depth: %s' % (src.__class__.__name__, dpth))

        else:
            print(tabs(dpth) + '%s %s, depth: %s' % (src, src.__class__.__name__, dpth))

# recursive_print(da)