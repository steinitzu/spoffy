spoffy
======

The IDE friendly sync and async `Spotify API`_ wrapper for python.

.. _`Spotify API`: https://developer.spotify.com/documentation/web-api/


Features include:

* Typed response models
* Async AND sync support
* Support for client credentials and OAuth2 authorization flows

Type hints everywhere
---------------------

All API json responses are converted to typed python objects.
This gives you excellent code completion in your IDE and makes your code less prone to simple mistakes.

This is still a thin API wrapper and the response bodies are not reshaped or restructured in any way. You get exactly the data returned from Spotify.

Sansio
------

Spoffy is built with sansio principles. In this case that means the choice of underlying http library is merely an implementation detail.
The client can be easily implemented to work with any sync or async http client library. Out of the box, spoffy ships with a sync implementation using `requests`_ and an async implementation using `aiohttp`_

.. _`requests`: https://2.python-requests.org/en/latest/
.. _`aiohttp`: https://aiohttp.readthedocs.io/en/stable/


Quickstart
==========

To start using the API you must first create a client ID and client secret by going to https://developer.spotify.com/dashboard/applications , log in with your spotify account and click "Create a client ID" and go through the steps to register your app.

Once you have your app set up you can access the public API using client credentials authentication.

Use with requests
-----------------

.. literalinclude:: /../examples/usewithrequests.py
   :language: python

Use with AIOHTTP
----------------
.. literalinclude:: /../examples/usewithaiohttp.py
   :language: python


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

------------------
IO Implementations
------------------

Requests
--------

.. automodule:: spoffy.io.requests
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:

AIOhttp
--------

.. automodule:: spoffy.io.aiohttp
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:

.. module:: spoffy

Spotify wrapper
---------------

Sync and async spotify API wrappers that wrap a client instance and expose the spotify api organized into individual modules

.. autoclass:: SyncSpotify
   :members:

.. autoclass:: AsyncSpotify
   :members:




Client base
-----------

.. autoclass:: SyncClient
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:

.. autoclass:: AsyncClient
   :members:
   :inherited-members:
   :show-inheritance:
   :undoc-members:

.. autoclass:: ClientCommon
   :members:
   :undoc-members:

Exceptions
----------

.. autoexception:: SpotifyException
   :members:

.. autoexception:: SpotifyUnauthorized
   :members:

.. autoexception:: SpotifyPremiumRequired
   :members:

API modules
-----------

.. automodule:: spoffy.modules.modules
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

.. automodule:: spoffy.modules.apimodule
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:


Object model
------------

.. automodule:: spoffy.models
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

.. automodule:: spoffy.models.core
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

.. automodule:: spoffy.models.audiofeatures
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

.. automodule:: spoffy.models.collections
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

.. automodule:: spoffy.models.image
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

.. automodule:: spoffy.models.library
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

.. automodule:: spoffy.models.paging
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

.. automodule:: spoffy.models.personalization
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:


.. automodule:: spoffy.models.player
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

.. automodule:: spoffy.models.playlists
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

.. automodule:: spoffy.models.search
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

.. automodule:: spoffy.models.token
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

.. automodule:: spoffy.models.users
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
