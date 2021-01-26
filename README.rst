Base Repr
=========
This module is for expressing Python data in the desired base system, such as 62 base system.

Introduce
---------
It supports up to 62 base systems that can be expressed only with digits and case sensitive alphabets.

This module was developed to make it easier to use for URLs or other data fields requiring length restrictions by expressing large numbers or hash values to a shorter length.

You can also encode strings or decode encoded strings. (Strings are not guaranteed to be shortened.)

It started with inspiration from ``base62`` and ``numpy.base_repr`` aim to be universally used in multiple systems such as ``base36`` in systems where ``base62`` cannot be applied because it is case-insensitive systems.

Installing Base Repr
--------------------
Base Repr is available on PyPI:

.. code-block:: bash

    $ python -m pip install base-repr

Base Repr supports Python 3.6+

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

You can also inherit a class to create and use the desired base system.

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
