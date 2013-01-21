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

# Feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = None
FEED_RSS = None
FEED_ALL_ATOM = None
FEED_ALL_RSS = "feeds/rss.xml"
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

THEME = "tuxlite_tbs"

# URLs
ARTICLE_URL = "{date:%Y}/{slug}.html" # Both slug and slug.html will work
ARTICLE_SAVE_AS = "{date:%Y}/{slug}.html"

# Directory settings
STATIC_PATHS = (
	("images"),
	("files"),
)
PAGE_EXCLUDES = (
	("_exclude"),
	("Portfolio"),
)
ARTICLE_EXCLUDES = (
	("_exclude"),
	("pages"),
	("Portfolio"),
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