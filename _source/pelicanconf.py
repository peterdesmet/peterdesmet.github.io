#!/usr/bin/env python
# -*- coding: utf-8 -*- #

SITENAME = u"Anderhalv"
SITEURL = "http://peterdesmet.github.com"
AUTHOR = u"Peter Desmet"

TIMEZONE = "Europe/Paris"
DEFAULT_LANG = u"en"

OUTPUT_PATH = "../" # One level above the _source folder
DEFAULT_PAGINATION = False # Verify
DELETE_OUTPUT_DIRECTORY = False # True doesn't seem to work + Not sure if it would remove _source
DISPLAY_PAGES_ON_MENU = True
FEED_ALL_RSS = "feeds/rss.xml" # Verify
FEEDS_ALL_ATOM = None # Verify

THEME = "tuxlite_tbs"

# Ignore the following work folders during publication
PAGE_EXCLUDES = (
	("Portfolio"),
	("Other"),
)
ARTICLE_EXCLUDES = (
	("pages"),
	("Portfolio"),
	("Other"),
)

# External services
DISQUS_SITENAME = "" # Set
GOOGLE_ANALYTICS = "" # Set
GITHUB_URL = "https://github.com/peterdesmet"

# Blogroll
LINKS = (
)

# Social widget
SOCIAL = (
	("Twitter", "https://www.twitter.com/peterdesmet"),
	("GitHub","https://github.com/peterdesmet"),
	("LinkedIn","http://www.linkedin.com/in/peterdesmet"),
	("Last.fm","http://www.last.fm/user/anderhalv"),
)