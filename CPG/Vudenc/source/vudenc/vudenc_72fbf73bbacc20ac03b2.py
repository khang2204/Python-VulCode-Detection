def action_button(label, url):...
action = (
    "<a href='{}'><button type='button' class='btn btn-sm'>{}</button></a>"
    .format(url, label))
return action
