# -*- coding: utf-8 -*-

source = 'pictures'
thumb_suffix = '.tn'
thumb_size = (200, 150)
keep_orig = True

links = [('Example link', 'http://example.org'),
         ('Another link', 'http://example.org')]

from sigal.plugins import copyright
plugins = ['sigal.plugins.adjust', copyright, 'sigal.plugins.feeds', ]
copyright = u"© An example copyright message"
adjust_options = {'color': 0.0, 'brightness': 1.0,
                  'contrast': 1.0, 'sharpness': 0.0}

rss_feed = {'feed_url': 'http://example.org/feed.rss', 'nb_items': 10}
atom_feed = {'feed_url': 'http://example.org/feed.atom', 'nb_items': 10}

# theme = 'galleria'
# thumb_size = (280, 210)
