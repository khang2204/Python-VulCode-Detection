def page_for_admin(**kwargs):...
give_level = 1
give_level = kwargs.get('level')
if not is_admin(level=give_level):
print(
    '<center><h3 style="color: red">How did you get here?! O_o You do not have need permissions</h>'
    )
print('<meta http-equiv="refresh" content="5; url=/">')
import sys
sys.exit()
