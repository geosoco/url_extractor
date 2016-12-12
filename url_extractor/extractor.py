#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
URLExtractor


"""

import re
import types
import itertools



class URLExtractorProcessorBase(object):
    """Base class for ExtractorProcessors.
    """

    def __init__(self):
        """Base class constructor
        """
        pass

    def extract(self, text):
        """Returns an array of extracted URLs.


        Args:
            text (str or unicode): string to search for urls

        Returns:
            list[str or unicode]
        """
        raise NotImplementedError


class URLExtractorRegexProcessor(URLExtractorProcessorBase):
    """Simple processor for a single regex.
    """

    def __init__(self, regex, flags=0):
        """Construct URLExtractorRegexProcessor from a regex

        Args:
            regex (str or unicode): regex string for matching URLs

        Returns:
            list[str or unicode]
        """
        self.re = re.compile(regex, flags)


    def extract(self, text):
        """Returns an array of extracted URLs.


        Args:
            text (str or unicode): string to search for urls


        Returns:
            list[str or unicode]
        """
        if text is None:
            return []
        return self.re.findall(text)


class URLExtractorMultiRegexProcessor(URLExtractorProcessorBase):
    """Processor for extracting URLs with multiple regexes.
    """

    def __init__(self, regex_list, flags=0):
        """Construct URLExtractorMultiRegexProcessor from a list of regexes

        Args:
            regex_list (list[str or unicode]): list of regexes for matching
                URLs

        Returns:
            list[str or unicode]
        """
        self.regex_list = [re.compile(r, flags) for r in regex_list]

    def extract(self, text):
        """Returns an array of extracted URLs.

        Args:
            text (str or unicode): string to search for urls

        Returns:
            list[str or unicode]
        """
        if text is None:
            return []
        matches = [r.findall(text) for r in self.regex_list]
        return list(itertools.chain(*matches))


class URLExtractor(object):
    """Class for extracting URLs from text objects
    """

    def __init__(self, processor_list=0):
        """
        """
        self.processors = processor_list


    def extract_urls(self, text, unique=False):
        """Extract all urls from text.

        Args:
            text    (st)
        """
        # return a flat list of all
        if text is None:
            return []
        matches = [r.extract(text) for r in self.processors]
        return list(itertools.chain(*matches))
