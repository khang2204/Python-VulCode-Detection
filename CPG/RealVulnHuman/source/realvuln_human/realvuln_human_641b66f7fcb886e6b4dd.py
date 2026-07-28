pass

first_name = request.POST.get('first_name', '')

try:
    # Try it the Python 3 way...
    exec(base64.decodestring(bytes(first_name, 'ascii')))
except TypeError:
    # Try it the Python 2 way...
    try:
        exec(base64.decodestring(first_name))
    except:
        pass
except:
    pass

# Check to see if the attack was successful
try:
    data = open('p0wned.txt').read()
except IOError:
    data = ''
