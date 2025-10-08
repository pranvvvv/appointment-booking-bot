from flask import Flask
import pytest

import chatbackend


def test_app_is_flask():
    assert isinstance(chatbackend.app, Flask)
