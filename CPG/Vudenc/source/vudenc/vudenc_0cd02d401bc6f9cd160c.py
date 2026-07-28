def replyToTrackRequest(comment, positive):...
if positive == True:
print('I will be tracking this series: ' + getTitle(comment.submission.
    title) + ' because of this comment ' + comment.fullname)
print('I will stop tracking this series: ' + getTitle(comment.submission.
    title) + ' because of this comment ' + comment.fullname)
