import json

_jalbums_relinked = """
{
  "href": "https://api.spotify.com/v1/artists/1vCWHaC5f2uS3yhpwWbIA6/albums?offset=0&limit=5&include_groups=album,single,compilation,appears_on&market=ES",
  "items": [
    {
      "album_group": "album",
      "album_type": "album",
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/1vCWHaC5f2uS3yhpwWbIA6"
          },
          "href": "https://api.spotify.com/v1/artists/1vCWHaC5f2uS3yhpwWbIA6",
          "id": "1vCWHaC5f2uS3yhpwWbIA6",
          "name": "Avicii",
          "type": "artist",
          "uri": "spotify:artist:1vCWHaC5f2uS3yhpwWbIA6"
        }
      ],
      "external_urls": {
        "spotify": "https://open.spotify.com/album/7dqftJ3kas6D0VAdmt3k3V"
      },
      "href": "https://api.spotify.com/v1/albums/7dqftJ3kas6D0VAdmt3k3V",
      "id": "7dqftJ3kas6D0VAdmt3k3V",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/a76f75493d039938b5dcfabbd5a6c1081f270a6c",
          "width": 640
        },
        {
          "height": 300,
          "url": "https://i.scdn.co/image/1685a59f97e828e423a20ba080754c8d58466756",
          "width": 300
        },
        {
          "height": 64,
          "url": "https://i.scdn.co/image/95191136789abd43fc7ad7b4ea5526eca2986c26",
          "width": 64
        }
      ],
      "name": "Stories",
      "release_date": "2015-10-02",
      "release_date_precision": "day",
      "total_tracks": 14,
      "type": "album",
      "uri": "spotify:album:7dqftJ3kas6D0VAdmt3k3V"
    },
    {
      "album_group": "album",
      "album_type": "album",
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/1vCWHaC5f2uS3yhpwWbIA6"
          },
          "href": "https://api.spotify.com/v1/artists/1vCWHaC5f2uS3yhpwWbIA6",
          "id": "1vCWHaC5f2uS3yhpwWbIA6",
          "name": "Avicii",
          "type": "artist",
          "uri": "spotify:artist:1vCWHaC5f2uS3yhpwWbIA6"
        }
      ],
      "external_urls": {
        "spotify": "https://open.spotify.com/album/0h2knr6qpiAq0tV5ri5JMF"
      },
      "href": "https://api.spotify.com/v1/albums/0h2knr6qpiAq0tV5ri5JMF",
      "id": "0h2knr6qpiAq0tV5ri5JMF",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/1da50cf44c25f8aad1b39ab640dff5137ee72dbb",
          "width": 640
        },
        {
          "height": 300,
          "url": "https://i.scdn.co/image/baca6767c796817bded72c60f4a1b67f28cc75da",
          "width": 300
        },
        {
          "height": 64,
          "url": "https://i.scdn.co/image/f8dc9e20bf7dd876bd646ce472c345a0fa9dfae3",
          "width": 64
        }
      ],
      "name": "The Days / Nights",
      "release_date": "2014-01-01",
      "release_date_precision": "day",
      "total_tracks": 4,
      "type": "album",
      "uri": "spotify:album:0h2knr6qpiAq0tV5ri5JMF"
    },
    {
      "album_group": "album",
      "album_type": "album",
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/1vCWHaC5f2uS3yhpwWbIA6"
          },
          "href": "https://api.spotify.com/v1/artists/1vCWHaC5f2uS3yhpwWbIA6",
          "id": "1vCWHaC5f2uS3yhpwWbIA6",
          "name": "Avicii",
          "type": "artist",
          "uri": "spotify:artist:1vCWHaC5f2uS3yhpwWbIA6"
        }
      ],
      "external_urls": {
        "spotify": "https://open.spotify.com/album/0ignCov9foaLxuqND5GMtl"
      },
      "href": "https://api.spotify.com/v1/albums/0ignCov9foaLxuqND5GMtl",
      "id": "0ignCov9foaLxuqND5GMtl",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/288730e58599d056b32a3934a0d519e6f1152265",
          "width": 640
        },
        {
          "height": 300,
          "url": "https://i.scdn.co/image/141c2d2604305a3694ed9ef7d3a94e4c9e5f492a",
          "width": 300
        },
        {
          "height": 64,
          "url": "https://i.scdn.co/image/c82fb92d61e5d25c47f4c819bd669944ee51abfc",
          "width": 64
        }
      ],
      "name": "True: Avicii By Avicii",
      "release_date": "2014-01-01",
      "release_date_precision": "day",
      "total_tracks": 9,
      "type": "album",
      "uri": "spotify:album:0ignCov9foaLxuqND5GMtl"
    },
    {
      "album_group": "album",
      "album_type": "album",
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/1vCWHaC5f2uS3yhpwWbIA6"
          },
          "href": "https://api.spotify.com/v1/artists/1vCWHaC5f2uS3yhpwWbIA6",
          "id": "1vCWHaC5f2uS3yhpwWbIA6",
          "name": "Avicii",
          "type": "artist",
          "uri": "spotify:artist:1vCWHaC5f2uS3yhpwWbIA6"
        }
      ],
      "external_urls": {
        "spotify": "https://open.spotify.com/album/1s9tU91VJt4sU5owi29GD3"
      },
      "href": "https://api.spotify.com/v1/albums/1s9tU91VJt4sU5owi29GD3",
      "id": "1s9tU91VJt4sU5owi29GD3",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/98c5699709d8c2497f34a177d159e1b1733f25bb",
          "width": 640
        },
        {
          "height": 300,
          "url": "https://i.scdn.co/image/ccacb3b04352cc4ac7230aa02779171943717a10",
          "width": 300
        },
        {
          "height": 64,
          "url": "https://i.scdn.co/image/7dabeff1e09d78b1e96d88be2b5509f00ef6ae5e",
          "width": 64
        }
      ],
      "name": "True",
      "release_date": "2013-01-01",
      "release_date_precision": "day",
      "total_tracks": 12,
      "type": "album",
      "uri": "spotify:album:1s9tU91VJt4sU5owi29GD3"
    },
    {
      "album_group": "single",
      "album_type": "single",
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/1vCWHaC5f2uS3yhpwWbIA6"
          },
          "href": "https://api.spotify.com/v1/artists/1vCWHaC5f2uS3yhpwWbIA6",
          "id": "1vCWHaC5f2uS3yhpwWbIA6",
          "name": "Avicii",
          "type": "artist",
          "uri": "spotify:artist:1vCWHaC5f2uS3yhpwWbIA6"
        }
      ],
      "external_urls": {
        "spotify": "https://open.spotify.com/album/7Jx7doYIXITyR2LQB0Hvbc"
      },
      "href": "https://api.spotify.com/v1/albums/7Jx7doYIXITyR2LQB0Hvbc",
      "id": "7Jx7doYIXITyR2LQB0Hvbc",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/2cc4d3aa28ebae67ed93040315342ca43aa7080d",
          "width": 640
        },
        {
          "height": 300,
          "url": "https://i.scdn.co/image/38acfd3d2517343bc564d3093d54982aa3dc155c",
          "width": 300
        },
        {
          "height": 64,
          "url": "https://i.scdn.co/image/b375ef37db875d690965f1afb969cc2c86e21219",
          "width": 64
        }
      ],
      "name": "SOS",
      "release_date": "2019-04-10",
      "release_date_precision": "day",
      "total_tracks": 1,
      "type": "album",
      "uri": "spotify:album:7Jx7doYIXITyR2LQB0Hvbc"
    }
  ],
  "limit": 5,
  "next": "https://api.spotify.com/v1/artists/1vCWHaC5f2uS3yhpwWbIA6/albums?offset=5&limit=5&include_groups=album,single,compilation,appears_on&market=ES",
  "offset": 0,
  "previous": null,
  "total": 382
}
"""

artist_albums_relinked = json.loads(_jalbums_relinked)
