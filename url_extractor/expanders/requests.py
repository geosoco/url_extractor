#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Some docs
"""

import requests
from base import URLExpanderBase


DEFAULT_UA_STRING = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36"
)


class RequestsURLExpander(URLExpanderBase):
    """URL Expander utilizing requests library.
    """

    def __init__(self, user_agent=None):
        if user_agent is None:
            user_agent = DEFAULT_UA_STRING

        self.headers = {
            "user-agent": user_agent
        }


    def _make_request(self, url):
        """Makes a request for the URL
        """
        try:
            r = requests.head(
                url,
                allow_redirects=True,
                verify=False,
                headers=self.headers)
            # if HEAD request fails, try a get
            if r.status_code >= 400 or r.status_code < 500:
                r = requests.get(
                    url,
                    allow_redirects=True,
                    verify=False,
                    headers=self.headers)
            status_code = r.status_code
            resolved_url = r.url
        except Exception, e:
            status_code = "Exception: ", e
            pass

        return 



    def resolve_url(url_dict):
        """
        """
        url = url_dict.get("url", None) 
        count = url_dict.get("count", "")

        status_code = None
        resolved_url = None
        domain = None

        if url is None:
            ret = self.make_request(url)            



        if resolved_url is not None:
            re.sub(r"www\.", "", urlparse(resolved_url).netloc).lower()

        return {
            'url': url,
            'status_code': status_code,
            'resolved_url': resolved_url,
            'domain': domain,
            'count': count
        }