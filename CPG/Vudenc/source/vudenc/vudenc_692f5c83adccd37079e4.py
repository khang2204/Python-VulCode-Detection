@commands.command()...
"""docstring"""
await self.simple_embed(
    """If your power LED turns on and off after you installed b9s, you are not bricked and are just missing a file called boot.firm in the root of your SD card.
To fix this you should:
1.Check you inserted the SD card in your console
2.Place/replace the file, downloading it from https://github.com/AuroraWright/Luma3DS/releases
Checking your SD for errors or corruption:
	Windows: https://3ds.guide/h2testw-(windows)#
	Linux: https://3ds.guide/f3-(linux)#
	Mac: https://3ds.guide/f3x-(mac)#"""
    , title='No. You are not bricked')
