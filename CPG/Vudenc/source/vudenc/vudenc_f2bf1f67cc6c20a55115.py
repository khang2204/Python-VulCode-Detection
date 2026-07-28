import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.httpclient
import tornado.gen
import os
import random
import shutil
import json
import multiprocessing
from utilities import sort_naturally
import settings
import redditUserImageScraper
enable_authentication = False
if enable_authentication:
import PasswordManager
authenticated_users = []
videoExtensions = '.mp4', '.webm'
supportedExtensions = '.gif', '.jpg', '.jpeg', '.png', '.mp4', '.webm'
savedImagesCache = []
def generateSavedImagesCache(outputDir):...
savedImagesCache = []
print('Creating Liked Saved cache...')
for root, dirs, files in os.walk(outputDir):
for file in files:
print('Finished creating Liked Saved cache ({} images/videos)'.format(len(
    savedImagesCache)))
if file.endswith(supportedExtensions):
def outputPathToServerPath(path):...
savedImagesCache.append(os.path.join(root, file))
return 'output' + path.split(settings.settings['Output_dir'])[1]
