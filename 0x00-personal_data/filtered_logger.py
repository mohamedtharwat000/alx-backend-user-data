#!/usr/bin/env python3
"""This module contains the User class."""

import re

def filter_datum(fields, redaction, message, separator):
    return re.sub(r'(?<=(?:^|{0}))(?:(?:{1})(?={0}))|(?:^|{0})(?:{1})(?={0}|$)'.format(re.escape(separator), '|'.join(map(re.escape, fields))), redaction, message)
