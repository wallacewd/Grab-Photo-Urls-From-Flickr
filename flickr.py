"""
Grab images urls from your flickr account
Author: Dan Wallace
Date: 09/30/2020
Website: www.brick.technology
*** This code is a useful but small part of larger project I am developing ***
"""

from flickrapi import FlickrAPI
import re

FLICKR_PUBLIC = 'api_public_key_here'
FLICKR_SECRET = 'api_private_key_here'
FLICK_USER_ID = 'flickr_user_id_here'
FLICKER_PHOTOSET_ID = 'flick_photoset_id_here'

flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
sets   = flickr.photosets.getPhotos(user_id=FLICK_USER_ID, photoset_id=FLICKER_PHOTOSET_ID)

photoFind = sets["photoset"]
photoFind1 = photoFind["photo"]
photoFind2 = photoFind1
length = len(photoFind2)

for x in range(length):
    final_photo = photoFind2[x]
    server_id = final_photo['server']
    photo_id = final_photo['id']
    photo_secret = final_photo['secret']
    photo_size = "b"
    server_url = 'https://live.staticflickr.com/' + server_id + '/' + photo_id + '_' + photo_secret + '_' + photo_size + '.jpg' 
    photo_url = server_url.replace(" ", "")
    print("Photo",x,":",photo_url)
