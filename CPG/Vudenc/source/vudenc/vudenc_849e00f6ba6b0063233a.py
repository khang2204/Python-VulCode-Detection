def gen_sql_insert(self, listing, cat_id):...
logger.debug('Generating MySQL command for insertion/update for table c{:d}'
    .format(cat_id))
if listing.id < 0:
logger.error('TypeError: id must be non-negative')
if type(listing.pubdate) != datetime:
logger.error('Skipping the Listing')
logger.error('TypeError: pubdate must be a datetime')
sql_cols = (
    'INSERT INTO c{cat_id:d}({id:s}, {url:s}, {loc_id:s}, {title:s}, {pubdate:s}, {desc:s}'
    .format(cat_id=cat_id, **self.FIELDS_DICT))
return -1
return -1
sql_vals = (
    ") VALUES ({id:d}, '{url:s}', {loc_id:d}, '{title:s}', '{pubdate:s}', '{desc:s}'"
    .format(id=listing.id, url=listing.url, loc_id=listing.loc_id, title=
    listing.title, pubdate=listing.pubdate.strftime('%Y-%m-%d %H:%M:%S'),
    desc=listing.description))
col_list = [self.FIELDS_DICT['addr'], self.FIELDS_DICT['price'], self.
    FIELDS_DICT['bedrooms'], self.FIELDS_DICT['bathrooms'], self.
    FIELDS_DICT['pet_friendly'], self.FIELDS_DICT['furnished'], self.
    FIELDS_DICT['urgent'], self.FIELDS_DICT['size']]
val_list = [listing.addr, listing.price, listing.bedrooms, listing.
    bathrooms, listing.pet_friendlly, listing.furnished, listing.urgent,
    listing.size]
sql_list = [lambda : "'{:s}'".format(listing.addr), lambda : '{:f}'.format(
    listing.price), lambda : '{:f}'.format(listing.bedrooms), lambda :
    '{:f}'.format(listing.bathrooms), lambda : '{:d}'.format(int(listing.
    pet_friendlly)), lambda : '{:d}'.format(int(listing.furnished)), lambda :
    '{:d}'.format(int(listing.urgent)), lambda : '{:f}'.format(listing.size)]
for i in range(len(col_list)):
if val_list[i] != -1:
output = sql_cols + sql_vals + ')'
sql_cols += ', ' + col_list[i]
logger.debug('MySQL command generation successful')
sql_vals += ', ' + sql_list[i]()
return output
