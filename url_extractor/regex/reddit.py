#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""


"""

"""
RE_REDDIT_URL is not the best regex, but it generally works. There are 
a few more constraints that could be enforced, like the length of the liveids
as is done in the RE_LIVE regex.
"""
RE_REDDIT_URL = r"(?:https?://)?(?:www\.)?reddit.com(?:/(r|u|live)/(\w*)(?:/comments/(\w*)/?[\w%]*/?(\w*)?(\?[^\n]*)?)?)?"
RE_LIVE = r"/?(?<!\w)live/\w{10,12}(?!\w)"
RE_USER = r"/?(?<!\w)u/\w+"
RE_SUB = r"/?(?<!\w)r/\w+"
RE_REDDIT_LINKS = r"reddit.com/(r|live|u)"
