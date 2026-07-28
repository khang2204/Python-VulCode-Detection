@handled_slot(bool)...
print('Opening IDLE.')
subprocess.Popen(
    'python -m idlelib -t "Matisse Controller - Python Shell" -c "from matisse import Matisse; '
     +
    'matisse = Matisse(); print(\'Access the Matisse using \\\'matisse.[method]\\\'\')"'
    )
