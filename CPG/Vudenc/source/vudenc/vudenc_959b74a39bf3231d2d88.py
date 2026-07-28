def create(self, request, *args, **kwargs):...
room_id = self.request.data.get('room')
self.room = Room.objects.get(pk=room_id)
return Response(status=status.HTTP_400_BAD_REQUEST)
self.request.data['sent_by'] = self.request.user.id
self.request.data['room'] = self.room.id
self.request.data['text'] = self.request.data.get('message')
serializer = self.get_serializer(data=request.data)
self.perform_create(serializer)
return Response(serializer.data, status=status.HTTP_201_CREATED)
