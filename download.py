from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

# APIキーの情報
key = "905bcf94fc7191ed981307990e3b6ed2"
secret = "54e5fc2a532dfc7e"
wait_time = 1

# 保存フォルダの指定
pancake = sys.argv[1]
savedir = "/Users/daiki/pancake_classifier/" + pancake

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text        = pancake,
    per_page    = 630000,
    media       = 'photos',
    sort        = 'relevance',
    safe_search = 1,
    extras      = 'url_q, license'
)

photos = result['photos']
for i, photo in enumerate(photos['photo']):
    url_q    = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q ,filepath)
    time.sleep(wait_time)
