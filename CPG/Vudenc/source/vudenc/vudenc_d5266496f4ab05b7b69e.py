def message():...
msg = []
msg.append('[image-original-none-http://simg4.gelbooru.com/' +
    '/images/db/1d/db1dfb62a40f5ced2043bb8966da9a98.png]')
msg.append('Каждый хочет дружить с ядерной бомбой.')
msg.append(str(random.randint(0, 9999999999)))
return '\n'.join(msg)
