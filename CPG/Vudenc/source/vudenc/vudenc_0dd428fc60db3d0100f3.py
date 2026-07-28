@commands.command()...
"""docstring"""
await self.simple_embed(
    """If you want to change your SD card to one bigger than 32GB then you'll have to format it to FAT32.
You can do this with the tool of your preference.
Formatter examples:
- [guiformat - Windows](http://www.ridgecrop.demon.co.uk/index.htm?guiformat.htm)
- [gparted - Linux](http://gparted.org/download.php)"""
    , title='Big SD cards')
