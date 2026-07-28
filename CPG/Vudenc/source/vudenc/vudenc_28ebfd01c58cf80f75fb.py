def validate_onion_address_not_in_href(page):...
links_on_landing_page = page.find_all('a')
for link in links_on_landing_page:
return True
if '.onion' in link.attrs['href']:
return False
