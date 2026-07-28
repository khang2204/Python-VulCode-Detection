@handle_html...
text = '\n'.join(('<a href="/mapmaker">/mapmaker</a><br/>',
    '<a href="/map">/map</a><br/>', '<a href="/login">/login</a><br/>',
    '<a href="/settings">/settings</a><br/>',
    '<a href="/mazetest">/mazetest</a><br/>',
    '<a href="http://disco.fleo.se/TEAM%2010%20FTW!!!">Team 10 FTW</a>'))
return base.format(text=text)
