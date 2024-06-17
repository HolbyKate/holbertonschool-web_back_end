#!/usr/bin/env python3

import re
"""Function that returns the log message obfuscated"""

def filter_datum(fields, redaction, message, separator):
    for field in fields:
        pattern = r'|'.join(field)(separator)
        message = re.sub(pattern, (redaction), (message))
    return pattern