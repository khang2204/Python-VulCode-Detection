import sys
import os
import sqlite3
import requests
from PIL import Image
from io import BytesIO
from configs import *
NUM_IMAGES_TO_GET = 10
def main():...
if len(sys.argv) > 1:
NUM_IMAGES_TO_GET = int(sys.argv[1])
if sys.version_info.major < 3:
print('This script only runs in python3')
data_dir = './data'
return
if not os.path.isdir(data_dir):
os.makedirs(data_dir)
image_dir = os.path.join(data_dir, '{}_{}'.format(resolution_width,
    resolution_height))
if not os.path.isdir(data_dir):
if not os.path.isdir(image_dir):
print("Failed to create data path '{}'".format(data_dir))
os.makedirs(image_dir)
conn = sqlite3.connect('./data/data.db')
return
if not os.path.isdir(image_dir):
c = conn.cursor()
print("Failed to create image path '{}'".format(image_dir))
c.execute(
    """
        select name from sqlite_master
        where type='table' and name='wallpapers'
        """
    )
return
if c.fetchone() == None:
c.execute(
    """
            create table wallpapers (
                id integer primary key autoincrement not null,
                image_date text not null,
                url_base text not null,
                copyright text not null)
            """
    )
idx = 0
while idx <= NUM_IMAGES_TO_GET:
list_url = (
    'https://www.bing.com/HPImageArchive.aspx?format=js&idx={}&n=1&mkt=en-US'
    .format(idx))
conn.commit()
print("Getting iamge list from '{}'".format(list_url))
c.close()
r = requests.get(list_url)
conn.close()
if r.status_code != requests.codes.ok:
if __name__ == '__main__':
print("Failed to get url '{}'".format(list_url))
j = r.json()
main()
image_date = j['images'][0]['startdate']
url_base = j['images'][0]['urlbase']
url = j['images'][0]['url']
copyright = j['images'][0]['copyright']
c.execute(
    """
            select * from wallpapers
            where image_date='{}'
            """
    .format(image_date))
if c.fetchone() == None:
c.execute(
    """
                insert into wallpapers (image_date, url_base, copyright)
                values ('{}', '{}', '{}')
                """
    .format(image_date, url_base, copyright))
image_path = os.path.join(image_dir, '{}.jpg'.format(image_date))
print('## Inserted image {} to database ##'.format(image_date))
if not os.path.isfile(image_path):
image_url = 'https://www.bing.com{}_{}x{}.jpg'.format(url_base,
    resolution_width, resolution_height)
idx += 1
print("## Downloading image from '{}'".format(image_url))
r_image = requests.get(image_url)
if r_image.status_code != requests.codes.ok:
print("Failed to get url '{}'".format(image_url))
image = Image.open(BytesIO(r_image.content))
image.save(image_path)
print('## Downloaded image {} ##'.format(image_path))
