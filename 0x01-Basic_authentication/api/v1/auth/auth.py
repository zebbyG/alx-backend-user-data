#!/usr/bin/env python3
"""
Auth class
"""
from flask import request
from typing import List, TypeVar

"""
required module
"""


class Auth:
    """
    class Auth to manage API authentication
    """
    def require_auth(path: str, excluded_paths: List[str]) -> bool:
        """
        :return: False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        :return: None
        """
        return str(None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        :param request:
        :return:
        """
        return None
