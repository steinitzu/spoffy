import json

_jartist_with_null_followers = """
{
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/1letzwegdFBTvoyJFSu8zK"
      },
      "followers": {
        "href": null,
        "total": null
      },
      "genres": [],
      "href": "https://api.spotify.com/v1/artists/1letzwegdFBTvoyJFSu8zK",
      "id": "1letzwegdFBTvoyJFSu8zK",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/de7b8a505c46c0366e7adfa9ca99a2b094a553b6",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/298d308873e5d788277e720dd0c8a11f799cad92",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/78ec2da2b382f20fe528cb74e6c3d65564096276",
          "width": 160
        }
      ],
      "name": "Perttu",
      "popularity": 39,
      "type": "artist",
      "uri": "spotify:artist:1letzwegdFBTvoyJFSu8zK"
    }
"""

_jartist = """
{
  "external_urls": {
    "spotify": "https://open.spotify.com/artist/0OdUWJ0sBjDrqHygGUXeCF"
  },
  "followers": {
    "href": null,
    "total": 698044
  },
  "genres": [
    "folk-pop",
    "indie folk",
    "indie pop",
    "indie rock",
    "modern rock",
    "stomp and holler"
  ],
  "href": "https://api.spotify.com/v1/artists/0OdUWJ0sBjDrqHygGUXeCF",
  "id": "0OdUWJ0sBjDrqHygGUXeCF",
  "images": [
    {
      "height": 640,
      "url": "https://i.scdn.co/image/0f9a5013134de288af7d49a962417f4200539b47",
      "width": 640
    },
    {
      "height": 320,
      "url": "https://i.scdn.co/image/8ae35be1043f330173de198c35a49161337e829c",
      "width": 320
    },
    {
      "height": 160,
      "url": "https://i.scdn.co/image/602dd7b3a2ee3f3fd86c6c4f50ab9b5a82e23c59",
      "width": 160
    }
  ],
  "name": "Band of Horses",
  "popularity": 65,
  "type": "artist",
  "uri": "spotify:artist:0OdUWJ0sBjDrqHygGUXeCF"
}
"""

artist = json.loads(_jartist)
artist_with_null_followers = json.loads(_jartist_with_null_followers)
