def hunt_del(request, pk):...
hunt = get_object_or_404(Hunt, id=pk)
hunt.stop()
hunt.delete()
return redirect('twitter_hunter:index')
