def add_price(self, itemid, storeid, price):...
"""docstring"""
r = self.cursor.execute(
    'select priceid, itemid, storeid, price from itemprices where (itemid = %s and storeid = %s)'
     % (itemid, storeid)).fetchall()
if r == []:
t = itemid, storeid, price
self.cursor.execute(
    'update itemprices set price = "%s" where (itemid = "%s" and storeid = "%s")'
     % (price, itemid, storeid))
self.cursor.execute(
    'insert into itemprices (itemid, storeid, price) values (?, ?, ?)', t)
self.connection.commit()
self.connection.commit()
