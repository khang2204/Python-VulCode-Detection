@validate(VUser(), meetup=VEditMeetup('id'))...
return BoringPage(pagename='Edit Meetup', content=EditMeetup(meetup, title=
    meetup.title, description=meetup.description, location=meetup.location,
    latitude=meetup.latitude, longitude=meetup.longitude, timestamp=int(
    meetup.timestamp * 1000), tzoffset=meetup.tzoffset)).render()
