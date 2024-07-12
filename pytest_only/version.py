from importlib import metadata

try:
    __version__ = metadata.version('pytest-only')
except pkg_resources.DistributionNotFound:
    __version__ = 'dev'
