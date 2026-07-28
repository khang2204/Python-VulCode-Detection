@commands.command()...
"""docstring"""
await self.simple_embed(
    """1. Navigate to the following folder on your SD card: `/Nintendo 3DS/(32 Character ID)/(32 Character ID)/extdata/00000000/`
2. Delete the corresponding folder for your region:
  USA: `000002cd`
   EUR: `000002ce`
   JPN: `000002cc`"""
    , title='How to delete Home Menu Theme Data')
