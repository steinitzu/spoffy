import json

_jalbum = """
{
  "album_type": "album",
  "artists": [
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/2BTZIqw0ntH9MvilQ3ewNY"
      },
      "href": "https://api.spotify.com/v1/artists/2BTZIqw0ntH9MvilQ3ewNY",
      "id": "2BTZIqw0ntH9MvilQ3ewNY",
      "name": "Cyndi Lauper",
      "type": "artist",
      "uri": "spotify:artist:2BTZIqw0ntH9MvilQ3ewNY"
    }
  ],
  "available_markets": [],
  "copyrights": [
    {
      "text": "(P) 2000 Sony Music Entertainment Inc.",
      "type": "P"
    }
  ],
  "external_ids": {
    "upc": "5099749994324"
  },
  "external_urls": {
    "spotify": "https://open.spotify.com/album/0sNOF9WDwhWunNAHPD3Baj"
  },
  "genres": [],
  "href": "https://api.spotify.com/v1/albums/0sNOF9WDwhWunNAHPD3Baj",
  "id": "0sNOF9WDwhWunNAHPD3Baj",
  "images": [
    {
      "height": 640,
      "url": "https://i.scdn.co/image/b6e762dcce1502ce63eb2c68798843eb2ed53c51",
      "width": 640
    },
    {
      "height": 300,
      "url": "https://i.scdn.co/image/66302ca80395b6be3600d5f0ef69db9e0c43f4f5",
      "width": 300
    },
    {
      "height": 64,
      "url": "https://i.scdn.co/image/e2e8cd6bf776613f9b84d1e4403a8abd51bb7234",
      "width": 64
    }
  ],
  "label": "Epic/Legacy",
  "name": "She's So Unusual",
  "popularity": 0,
  "release_date": "1983",
  "release_date_precision": "year",
  "total_tracks": 13,
  "tracks": {
    "href": "https://api.spotify.com/v1/albums/0sNOF9WDwhWunNAHPD3Baj/tracks?offset=0&limit=50",
    "items": [
      {
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2BTZIqw0ntH9MvilQ3ewNY"
            },
            "href": "https://api.spotify.com/v1/artists/2BTZIqw0ntH9MvilQ3ewNY",
            "id": "2BTZIqw0ntH9MvilQ3ewNY",
            "name": "Cyndi Lauper",
            "type": "artist",
            "uri": "spotify:artist:2BTZIqw0ntH9MvilQ3ewNY"
          }
        ],
        "available_markets": [],
        "disc_number": 1,
        "duration_ms": 305560,
        "explicit": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/track/3f9zqUnrnIq0LANhmnaF0V"
        },
        "href": "https://api.spotify.com/v1/tracks/3f9zqUnrnIq0LANhmnaF0V",
        "id": "3f9zqUnrnIq0LANhmnaF0V",
        "is_local": false,
        "name": "Money Changes Everything",
        "preview_url": null,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:3f9zqUnrnIq0LANhmnaF0V"
      },
      {
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2BTZIqw0ntH9MvilQ3ewNY"
            },
            "href": "https://api.spotify.com/v1/artists/2BTZIqw0ntH9MvilQ3ewNY",
            "id": "2BTZIqw0ntH9MvilQ3ewNY",
            "name": "Cyndi Lauper",
            "type": "artist",
            "uri": "spotify:artist:2BTZIqw0ntH9MvilQ3ewNY"
          }
        ],
        "available_markets": [],
        "disc_number": 1,
        "duration_ms": 238266,
        "explicit": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/track/2joHDtKFVDDyWDHnOxZMAX"
        },
        "href": "https://api.spotify.com/v1/tracks/2joHDtKFVDDyWDHnOxZMAX",
        "id": "2joHDtKFVDDyWDHnOxZMAX",
        "is_local": false,
        "name": "Girls Just Want to Have Fun",
        "preview_url": null,
        "track_number": 2,
        "type": "track",
        "uri": "spotify:track:2joHDtKFVDDyWDHnOxZMAX"
      },
      {
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2BTZIqw0ntH9MvilQ3ewNY"
            },
            "href": "https://api.spotify.com/v1/artists/2BTZIqw0ntH9MvilQ3ewNY",
            "id": "2BTZIqw0ntH9MvilQ3ewNY",
            "name": "Cyndi Lauper",
            "type": "artist",
            "uri": "spotify:artist:2BTZIqw0ntH9MvilQ3ewNY"
          }
        ],
        "available_markets": [],
        "disc_number": 1,
        "duration_ms": 306706,
        "explicit": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6ClztHzretmPHCeiNqR5wD"
        },
        "href": "https://api.spotify.com/v1/tracks/6ClztHzretmPHCeiNqR5wD",
        "id": "6ClztHzretmPHCeiNqR5wD",
        "is_local": false,
        "name": "When You Were Mine",
        "preview_url": null,
        "track_number": 3,
        "type": "track",
        "uri": "spotify:track:6ClztHzretmPHCeiNqR5wD"
      },
      {
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2BTZIqw0ntH9MvilQ3ewNY"
            },
            "href": "https://api.spotify.com/v1/artists/2BTZIqw0ntH9MvilQ3ewNY",
            "id": "2BTZIqw0ntH9MvilQ3ewNY",
            "name": "Cyndi Lauper",
            "type": "artist",
            "uri": "spotify:artist:2BTZIqw0ntH9MvilQ3ewNY"
          }
        ],
        "available_markets": [],
        "disc_number": 1,
        "duration_ms": 241333,
        "explicit": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/track/2tVHvZK4YYzTloSCBPm2tg"
        },
        "href": "https://api.spotify.com/v1/tracks/2tVHvZK4YYzTloSCBPm2tg",
        "id": "2tVHvZK4YYzTloSCBPm2tg",
        "is_local": false,
        "name": "Time After Time",
        "preview_url": null,
        "track_number": 4,
        "type": "track",
        "uri": "spotify:track:2tVHvZK4YYzTloSCBPm2tg"
      },
      {
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2BTZIqw0ntH9MvilQ3ewNY"
            },
            "href": "https://api.spotify.com/v1/artists/2BTZIqw0ntH9MvilQ3ewNY",
            "id": "2BTZIqw0ntH9MvilQ3ewNY",
            "name": "Cyndi Lauper",
            "type": "artist",
            "uri": "spotify:artist:2BTZIqw0ntH9MvilQ3ewNY"
          }
        ],
        "available_markets": [],
        "disc_number": 1,
        "duration_ms": 229266,
        "explicit": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6iLhMDtOr52OVXaZdha5M6"
        },
        "href": "https://api.spotify.com/v1/tracks/6iLhMDtOr52OVXaZdha5M6",
        "id": "6iLhMDtOr52OVXaZdha5M6",
        "is_local": false,
        "name": "She Bop",
        "preview_url": null,
        "track_number": 5,
        "type": "track",
        "uri": "spotify:track:6iLhMDtOr52OVXaZdha5M6"
      },
      {
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2BTZIqw0ntH9MvilQ3ewNY"
            },
            "href": "https://api.spotify.com/v1/artists/2BTZIqw0ntH9MvilQ3ewNY",
            "id": "2BTZIqw0ntH9MvilQ3ewNY",
            "name": "Cyndi Lauper",
            "type": "artist",
            "uri": "spotify:artist:2BTZIqw0ntH9MvilQ3ewNY"
          }
        ],
        "available_markets": [],
        "disc_number": 1,
        "duration_ms": 272840,
        "explicit": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/track/3csiLr2B2wRj4lsExn6jLf"
        },
        "href": "https://api.spotify.com/v1/tracks/3csiLr2B2wRj4lsExn6jLf",
        "id": "3csiLr2B2wRj4lsExn6jLf",
        "is_local": false,
        "name": "All Through the Night",
        "preview_url": null,
        "track_number": 6,
        "type": "track",
        "uri": "spotify:track:3csiLr2B2wRj4lsExn6jLf"
      },
      {
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2BTZIqw0ntH9MvilQ3ewNY"
            },
            "href": "https://api.spotify.com/v1/artists/2BTZIqw0ntH9MvilQ3ewNY",
            "id": "2BTZIqw0ntH9MvilQ3ewNY",
            "name": "Cyndi Lauper",
            "type": "artist",
            "uri": "spotify:artist:2BTZIqw0ntH9MvilQ3ewNY"
          }
        ],
        "available_markets": [],
        "disc_number": 1,
        "duration_ms": 220333,
        "explicit": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/track/4mRAnuBGYsW4WGbpW0QUkp"
        },
        "href": "https://api.spotify.com/v1/tracks/4mRAnuBGYsW4WGbpW0QUkp",
        "id": "4mRAnuBGYsW4WGbpW0QUkp",
        "is_local": false,
        "name": "Witness",
        "preview_url": null,
        "track_number": 7,
        "type": "track",
        "uri": "spotify:track:4mRAnuBGYsW4WGbpW0QUkp"
      },
      {
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2BTZIqw0ntH9MvilQ3ewNY"
            },
            "href": "https://api.spotify.com/v1/artists/2BTZIqw0ntH9MvilQ3ewNY",
            "id": "2BTZIqw0ntH9MvilQ3ewNY",
            "name": "Cyndi Lauper",
            "type": "artist",
            "uri": "spotify:artist:2BTZIqw0ntH9MvilQ3ewNY"
          }
        ],
        "available_markets": [],
        "disc_number": 1,
        "duration_ms": 252626,
        "explicit": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/track/3AIeUnffkLQaUaX1pkHyeD"
        },
        "href": "https://api.spotify.com/v1/tracks/3AIeUnffkLQaUaX1pkHyeD",
        "id": "3AIeUnffkLQaUaX1pkHyeD",
        "is_local": false,
        "name": "I'll Kiss You",
        "preview_url": null,
        "track_number": 8,
        "type": "track",
        "uri": "spotify:track:3AIeUnffkLQaUaX1pkHyeD"
      },
      {
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2BTZIqw0ntH9MvilQ3ewNY"
            },
            "href": "https://api.spotify.com/v1/artists/2BTZIqw0ntH9MvilQ3ewNY",
            "id": "2BTZIqw0ntH9MvilQ3ewNY",
            "name": "Cyndi Lauper",
            "type": "artist",
            "uri": "spotify:artist:2BTZIqw0ntH9MvilQ3ewNY"
          }
        ],
        "available_markets": [],
        "disc_number": 1,
        "duration_ms": 45933,
        "explicit": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/track/53eCpAFNbA9MQNfLilN3CH"
        },
        "href": "https://api.spotify.com/v1/tracks/53eCpAFNbA9MQNfLilN3CH",
        "id": "53eCpAFNbA9MQNfLilN3CH",
        "is_local": false,
        "name": "He's so Unusual",
        "preview_url": null,
        "track_number": 9,
        "type": "track",
        "uri": "spotify:track:53eCpAFNbA9MQNfLilN3CH"
      },
      {
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2BTZIqw0ntH9MvilQ3ewNY"
            },
            "href": "https://api.spotify.com/v1/artists/2BTZIqw0ntH9MvilQ3ewNY",
            "id": "2BTZIqw0ntH9MvilQ3ewNY",
            "name": "Cyndi Lauper",
            "type": "artist",
            "uri": "spotify:artist:2BTZIqw0ntH9MvilQ3ewNY"
          }
        ],
        "available_markets": [],
        "disc_number": 1,
        "duration_ms": 196373,
        "explicit": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/track/51JS0KXziu9U1T8EBdRTUF"
        },
        "href": "https://api.spotify.com/v1/tracks/51JS0KXziu9U1T8EBdRTUF",
        "id": "51JS0KXziu9U1T8EBdRTUF",
        "is_local": false,
        "name": "Yeah Yeah",
        "preview_url": null,
        "track_number": 10,
        "type": "track",
        "uri": "spotify:track:51JS0KXziu9U1T8EBdRTUF"
      },
      {
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2BTZIqw0ntH9MvilQ3ewNY"
            },
            "href": "https://api.spotify.com/v1/artists/2BTZIqw0ntH9MvilQ3ewNY",
            "id": "2BTZIqw0ntH9MvilQ3ewNY",
            "name": "Cyndi Lauper",
            "type": "artist",
            "uri": "spotify:artist:2BTZIqw0ntH9MvilQ3ewNY"
          }
        ],
        "available_markets": [],
        "disc_number": 1,
        "duration_ms": 275560,
        "explicit": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/track/2BGJvRarwOa2kiIGpLjIXT"
        },
        "href": "https://api.spotify.com/v1/tracks/2BGJvRarwOa2kiIGpLjIXT",
        "id": "2BGJvRarwOa2kiIGpLjIXT",
        "is_local": false,
        "name": "Money Changes Everything",
        "preview_url": null,
        "track_number": 11,
        "type": "track",
        "uri": "spotify:track:2BGJvRarwOa2kiIGpLjIXT"
      },
      {
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2BTZIqw0ntH9MvilQ3ewNY"
            },
            "href": "https://api.spotify.com/v1/artists/2BTZIqw0ntH9MvilQ3ewNY",
            "id": "2BTZIqw0ntH9MvilQ3ewNY",
            "name": "Cyndi Lauper",
            "type": "artist",
            "uri": "spotify:artist:2BTZIqw0ntH9MvilQ3ewNY"
          }
        ],
        "available_markets": [],
        "disc_number": 1,
        "duration_ms": 320400,
        "explicit": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/track/5ggatiDTbCIJsUAa7IUP65"
        },
        "href": "https://api.spotify.com/v1/tracks/5ggatiDTbCIJsUAa7IUP65",
        "id": "5ggatiDTbCIJsUAa7IUP65",
        "is_local": false,
        "name": "She Bop - Live",
        "preview_url": null,
        "track_number": 12,
        "type": "track",
        "uri": "spotify:track:5ggatiDTbCIJsUAa7IUP65"
      },
      {
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2BTZIqw0ntH9MvilQ3ewNY"
            },
            "href": "https://api.spotify.com/v1/artists/2BTZIqw0ntH9MvilQ3ewNY",
            "id": "2BTZIqw0ntH9MvilQ3ewNY",
            "name": "Cyndi Lauper",
            "type": "artist",
            "uri": "spotify:artist:2BTZIqw0ntH9MvilQ3ewNY"
          }
        ],
        "available_markets": [],
        "disc_number": 1,
        "duration_ms": 288240,
        "explicit": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/track/5ZBxoa2kBrBah3qNIV4rm7"
        },
        "href": "https://api.spotify.com/v1/tracks/5ZBxoa2kBrBah3qNIV4rm7",
        "id": "5ZBxoa2kBrBah3qNIV4rm7",
        "is_local": false,
        "name": "All Through The Night - Live",
        "preview_url": null,
        "track_number": 13,
        "type": "track",
        "uri": "spotify:track:5ZBxoa2kBrBah3qNIV4rm7"
      }
    ],
    "limit": 50,
    "next": null,
    "offset": 0,
    "previous": null,
    "total": 13
  },
  "type": "album",
  "uri": "spotify:album:0sNOF9WDwhWunNAHPD3Baj"
}
"""

album = json.loads(_jalbum)
