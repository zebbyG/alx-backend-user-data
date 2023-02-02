#!/usr/bin/env python3
"""A module for filtering logs.
"""
import re
import logging
from typing import List
"""
required inputs
"""
patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    :param fields: a list of strings representing all fields to obfuscate
    :param redaction: a string representing by what the field will be obfuscated
    :param message: a string representing the log line
    :param separator: a string representing by which character is separating all fields in the log line (message)
    :return: the log message obfuscated
    """
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        initializing class
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        formats a LogRecord.
        """
        message = super(RedactingFormatter, self).format(record)
        txt = filter_datum(self.fields, self.REDACTION, message, self.SEPARATOR)
        return txt
