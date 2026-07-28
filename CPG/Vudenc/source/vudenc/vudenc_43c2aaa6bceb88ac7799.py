def show_log(stdout):...
i = 0
for line in stdout:
i = i + 1
line_class = 'line3' if i % 2 == 0 else 'line'
print('<div class="' + line_class + '">' + escape_html(line) + '</div>')
