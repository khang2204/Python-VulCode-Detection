def display_rides(self, page_num):...
page = self.rides[page_num * 5:min(page_num * 5 + 5, len(self.rides))]
for ride in page:
print(str(ride[0]) + '.', end='')
if page_num * 5 + 5 < len(self.rides):
print(ride)
user_input = input(
    "To book a member on a ride, please enter 'b'. To see more rides, please enter 'y'. To exit, press 'e': "
    )
user_input = input(
    "To book a member on a ride, please enter 'b'. To exit, press 'e': ")
if user_input == 'y':
if user_input == 'b':
self.display_rides(page_num + 1)
self.book_ride()
