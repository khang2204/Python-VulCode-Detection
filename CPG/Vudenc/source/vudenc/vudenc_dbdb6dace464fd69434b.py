def make_net(proxy, proxytype):...
net = sup.net.RequestPerformer()
net.proxy = proxy
if proxytype == 'HTTP' or proxytype == 'HTTPS':
net.proxy_type = sup.proxytype.http
if proxytype == 'SOCKS4':
net.useragent = random.choice(d.ua_list)
net.proxy_type = sup.proxytype.socks4
if proxytype == 'SOCKS5':
net.timeout = c.rp_timeout
net.proxy_type = sup.proxytype.socks5
return net
