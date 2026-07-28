args = parser.parse_args()
proto = 'http' if not args.ssl else 'https'

try:
    httpd = VulnHTTPServer((args.host, args.port), VulnHTTPRequestHandler)
    httpd.RequestHandlerClass.risk = args.risk

    if args.ssl:
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ctx.options &= ~ssl.OP_NO_SSLv3
        ctx.options &= ~ssl.OP_NO_COMPRESSION
        ctx.options &= ~ssl.OP_CIPHER_SERVER_PREFERENCE
        ctx.load_cert_chain(certfile='./ssl/cert.pem', keyfile='./ssl/key.pem')
        httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)

    print('[*] Navigate to {}://{}:{} to access DSVPWA'.format(proto, args.host, args.port))
    httpd.serve_forever()
except KeyboardInterrupt:
    print('[*] Quitting...')
    pass
except Exception as ex:
    print("[!] Exception occurred ('%s')" % ex)
