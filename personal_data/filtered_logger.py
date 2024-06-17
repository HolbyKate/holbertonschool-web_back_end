#!/usr/bin/env python3

import re
"""Function that returns the log message obfuscated"""

def filter_datum(fields, redaction, message, separator):
    """Obfuscate field message"""
    for field in fields:
        pattern = rf'({field}=)([^{separator}]*)'
        message = re.sub(pattern, rf'\1{redaction}', message)
    return message


    if __name__ == "__main__":
        main()