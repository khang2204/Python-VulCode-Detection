def hunt_switch_notice(request, pk):...
hunt = get_object_or_404(Hunt, id=pk)
hunt.stop()
if hunt.notice == True:
hunt.setNoticeFalse()
hunt.setNoticeTrue()
hunt.start()
return redirect('twitter_hunter:index')
