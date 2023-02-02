#!/usr/bin/env python3
"""
Regex-ing
"""
import re
import typing
"""
required module
"""
            # 0.Regex-ing task


def filter_datum(fields: typing.List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    :param fields: a list of strings representing all fields to obfuscate
    :param redaction: a string representing by what the field will be obfuscated
    :param message: a string representing the log line
    :param separator: a string representing by which character is separating all fields in the log line (message)
    :return: the log message obfuscated
    """
    for f in fields:
        message = re.sub(f+'=.*?'+separator,
                         f+'='+redaction+separator, message)
        return message

# task 1: Log Formatter
