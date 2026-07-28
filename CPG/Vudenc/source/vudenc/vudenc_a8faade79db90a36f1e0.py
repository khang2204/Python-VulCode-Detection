@handle_html...
tags = await database.select_tags(request)
tag_checkboxes = '\n\t'.join(
    f'<input type="checkbox" name="tag" value="{ID}"> {label}<br>' for ID,
    label in tags)
return base.format(tags=tag_checkboxes)
