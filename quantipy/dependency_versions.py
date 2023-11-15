import pandas as pd
from pandas.util.version import Version
from scipy.version import version as scipy_version

__pandas_version_parsed__ = Version(pd.__version__)

__scipy_version_parsed__ = Version(scipy_version)
