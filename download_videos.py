#!/usr/bin/python

import requests
import os

os.makedirs('Features', exist_ok=True)

PLAYLISTS = ['playlist_day.m3u', 'playlist_night.m3u']

for playlist in PLAYLISTS:
    with open(playlist, 'r') as playf:
        vids = playf.readlines()
        for vid in vids:
            vid = vid.strip()
            out = vid.replace('http://a1.phobos.apple.com/us/r1000/000/', './')
            vidf = requests.get(vid)
            print(f'downloading {out}...', end='')
            os.makedirs(os.path.dirname(out), exist_ok=True)
            with open(out, 'wb') as outf:
                outf.write(vidf.content)
            print('done')
