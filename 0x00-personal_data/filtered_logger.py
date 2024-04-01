#!/usr/bin/env python3
"""This module contains the User class."""


import re
from typing import List

def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    return re.sub(r'(?<=(?:^|{0}))(?:(?:{1})(?={0}))|'
                  r'(?:^|{0})(?:{1})(?={0}|$)'.format(
                      re.escape(separator),
                      '|'.join(map(re.escape, fields))),
                  redaction, message)
