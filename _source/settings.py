#!/usr/bin/env python
# -*- coding: utf-8 -*- #

SITENAME = "Peter Desmet"
SITESUBTITLE = "Blue is the new red"
SITEURL = "http://peterdesmet.com"
SITEDESCRIPTION = "My personal blog on open data, design, travel, and other stuff."
AUTHOR = "Peter Desmet"

TIMEZONE = "Europe/Paris"
DEFAULT_LANG = "en"
MARKUP = "md"

# Reading settings
DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = None
DEFAULT_DATE_FORMAT  = "%B %d, %Y"
SUMMARY_MAX_LENGTH = -1

# Directory settings
DELETE_OUTPUT_DIRECTORY = False # True doesn't seem to work + Not sure if it would remove _source
PATH = ""
ARTICLE_DIR = "posts"
PAGE_DIR = "pages"
STATIC_PATHS = (
    ("images"),
    ("files"),
)
OUTPUT_PATH = "../" # One level above the _source folder

# URLs
ARTICLE_URL = "posts/{slug}.html" # Both slug and slug.html will work
ARTICLE_SAVE_AS = "posts/{slug}.html"

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

# Theme
THEME = "../../spoonbill" # Relative link to theme repository

# External services
DISQUS_SITENAME = "peterdesmet"
GOOGLE_ANALYTICS = "UA-2043127-1"
GOOGLE_WEBMASTER = "QsSLW3AksA4dYqzZOsQLzsIcy5qYYH09wl9CzHtADFs"
GITHUB_URL = "https://github.com/peterdesmet"
TWITTER_URL = "https://twitter.com/peterdesmet"

# Blogroll
LINKS = (
)

# Social widget
SOCIAL = (
    ("Twitter", "https://twitter.com/peterdesmet"),
    ("LinkedIn","http://www.linkedin.com/in/peterdesmet"),
    ("GitHub","https://github.com/peterdesmet"),
    ("Disqus","http://disqus.com/peterdesmet/"),
    ("Speakerdeck","https://speakerdeck.com/peterdesmet"),
    ("Last.fm","http://www.last.fm/user/anderhalv"),
    ("Goodfil.ms","https://goodfil.ms/anderhalv"),
)