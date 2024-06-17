#!/usr/bin/env python3
"""Function that returns the log message obfuscated"""
import re


def filter_datum(fields: list, redaction: str, message: str,
                 separator: str) -> str:
    """Obfuscate field message and return log message"""
    for field in fields:
        pattern = rf'({field}=)([^{separator}]*)'
        message = re.sub(pattern, rf'\1{redaction}', message)
    return message
