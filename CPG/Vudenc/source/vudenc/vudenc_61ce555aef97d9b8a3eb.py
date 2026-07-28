@validate(meetup=VMeetup('id'), sort=VMenu('controller', CommentSortMenu),...
article = Link._byID(meetup.assoc_link)
user_num = c.user.pref_num_comments or g.num_comments
num = g.max_comments if num_comments == 'true' else user_num
builder = CommentBuilder(article, CommentSortMenu.operator(sort), None, None)
listing = NestedListing(builder, num=num, parent_name=article._fullname)
displayPane = PaneStack()
if c.user_is_loggedin:
displayPane.append(CommentReplyBox())
displayPane.append(listing.listing())
displayPane.append(CommentReplyBox(link_name=article._fullname))
sort_menu = CommentSortMenu(default=sort, type='dropdown2')
nav_menus = [sort_menu, NumCommentsMenu(article.num_comments, default=
    num_comments)]
content = CommentListing(content=displayPane, num_comments=article.
    num_comments, nav_menus=nav_menus)
lastViewed = None
if c.user_is_loggedin:
clicked = article._getLastClickTime(c.user)
res = ShowMeetup(meetup=meetup, content=content, fullname=article._fullname,
    lastViewed=lastViewed)
lastViewed = clicked._date if clicked else None
return BoringPage(pagename=meetup.title, content=res, body_class='meetup'
    ).render()
article._click(c.user)
