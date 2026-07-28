print("JWT Token from API: {0}".format(decoded))
        return True
    except DecodeError:
        print("Error in decoding token")
        return False
    except MissingRequiredClaimError as e:
        print('Claim required is missing: {0}'.format(e))
        return False

def insecure_verify(token):
    decoded = jwt.decode(token, verify = False)
    print(decoded)
    return True

@app.errorhandler(404)
def pnf(e):
    template = '''<html>
    <head>
    <title>Error</title>
    </head>
    <body>
