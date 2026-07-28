def perform_create(self, serializer):...
serializer.is_valid(self)
instance = serializer.save(sent_by=self.request.user, room=self.room)
if not settings.IS_TESTING:
data = {'id': instance.id.__str__(), 'timestamp': instance.time_ago,
    'timestamp_string': instance.timestamp_string, 'user_handle': self.
    request.user.full_name, 'user_type': self.request.user.user_type,
    'message': instance.text, 'file_name': os.path.basename(urlparse(
    instance.attachment.path).path) if instance.attachment else None,
    'file_link': instance.file_download_link if instance.attachment else None}
group_channel = get_room_group_channel(instance.room.id)
self.push_socket_update(group_channel, data)
