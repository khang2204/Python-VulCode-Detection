def hunt_switch_enable(request, pk):...
hunt = get_object_or_404(Hunt, id=pk)
if hunt.enable == True:
hunt.setDisable()
hunt.setEnable()
hunt.stop()
hunt.start()
return redirect('twitter_hunter:index')
