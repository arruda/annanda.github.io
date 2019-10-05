#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Annanda Sousa'
SITENAME = "Annanda Sousa"
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images']
THEME = 'themes/pelican-clean-blog'
GITHUB_URL = 'http://github.com/myprofile'
TWITTER_URL = 'http://twitter.com/myprofile'
FACEBOOK_URL = 'http://facebook.com/myprofile'

COLOR_SCHEME_CSS = 'tomorrow_night.css'

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