def hunt_switch_enable(request, pk):...
hunt = get_object_or_404(Hunt, id=pk)
if hunt.enable == True:
hunt.setDisable()
hunt.setEnable()
return redirect('threat_hunter:index')
hunt.run()
