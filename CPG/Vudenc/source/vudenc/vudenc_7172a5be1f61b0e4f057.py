def route_add(self, net, mask, gateway):...
"""docstring"""
cmd = '/usr/bin/tmsh create net route {0}/{1} gw {2}'.format(net, mask, gateway
    )
return shellutil.run(cmd, chk_err=False)
