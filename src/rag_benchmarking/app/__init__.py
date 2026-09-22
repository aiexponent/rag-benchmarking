from importlib.metadata import PackageNotFoundError, version

__all__ = [
    "__version__",
]

try:
    __version__ = version("rag-benchmarking")
except PackageNotFoundError:  # running from a source tree, not installed
    __version__ = "0.0.0+local"
