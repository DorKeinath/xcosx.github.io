#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ephraim Keinath'
# pic von https://openclipart.org/detail/189172/talking-fox
SITENAME = 'xcosx - DorKeinath'
SITEURL = 'http://localhost:8000'
SITETITLE = 'xcosx'
SITEDESCRIPTION = 'Hier schreibt DorKeinath über Ethik und Informatik'
#MENUITEMS = [('ABOUT ME', '/about.html')]

PATH = 'content'

TIMEZONE = 'Europe/Berlin'
# LOCALE = ('de_DE', 'de')
DEFAULT_LANG = 'de'
DEFAULT_DATE_FORMAT = '%a, %d. %B %Y'

DEFAULT_DATE = 'fs'
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Allgemeines'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True

#Favicon https://stackoverflow.com/questions/44209165/hosting-raw-html-pages-in-a-pelican-static-website
STATIC_PATHS = ['images', 'authors', 'extra']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# FAVICON = 'extra/favicon.ico'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget mit http://fontawesome.io/icons/
SOCIAL = (('commenting-o', '/pages/kontakt.html'),
          ('rss', 'feed.html'),
          ('github', 'https://github.com/DorKeinath')
         )

# SHARE_BUTTONS = ('mail')

# Blogroll
#LINKS = (('Home', 'http://getpelican.com/'),
#         ('Über mich', 'http://python.org/'),
#         ('Impressum', 'http://jinja.pocoo.org/'))

DEFAULT_PAGINATION = 20

SUMMARY_MAX_LENGTH = 70

# DISQUS_SITENAME = "fabisblog"

# GOOGLE_ANALYTICS = "UA-98289312-1"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = "/home/effe/Git/xcosx.github.io/themes/minimalX"

TAG_CLOUD = False
# Tagcloud Settings
TAG_CLOUD_STEPS = 5
TAG_CLOUD_MAX_ITEMS = 50
TAG_CLOUD_BADGE = True
TAG_CLOUD_SORTING = 'size'

# Author Pages
AUTHOR_PAGE_PATH = 'authors'

# Author Information
AUTHOR_INFO_SHORT_FABIAN_KEITEL = 'DorKeinath hat Mathematik und Philosophie studiert und beschäftigt sich (zu) viel mit Informatik.'

AUTHOR_INFO_FABIAN_KEITEL = 'Ich, DorKeinath, habe Mathematik und Philosophie studiert und beschäftige mich (zu) viel mit Informatik. <br>Entsprechend diesen Fachgebieten, diskutiere ich gerne über die ethische Relevanz von Informationstechnik. Beiträge, die gleichzeitig IT und Ethik betreffen, habe ich in der Kategorie IT-Ethik gespeichert. <br><br>Wenn ich nicht gerade arbeite oder vor dem PC sitze, gehe ich gerne Joggen oder ins <a style="color: red" href="https://de.wikipedia.org/wiki/Brazilian_Jiu-Jitsu">BJJ</a> (Brazilian Jiu-Jitsu). Das ist die anstrengendste Sportart, die ich kenne. Sehr zu empfehlen!'

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud", "autopages"]
# PLUGINS = ["autopages"]
