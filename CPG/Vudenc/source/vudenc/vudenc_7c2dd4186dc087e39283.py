def get_review():...
request_data = request.get_json()
title = request_data['review']['title']
comment = request_data['review']['comment']
rating = request_data['review']['rating']
review = {'title': title, 'comment': comment, 'rating': rating}
return review
