def get(self, request, format=None):...
end_str = request.GET.get('end', None)
if end_str:
return self.streaming_response(f'wins_current_fy_{now().isoformat()}.csv')
self.end_date = models.DateField().to_python(end_str)
self.end_date = None
