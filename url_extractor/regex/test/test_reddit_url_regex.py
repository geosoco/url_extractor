#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import re
from url_extractor.regex.reddit import (
    RE_REDDIT_URL,
    RE_LIVE,
    RE_USER,
    RE_SUB,
    RE_REDDIT_LINKS)



REDDIT_URL_PARAMS = {
    # full normal url
    "full normal url":
    (
        "https://www.reddit.com/r/news/comments/hgh53/big_news_article/a2f3l9d",
        [("r", "news", "hgh53", "a2f3l9d", "")]
    ),
    # no comment id & trailing slash
    "no comment id & trailing slash":
    (
        "https://www.reddit.com/r/news/comments/hgh53/big_news_article/",
        [("r", "news", "hgh53", "", "")]
    ),
    # no comment id trailing slash
    "no comment id trailing slash":
    (
        "https://www.reddit.com/r/news/comments/hgh53/big_news_article",
        [("r", "news", "hgh53", "", "")]

    ),
    # http
    "http":
    (
        "http://www.reddit.com/r/news/comments/hgh53/big_news_article",
        [("r", "news", "hgh53", "", "")]

    ),
    # no protocol
    "no protocol":
    (
        "www.reddit.com/r/news/comments/hgh53/big_news_article/",
        [("r", "news", "hgh53", "", "")]
    ),
    # no protocol or www
    "no protocol or www":
    (
        "reddit.com/r/news/comments/hgh53/big_news_article/",
        [("r", "news", "hgh53", "", "")]

    ),
    # just article url
    "just article url":
    (
        "reddit.com/r/news/comments/hgh53/",
        [("r", "news", "hgh53", "", "")]
    ),
    # no article name or trailing slash
    "no article name or trailing slash":
    (
        "reddit.com/r/news/comments/hgh53",
        [("r", "news", "hgh53", "", "")]
    ),
    # only reddit.com
    "only reddit.com":
    (
        "reddit.com",
        [("", "", "", "", "")]
    ),
    # username
    "username":
    (
        "reddit.com/u/username",
        [("u", "username", "", "", "")]
    ),
    # only reddit.com
    "only reddit.com":
    (
        "reddit.com",
        [("", "", "", "", "")]
    )
}


@pytest.fixture
def reddit_regex():
    return re.compile(RE_REDDIT_URL)


@pytest.mark.parametrize(
    "text, expected",
    REDDIT_URL_PARAMS.values(),
    ids=REDDIT_URL_PARAMS.keys())
def test_reddit_url_regex_equal(reddit_regex, text, expected):
    assert reddit_regex.findall(text) == expected


"""
=======================================================================

Live URL Regex Tests


=======================================================================
"""

REDDIT_LIVE_URL_PARAMS = {
    "Full URL":
    (
        "reddit.com/live/c2bmrktaqig3",
        [("/live/c2bmrktaqig3")]
    ),
    "live text, no prior slash":
    (
        "live/c2bmrktaqig3",
        [("live/c2bmrktaqig3")]
    ),

    "live w/ prior slash":
    (
        "/live/c2bmrktaqig3",
        [("/live/c2bmrktaqig3")]
    ),

    "alpha characters before live [fail]":
    (
        "alive/c2bmrktaqig3",
        []
    ),

    "id too short":
    (
        "live/c2bmrktaq",
        []
    ),

    "id too long":
    (
        "live/c2bmrktaqig3a",
        []
    ),
    # XXX soco - Should this fail?
    # this is an odd case that is possible, but not sure if it should
    # pass or fail
    "multiple concatened w/o space":
    (
        "/live/c2bmrktaqig3/live/c2bmrktaqig3",
        [("/live/c2bmrktaqig3"), ("/live/c2bmrktaqig3")]
    ),

    "multiple with space":
    (
        "/live/c2bmrktaqig3 /live/c2bmrktaqig3",
        [("/live/c2bmrktaqig3"), ("/live/c2bmrktaqig3")]
    ),
}

@pytest.fixture
def reddit_live_regex():
    return re.compile(RE_LIVE)

@pytest.mark.parametrize(
    "text, expected",
    REDDIT_LIVE_URL_PARAMS.values(),
    ids=REDDIT_LIVE_URL_PARAMS.keys())
def test_reddit_live_url_regex_equal(reddit_live_regex, text, expected):
    assert reddit_live_regex.findall(text) == expected


"""
=======================================================================

User URL Regex Tests


=======================================================================
"""

REDDIT_USER_URL_PARAMS = {
    "Full user URL":
    (
        "reddit.com/u/peanutbutter",
        [("/u/peanutbutter")]
    ),
    "user, no prior slash":
    (
        "u/peanutbutter",
        [("u/peanutbutter")]
    ),

    "user w/ prior slash":
    (
        "/u/peanutbutter",
        [("/u/peanutbutter")]
    ),

    "alpha characters before user [fail]":
    (
        "emu/peanutbutter",
        []
    ),

    # XXX soco - Should this fail?
    # this is an odd case that is possible, but not sure if it should
    # pass or fail
    "multiple concatened w/o space":
    (
        "u/peanutbutter/u/peanutbutter",
        [("u/peanutbutter"), ("/u/peanutbutter")]
    ),

    "multiple with space":
    (
        "u/peanutbutter /u/peanutbutter",
        [("u/peanutbutter"), ("/u/peanutbutter")]
    ),
}

@pytest.fixture
def reddit_user_regex():
    return re.compile(RE_USER)

@pytest.mark.parametrize(
    "text, expected",
    REDDIT_USER_URL_PARAMS.values(),
    ids=REDDIT_USER_URL_PARAMS.keys())
def test_reddit_user_url_regex_equal(reddit_user_regex, text, expected):
    assert reddit_user_regex.findall(text) == expected


# TODO soco - create tests for other regexes
#
#
