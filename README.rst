Base Representation
===================
This module is for represent Python data in the desired base system, like Base36 and Base62.

Introduce
---------
This supports from 2 base systems to 62 base systems that can be expressed only with digits and case sensitive alphabets.

This module was developed to make it easier to use for URLs or other data fields requiring length restrictions by expressing large numbers or hash values to a shorter length.

You can also encode strings or decode encoded strings. (Strings are not guaranteed to be shortened.)

This started with inspiration from ``base62`` idea and ``numpy.base_repr`` library and aim to be universally used in multiple systems such as ``Base36`` in systems where ``Base62`` cannot be applied because it is case-insensitive systems.

.. image:: https://img.shields.io/pypi/v/base-repr
    :target: https://pypi.org/project/base-repr/

.. image:: https://img.shields.io/pypi/wheel/base-repr
    :target: https://pypi.org/project/base-repr/

.. image:: https://img.shields.io/pypi/l/base-repr
    :target: https://pypi.org/project/base-repr/

.. image:: https://img.shields.io/pypi/pyversions/base-repr
    :target: https://pypi.org/project/base-repr/

.. image:: https://img.shields.io/pypi/dm/base-repr
    :target: https://pypi.org/project/base-repr/

Installing Base Representation
------------------------------
Base Representation is available on PyPI:

.. code-block:: bash

    $ python -m pip install base-repr

Base Representation is tested on Python 3.6+

How to use
----------
Using functions
"""""""""""""""
.. code-block:: python

    >>> import base_repr
    # Number to string representation
    >>> base_repr.int_to_repr(1234, base=62)
    'Ju'
    >>> base_repr.repr_to_int('Ju', base=62)
    1234

    # Bytes to string representation
    # bytes([1, 2, 3, 4]) == b'\x01\x02\x03\x04'
    >>> base_repr.bytes_to_repr(bytes([1, 2, 3, 4]), base=62, byteorder='little')
    '4YPMP'
    >>> base_repr.repr_to_bytes('4YPMP', base=62, byteorder='little')
    b'\x01\x02\x03\x04'

    # sha256
    import hashlib
    # hashlib.sha256(b'Hello World!').hexdigest() == '7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069'
    >>> base_repr.bytes_to_repr(hashlib.sha256(b'Hello World!').digest(), base=62, byteorder='little')
    'P20z9unz25ZdkS9kKi65j9Rb8jqP5knHG08sDpvsQDn'

    # string
    >>> base_repr.str_to_repr('Hello', base=62, byteorder='little', encoding='utf-8')
    '8QMwioi'
    >>> base_repr.repr_to_str('8QMwioi', base=62, byteorder='little', encoding='utf-8')
    'Hello'

    # simple wrapper to union above 3 functions for data type int, bytes and str.
    >>> base_repr.to_repr('int or bytes or str', base=62)
    '3xDXjUL88hX1Dq95EbXKCI7cOP'


Using class
"""""""""""
You can use classes to reduce repetitive parameters.

.. code-block:: python

    >>> from base_repr import Base62
    >>> base62 = Base62(byteorder='little', encoding='utf-8')
    >>> base62.bytes_to_repr(bytes([1, 2, 3, 4]))
    '4YPMP'
    >>> base62.repr_to_bytes('4YPMP')
    b'\x01\x02\x03\x04'
    >>> base62.to_repr('int or bytes or str')
    '3xDXjUL88hX1Dq95EbXKCI7cOP'

You can also inherit a base class to create your own desired base system simply.

.. code-block:: python

    >>> from base_repr import BaseRepr
    >>> class Base36(BaseRepr):
    ... def __init__(self, padding: int = 0, byteorder: str = sys.byteorder, encoding: str = 'utf-8'):
    ...     super().__init__(36, padding, byteorder, encoding)

    >>> base = Base36(padding=0, byteorder='big', encoding='utf-8')
    >>> base.int_to_repr(1234)
    'YA'
    >>> base.repr_to_int('YA')
    1234

``Base62`` and ``Base36`` are already defined in module and ready to use.
