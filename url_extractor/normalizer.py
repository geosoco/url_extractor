#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

from six.moves import html_parser
from six.moves.urllib.parse import (urlparse, unquote)


class URLNormalizer(object):
    """Converts URLs into a more normal form to better compare.

    This class handles a variety of situations which could arise in
    grabbing URLS including html entities from text, encoded urls,
    capitalization, query parameters, etc.
    """

    def __init__(
            self, decode_html=True, decode_url_entities=True,
            adjust_case=True):
        """Constructs an object to normalize URLs. 

        Args:
            decode_html (bool): True to decode HTML entites from the URL
            decode_url_entities (bool): True to decode URL entities
            adjust_case (bool): True adjust the case of casse-insensitive 
                parts of the URL (protocol and domain)
        """
        self.decode_entities = decode_html
        self.decode_url_entities = decode_url_entities
        self.adjust_case = adjust_case
        self.html_parser = html_parser()

    def decode_html_entities(self, url):
        """Returns a string with HTML entities decoded.

        Args:
            url (str or unicode): input string

        Returns:
            string with html entities decoded.
        """
        return self.html_parser.unescape(url)


    def decode_url_entities(self, url):
        """Decodes URL entities.

        Referred to in python as unquoting them. These are the %XX escapes
        for special characters in a URL.

        Args:
            url (str or unicode): url to decode

        Returns:
            returns

        """
        return unquote(url)

    def normalize_parts(self, url):
        """
        """
        parts = urlparse(url)

        if self.adjust_case


    def normalize(self, url):
        """Normalize a url.

        Works by running a number of operations on the string to
        normalize it.

        Args:
            url (str or unicode): url to normalize

        Returns:
            (str or unicode): normalized url
        """

        nurl = url
        # decode entities first as that's a text leftover
        if self.decode_entities:
            nurl = self.decode_html_entities(nurl)

        # next decode url entities
        if self.decode_url_entities:
            nurl = self.decode_url_entities(nurl)
