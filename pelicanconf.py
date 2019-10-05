#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'themes/pelican-alchemy/alchemy'

AUTHOR = 'Annanda Sousa'
SITENAME = 'Annanda Sousa'
SITESUBTITLE = ''
SITEURL = ''
DESCRIPTION = SITESUBTITLE


PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'Europe/Dublin'

DEFAULT_LANG = 'en'

TYPOGRIFY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'

SITEIMAGE = '/images/logo-3.jpg'
# PYGMENTS_STYLE = 'default'
PYGMENTS_STYLE = 'monokai'
RFG_FAVICONS = True
