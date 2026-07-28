def detectForms(html):...
soup = BeautifulSoup(html, 'html.parser')
detectedForms = soup.find_all('form')
returnForms = []
if len(detectedForms) > 0:
for f in detectedForms:
return returnForms
fileInputs = f.findChildren('input', {'type': 'file'})
if len(fileInputs) > 0:
returnForms.append((f, fileInputs))
