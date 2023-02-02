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
patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}


def filter_datum(fields: typing.List[str], redaction: str, message: str, separator: str) -> str:
    """
    :param fields: a list of strings representing all fields to obfuscate
    :param redaction: a string representing by what the field will be obfuscated
    :param message: a string representing the log line
    :param separator: a string representing by which character is separating all fields in the log line (message)
    :return: the log message obfuscated
    """
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)
