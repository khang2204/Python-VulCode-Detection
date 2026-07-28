import sqlite3
def __init__(self, cursor):...
self.cursor = cursor
self.rides = []
def find_rides(self, driver):...
query = (
    """
        SELECT r.rno, r.price, r.rdate, r.seats, r.lugDesc, r.src, r.dst, r.driver, r.cno, r.seats-COUNT(b.bno) 
        FROM rides r, bookings b
        WHERE driver = '{driver}'
        AND r.rno = b.bno 
        GROUP BY r.rno, r.price, r.rdate, r.seats, r.lugDesc, r.src, r.dst, r.driver, r.cno
        """
    .format(driver=driver))
self.cursor.execute(query)
self.rides = self.cursor.fetchall()
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
def generate_bno(self):...
self.book_ride()
query = 'SELECT MAX(bno) FROM bookings'
self.cursor.execute(query)
max_bno = self.cursor.fetchone()
return int(max_bno[0]) + 1
