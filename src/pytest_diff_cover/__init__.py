"""Report diff coverage in pytest"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pytest-diff-cover")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Talley Lambert"
__email__ = "talley.lambert@gmail.com"
