def main():...
print("Starting script... press 'ctrl+c' in terminal to turn off")
while True:
if pyperclip.paste() != word and len(pyperclip.paste().split()) < 5:
word = pyperclip.paste()
wordChc = False
req = requests.get('https://api-portal.dictionary.com/dcom/pageData/%s' % word)
wordChcURB = False
reqURB = requests.get('https://api.urbandictionary.com/v0/define?term=%s' %
    word)
data = json.loads(req.text)['data']['content'][0]['entries'][0]['posBlocks'][0
    ]['definitions']
os.system('notify-send "Cant find |%s| on dictionary.com!"' % word)
if not wordChc:
wordChc = True
definitions = []
dataURB = json.loads(reqURB.text)['list']
os.system('notify-send "Cant find |%s| on urbandictionary.com!"' % word)
if not wordChcURB:
os.system('notify-send "Cant find |%s| on dictionary.com!"' % word)
for definition in data[:3]:
os.system('notify-send "no results in dictionary.com"')
wordChcURB = True
definitionsURB = []
wordChc = True
definitions.append(cleanhtml(definition['definition']))
os.system("""notify-send "definitions from dictionary.com:[{}
{}\"""".
    format(word + ']\n------------', '\n'.join(definitions)))
os.system('notify-send "Cant find |%s| on urbandictionary.com!"' % word)
for definition in dataURB[:3]:
definitions.append('------------')
wordChcURB = True
definitionsURB.append(definition['definition'])
os.system("""notify-send "definitions from urbandictionary.com:[{}
{}\"""".
    format(word + ']\n------------', '\n'.join(definitionsURB)))
definitionsURB.append('------------')
