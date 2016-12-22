=======================
Welcome to thecut-media
=======================

..
  .. image:: https://travis-ci.org/thecut/thecut-media.svg
      :target: https://travis-ci.org/thecut/thecut-media

  .. image:: https://codecov.io/github/thecut/thecut-media/coverage.svg
      :target: https://codecov.io/github/thecut/thecut-media

  .. image:: https://readthedocs.org/projects/thecut-media/badge/?version=latest
      :target: http://thecut-media.readthedocs.io/en/latest/?badge=latest
      :alt: Documentation Status

A reusable application.


Documentation
-------------

This application requires ``thecut.ordering`` and ``thecut.publishing``.


If pgmagick is to be used as thumbnail engine then the libgraphicsmagick++-dev
and libboost-python-dev packages need to be installed before installing
'pgmagick>=0.3.2' using pip.


To install this application (whilst in the project's activated virtualenv)::
    pip install git+ssh://git@git.thecut.net.au/thecut-media


Add the ``thecut.media`` and ``thecut.media.mediasources`` to the project's
``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        ...
        'thecut.media',
        'thecut.media.mediasources'
    )


Add ``MEDIA_SOURCES`` and ``THUMBNAIL_ENGINE`` setting::

    MEDIA_SOURCES = [
        'thecut.media.mediasources.models.Image',
        'thecut.media.mediasources.models.Document',
    ]
    THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.pil_engine.Engine'


For exif/xmp data extraction, the pyexiftool package is required. This can be
installed (whist in the project's activated virtualenv) using pip:
    pip install git+https://github.com/smarnach/pyexiftool.git

The exiftool package also needs to be installed on the system:
    sudo apt-get install libimage-exiftool-perl

Credits
-------

See ``AUTHORS.rst``.
