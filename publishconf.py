#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://xcosx.github.io'
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ALL_RSS = 'feeds/all.rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'

DELETE_OUTPUT_DIRECTORY = False
RSS_FEED_SUMMARY_ONLY = False

#THEME = "/home/fabi/blog/themes/minimalX"

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
