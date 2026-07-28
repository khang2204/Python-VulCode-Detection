async def send_channel_message(self, message, channel_name):...
channels = self.get_all_channels()
channel = [x for x in channels if x.name == channel_name][0]
await channel.send(message)
