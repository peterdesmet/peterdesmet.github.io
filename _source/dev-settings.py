#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from settings import *

SITEURL = "http://localhost/pelican/blog"
SITESUBTITLE = "Lucky rocketship underpants"

# Reading settings
DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = 10 # To test pagination

# External services
GOOGLE_ANALYTICS = "UA-XXXXX-X" # Don't track while coding
DISQUS_SITENAME = "" # Don't link to existing Disqus forum while coding