def streaming_response(self, filename):...
resp = StreamingHttpResponse(self._make_flat_wins_csv_stream(self.
    _make_flat_wins_csv()), content_type=mimetypes.types_map['.csv'])
resp['Content-Disposition'] = f'attachent; filename={filename}'
return resp
