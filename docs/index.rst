spoffy
======

The IDE friendly sync and async `Spotify API`_ wrapper for python.

.. _`Spotify API`: https://developer.spotify.com/documentation/web-api/


Features include:

* Typed response models
* Async AND sync support
* Built in support for aiohttp and requests (or bring your own http library)
* Support for client credentials and OAuth2 authorization flows

Type hints everywhere
---------------------

All API json responses are unmarshalled to typed python objects. (e.g. :py:class:`~spoffy.models.Playlist`)
This gives you excellent code completion in your IDE and makes your code less prone to simple mistakes.


Spoffy is still a thin API wrapper and the response bodies are not reshaped or restructured in any way. You get exactly the data returned from Spotify.

Note: Spotify sometimes includes undocumented attributes in responses, these are also included as attributes on the response object but they're not typed or documented.

Sansio
------

Spoffy is built with sansio principles. In this case that means the choice of underlying http library is merely an implementation detail.
The client can be easily implemented to work with any sync or async http client library. Out of the box, spoffy ships with a sync implementation using `requests`_ and an async implementation using `aiohttp`_

.. _`requests`: https://2.python-requests.org/en/latest/
.. _`aiohttp`: https://aiohttp.readthedocs.io/en/stable/

Usage
=====

The Spotify wrapper comes in two flavours :py:class:`~spoffy.SyncSpotify` to use with a synchronous http library such as requests and :py:class:`~spoffy.AsyncSpotify` to use async/await keywords with an async http library such as aiohttp.
The wrapper takes in a client as an argument, this is the part that generates http requests and sends them to the spotify api. To implement your own client use the :py:class:`~spoffy.AsyncClient` or :py:class:`~spoffy.SyncClient` as a base respectively, or use the one of the built in clients: :py:class:`~spoffy.io.requests.RequestsClient` or :py:class:`~spoffy.io.aiohttp.AioHttpClient`

This is how you instantiate the spotify wrapper with the requests client:

.. code-block:: python3

   from spoffy import SyncSpotify
   from spoffy.io.requests import RequestsClient

   spotify = SyncSpotify(RequestsClient(...))

   # Or use the factory function, this is equivalent

   from spoffy.io.requests import make_spotify

   spotify = make_spotify(...)


This is how you use it with the aiohttp client:

.. code-block:: python3

   import aiohttp
   from spoffy import AsyncSpotify
   from spoffy.io.aiohttp import AioHttpclient

   ...

   async with aiohttp.ClientSession() as session:
       spotify = SyncSpotify(AioHttpClient(session=session))

   # Or use the factory function, this is equivalent

   from spoffy.io.aiohttp import make_spotify

   async with aiohttp.ClientSession() as session:
       spotify = make_spotify(session=session)


Quickstart
==========

To start using the API you must first create a client ID and client secret by going to https://developer.spotify.com/dashboard/applications , log in with your spotify account and click "Create a client ID" and go through the steps to register your app.

Once you have your app set up you can access the public API using client credentials authentication.

Note: Spoffy does not have dependencies on any http client libraries, so you must install your preferred library yourself

Use with requests
-----------------

.. code-block::

   pip install requests

.. literalinclude:: /../examples/usewithrequests.py
   :language: python3

Use with AIOHTTP
----------------
.. code-block::

   pip install aiohttp

.. literalinclude:: /../examples/usewithaiohttp.py
   :language: python3


Authentication
==============


Client credentials
------------------

Client credentials tokens can be created without any user interaction and allow access to public spotify data.
Here's an example of how to use it with the requests client

.. literalinclude:: /../examples/clientauth.py
   :language: python

OAuth2 login
------------

Spoffy implements the authorization code login flow. This is described in great detail in `Spotify's Authorization guide`_

.. _`Spotify's Authorization guide`: https://developer.spotify.com/documentation/general/guides/authorization-guide/

Here is a simple example using flask to implement this oauth flow in a web backend and print the user's all time top artist.

First you will need to create an app ID and secret at https://developer.spotify.com/dashboard/ and set your redirect URI to http://localhost:5000/callback (if running your app at a different port/hostname substitute accordingly).

.. literalinclude:: /../examples/flaskauth.py
   :language: python


Refreshing an access token
--------------------------

When you get a token through the oauth login the access token expires after one hour. You also get a refresh token that can be used to reauthorize with the spotify api without the user having to log in again.

If you already have an authorized user on your Spoffy client, refreshing is simple:

.. code-block:: python

   spotify.auth.refresh_authorzation()

If you have a refresh token from somewhere else, simply pass a refresh token explicitly

.. code-block:: python

   s = make_spotify(client_id='my_client_id', client_secret='my_client_secret')
   s.auth.refresh_authorization('my_refresh_token')

If you have a :py:class:`~spoffy.models.UserToken` object from a previous session

.. code-block:: python

   s = make_spotify(
       client_id='my_client_id',
       client_secret='my_client_secret',
       token=my_token_object
   )
   s.auth.refresh_authorization()


Install
=======

.. code-block::

   pip install spoffy

Due the use of typehints and async/await keywords, only python3.6 and up are supported


API Reference
=============

IO Implementations
------------------

Requests
--------

.. automodule:: spoffy.io.requests
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:

AIOhttp
--------

.. automodule:: spoffy.io.aiohttp
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:

.. module:: spoffy

Spotify wrapper
---------------

Sync and async spotify API wrappers that wrap a client instance and expose the spotify api organized into individual modules

.. autoclass:: SyncSpotify
   :members:
   :noindex:

.. autoclass:: AsyncSpotify
   :members:
   :noindex:

Client base
-----------

.. autoclass:: SyncClient
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:

.. _asynclient-label:

.. autoclass:: AsyncClient
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:

.. autoclass:: ClientCommon
   :members:
   :undoc-members:
   :noindex:

Exceptions
----------

.. autoexception:: SpotifyException
   :members:
   :noindex:

.. autoexception:: SpotifyUnauthorized
   :members:
   :noindex:

.. autoexception:: SpotifyPremiumRequired
   :members:
   :noindex:

Sync API modules
----------------

.. module:: spoffy.modules.modules

.. autoclass:: Auth
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:

.. autoclass:: Albums
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:

.. autoclass:: Artists
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:

.. autoclass:: Library
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:

.. autoclass:: Player
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:

.. autoclass:: Playlists
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:

.. autoclass:: Tracks
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:

.. autoclass:: Search
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:

.. autoclass:: Users
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:


Async API modules
-----------------


.. autoclass:: AsyncAuth
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:

.. autoclass:: AsyncAlbums
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:

.. autoclass:: AsyncArtists
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:

.. autoclass:: AsyncLibrary
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:

.. autoclass:: AsyncPlayer
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:

.. autoclass:: AsyncPlaylists
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:

.. autoclass:: AsyncTracks
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:

.. autoclass:: AsyncSearch
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:

.. autoclass:: AsyncUsers
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:
   :noindex:


Object model
------------

.. automodule:: spoffy.models
   :members:
   :undoc-members:
   :inherited-members:
   :noindex:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
