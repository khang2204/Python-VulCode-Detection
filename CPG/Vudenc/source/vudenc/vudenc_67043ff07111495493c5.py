def hunt_switch_notice(request, pk):...
hunt = get_object_or_404(Hunt, id=pk)
if hunt.notice == True:
hunt.setNoticeFalse()
hunt.setNoticeTrue()
hunt.run()
return redirect('threat_hunter:index')
