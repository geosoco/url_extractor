#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import re
from url_extractor.regex.core import RE_URL

URL_REGEX_PARAMS = [
    RE_URL
]

URL_REGEX_MATCH_PARAMS = [
    # simple
    ("http://a.com/a", ["http://a.com/a"]),
    # don't match trailing comma
    ("http://a.com/a,", ["http://a.com/a"]),
    # don't match trailing period
    ("http://a.com/a.", ["http://a.com/a"]),
    # don't match trailing period
    ("HTTP://a.com/a", ["HTTP://a.com/a"]),
    #
    (
        "http://imgur.com/a/jvqf6)|60|8|38|",
        ["http://imgur.com/a/jvqf6"]
    ),
    #
    (
        "http://bit.ly/neynfv)",
        ["http://bit.ly/neynfv"]
    ),
    #
    (
        "http://www.usairways.com/TravelCenter/Advisories.aspx,",
        ["http://www.usairways.com/TravelCenter/Advisories.aspx"]
    ),
    # period and trailing comma
    (
        "http://www.delta.com/content/www/en_US/traveling-with-us/alerts-and-advisories/boston.html,",
        ["http://www.delta.com/content/www/en_US/traveling-with-us/alerts-and-advisories/boston.html"]
    ),
    # params and commas
    (
        "http://www.madeup.com/12,29,35?title=welcome,tothe,jungle,",
        ["http://www.madeup.com/12,29,35?title=welcome,tothe,jungle"]
    ),
    # two matches separated by markdown punctuation
    (
        "pic.twitter.com/IGZvJd565S](https://twitter.com/WilliamsJon/status",
        [
            "pic.twitter.com/IGZvJd565S",
            "https://twitter.com/WilliamsJon/status"
        ]
    ),

]


@pytest.fixture
def cowboy_regex():
    return re.compile(RE_URL, re.I)

@pytest.mark.parametrize('text, expected', URL_REGEX_MATCH_PARAMS)
def test_findall_match(cowboy_regex, text, expected):
    print type(cowboy_regex), cowboy_regex
    assert cowboy_regex.findall(text) == expected
