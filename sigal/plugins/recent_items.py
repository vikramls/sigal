# -*- coding: utf-8 -*-

"""Plugin which generates a recent-changes album.

Settings:
- ``recent_items``, see below

Example::

    recent_items = {'nb_items':10, 'recent_dir':'recent'}

"""

import logging
import os
import codecs

from datetime import datetime
from sigal import signals

from ..gallery import Album

logger = logging.getLogger(__name__)


def generate_recents(gallery):
    images = [img for album in gallery.albums.values()
              for img in album.images if img.date is not None]
    images.sort(key=lambda im:im.date, reverse=True)

    settings = gallery.settings
    recent_items = settings.get('recent_items')
    nb_items = 10
    if recent_items:
        nb_items = recent_items.get('nb_items', 10) # default 10

    recent_dir = recent_items.get('recent_dir', 'recent')
    if recent_dir in gallery.albums:
        # TODO: The recent_dir specified is already an album
        pass
    root_album = gallery.albums['.']
    
    nb_items = min(nb_items, len(images))
    files = []

    for item in images[:nb_items]:
        files.append(item.path)

    album = Album(os.path.join(root_album, recent_dir), settings, [], files, gallery)
    album.create_output_directories()
    if settings.get('write_html'):
        writer = Writer(settings, index_title=gallery.title)
        writer.write(album)

def register(settings):
    signals.gallery_build.connect(generate_recents)
