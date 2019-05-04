Spoffy
######

************
Introduction
************

The IDE friendly sync and async `Spotify API`_ wrapper for python.

.. _`Spotify API`: https://developer.spotify.com/documentation/web-api/


Features include:

* Typed response models
* Async AND sync support
* Built in support for aiohttp and requests (or bring your own http library)
* Support for client credentials and OAuth2 authorization flows

Type hints everywhere
=====================

All API json responses are unmarshalled to typed python objects. (e.g. :py:class:`~spoffy.models.Playlist`)
This gives you excellent code completion in your IDE and makes your code less prone to simple mistakes.


Spoffy is still a thin API wrapper and the response bodies are not reshaped or restructured in any way. You get exactly the data returned from Spotify.

Note: Spotify sometimes includes undocumented attributes in responses, these are also included as attributes on the response object but they're not typed or documented.

Sansio
======

Spoffy is built with sansio principles. In this case that means the choice of underlying http library is merely an implementation detail.
The client can be easily implemented to work with any sync or async http client library. Out of the box, spoffy ships with a sync implementation using `requests`_ and an async implementation using `aiohttp`_

.. _`requests`: https://2.python-requests.org/en/latest/
.. _`aiohttp`: https://aiohttp.readthedocs.io/en/stable/

.. toctree::

   content
