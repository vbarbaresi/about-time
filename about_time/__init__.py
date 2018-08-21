VERSION = (1, 0, 0)

__author__ = 'Rogério Sampaio de Almeida'
__email__ = 'rsalmei@gmail.com'
__version__ = '.'.join(map(str, VERSION))

__all__ = ('__author__', '__version__', 'about_time')

from .about_time import about_time