#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This regex is a modified version of the @cowboy version from
Mathias Bynen's URL regex comparison:
https://mathiasbynens.be/demo/url-regex

After brief modification for python, it seemed to grant the best matches
for my project at the time (finding urls in text & markdown),
though I made a few modifications to disallow urls to end with commas,
dots, closing brackets, and closing parens. I also disallowed the
parens and brackets within a URL, which will break for some people.
However, the domain suffix list here alone is probably already broken
for many cases.

"""

RE_URL = (
    r"(?:\b[a-z\d.-]+://[^<>\s\)\]]+|\b(?:(?:(?:[^\s!@#$%^&\*(\)_=+[\]{}\|;:"
    r"\'\",\.<>/?]+)\.)+(?:ac|ad|aero|ae|af|ag|ai|al|am|an|ao|aq|arpa|ar|"
    r"asia|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|biz|bi|bj|bm|bn|bo|br|bs|"
    r"bt|bv|bw|by|bz|cat|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|coop|com|co|cr|cu|"
    r"cv|cx|cy|cz|de|dj|dk|dm|do|dz|ec|edu|ee|eg|er|es|et|eu|fi|fj|fk|fm|fo|"
    r"fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gov|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|"
    r"hn|hr|ht|hu|id|ie|il|im|info|int|in|io|iq|ir|is|it|je|jm|jobs|jo|jp|"
    r"ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|"
    r"mc|md|me|mg|mh|mil|mk|ml|mm|mn|mobi|mo|mp|mq|mr|ms|mt|museum|mu|mv|mw|"
    r"mx|my|mz|name|na|nc|net|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|org|pa|pe|pf|"
    r"pg|ph|pk|pl|pm|pn|pro|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|"
    r"sg|sh|si|sj|sk|sl|sm|sn|so|sr|st|su|sv|sy|sz|tc|td|tel|tf|tg|th|tj|tk|"
    r"tl|tm|tn|to|tp|travel|tr|tt|tv|tw|tz|ua|ug|uk|um|us|uy|uz|va|vc|ve|vg|"
    r"vi|vn|vu|wf|ws|xn--0zwm56d|xn--11b5bs3a9aj6g|xn--80akhbyknj4f|"
    r"xn--9t4b11yi5a|xn--deba0ad|xn--g6w251d|xn--hgbk6aj7f53bba|"
    r"xn--hlcj6aya9esc7a|xn--jxalpdlp|xn--kgbechtv|xn--zckzah|ye|yt|yu|za|"
    r"zm|zw)|(?:(?:[0-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(?:[0-9]|"
    r"[1-9]\d|1\d{2}|2[0-4]\d|25[0-5]))(?:[;/][^#?<>\s\)\]]*)?"
    r"(?:\?[^#<>\s]*)?(?:#[^<>\s]*)?(?!\w))(?<![,\)\]\.])"
)