.. The Cut Media documentation master file, created by
   sphinx-quickstart on Fri Sep 12 14:38:03 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to The Cut Media's documentation!
=========================================

The basic aim of this project is to handle uploading and attaching
media, such as images and documents, to Django models. The core of the
project consists of the ``thecut.media.models.MediaContentType``, a
sub-class of ``django.contrib.contenttypes.models.ContentType``, and a
join table which allows a media item (any model whose content type is
``thecut.media.models.MediaContentType``) to be linked with any other
model.


Contents:

.. toctree::
   :maxdepth: 2


Basic usage
-----------

To install this application (whilst in the project's activated virtualenv)::

    pip install git+ssh://git@git.thecut.net.au/thecut-media


Add the ``thecut.media`` and ``thecut.media.mediasources`` to the project's
``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        ...
        'thecut.media',
        'thecut.media.mediasources'
    )


In the project's settings file, define the default media types which
may be attached to objects ::

    MEDIA_DEFAULT_ATTACHED_MEDIA_MODELS =
        'thecut.media.mediasources.models.Image',
        'thecut.media.mediasources.models.Document',
    ]

In the project's settings file, define the thumbnail options::

    THUMBNAIL_BACKEND = 'thecut.media.backends.ThumbnailBackend'

    THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.pil_engine.Engine'

    MEDIA_PREGENERATE_THUMBNAIL_SIZES = [
        # Homepage CTAs
	('960x400', {'crop': 'center'}),
    ]


Development setup
-----------------

There are currently no tests (boo!) which makes getting set up
reasonably straight forward (yay!) To start development on the
thecut-media, clone the project from the project's git repository::

  $ git clone git@git.thecut.net.au:thecut-media

In order to build this documentation, you'll need to install the
development requirements, probably inside a ``virtualenv``::

  $ virtualenv ~/venvs/thecut-media
  $ source ~/venvs/thecut-media/bin/activate
  $ pip install -r requirements-dev.txt
  $ cd docs
  $ make html


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
