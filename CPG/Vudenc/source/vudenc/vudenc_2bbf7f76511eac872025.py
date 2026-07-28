def request_and_scrape_page(url, allow_redirects=True):...
"""docstring"""
page = requests.get(url, allow_redirects=allow_redirects)
page = requests.get('https://{}'.format(url), allow_redirects=allow_redirects)
return page, soup
soup = BeautifulSoup(page.content, 'lxml')
soup = BeautifulSoup(page.content, 'lxml')
