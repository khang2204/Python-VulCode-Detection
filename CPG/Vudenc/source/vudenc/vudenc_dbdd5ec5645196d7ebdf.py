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
