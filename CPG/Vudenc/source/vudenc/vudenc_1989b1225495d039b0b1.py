def hunt_del(request, pk):...
hunt = get_object_or_404(Hunt, id=pk)
hunt.delete()
return redirect('threat_hunter:index')
