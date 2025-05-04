#!/usr/bin/env python
# -*- coding: utf-8 -*- #s

AUTHOR = 'John H. Clarke'
SITENAME = 'JohnClarkeMusic.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = 'theme/simple-jcm-2.0'  

OUTPUT_PATH = 'docs'

# STATIC_PATHS = ['static']

DISQUS_SITENAME = 'johnclarkemusic'
TWITTER_USERNAME= 'johnclarkemusic'

DEFAULT_OG_TITLE = SITENAME
DEFAULT_OG_DESCRIPTION = 'John Clarke Music'
DEFAULT_OG_IMAGE = 'https://johnclarkemusic.com' + '/theme/images/header-2_cropped-thin.jpg'
DEFAULT_OG_URL = 'https://johnclarkemusic.com'
DEFAULT_OG_TYPE = 'website'

MENUITEMS= []

PAGE_EXCLUDES = 'static'
STATIC_PATHS = ['static', 'images' ,'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}


INDEX_SAVE_AS = 'blog_index.html'
