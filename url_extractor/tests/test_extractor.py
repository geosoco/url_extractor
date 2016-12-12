#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from url_extractor.extractor import (
    URLExtractorRegexProcessor,
    URLExtractorMultiRegexProcessor,
    URLExtractor)

"""
URLExtractorRegexProcessor
"""
REGEX_PROCESSOR_EXTRACT_PARAMS = [
        # simple match
        (r"ab", "ab", ["ab"]),
        # match in longer text
        (r"ab", "abc", ["ab"]),
        # no match
        (r"abc", "ab", []),
        # empty text
        (r"ab", "", []),
        # text is None,
        (r"ab", None, []),
        # empty regex
        (r"", "abc", [""] * 4),
        # multiple matches
        (r"a", "appalachian", ["a"] * 4),
]


@pytest.mark.parametrize(
    "regex, text, expected", REGEX_PROCESSOR_EXTRACT_PARAMS)
def test_regex_processor_extract_equal(regex, text, expected):
    proc = URLExtractorRegexProcessor(regex)
    assert proc.extract(text) == expected

"""
URLExtractorMultiRegexProcessor
"""
REGEX_LIST_PROCESSOR_EXTRACT_PARAMS = [
        # simple match
        ([r"a"], "a", ["a"]),
        # simple list
        ([r"a", r"b"], "ab", ["a", "b"]),
        # simple order test
        ([r"a", r"b"], "aab", ["a", "a", "b"]),
        # no match
        ([r"ab"], "a", []),
        # empty text
        ([r"ab"], "", []),
        # text is none
        ([r"ab"], None, []),
        # empty regex
        ([r""], "abc", [""] * 4),
]


@pytest.mark.parametrize(
    "regex_list, text, expected", REGEX_LIST_PROCESSOR_EXTRACT_PARAMS)
def test_regex_list_processor_extract_equal(regex_list, text, expected):
    proc = URLExtractorMultiRegexProcessor(regex_list)
    assert proc.extract(text) == expected
