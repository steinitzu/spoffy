import json

_jtrack = """
{
  "album": {
    "album_type": "single",
    "artists": [
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/6sFIWsNpZYqfjUpaCgueju"
        },
        "href": "https://api.spotify.com/v1/artists/6sFIWsNpZYqfjUpaCgueju",
        "id": "6sFIWsNpZYqfjUpaCgueju",
        "name": "Carly Rae Jepsen",
        "type": "artist",
        "uri": "spotify:artist:6sFIWsNpZYqfjUpaCgueju"
      }
    ],
    "external_urls": {
      "spotify": "https://open.spotify.com/album/0tGPJ0bkWOUmH7MEOR77qc"
    },
    "href": "https://api.spotify.com/v1/albums/0tGPJ0bkWOUmH7MEOR77qc",
    "id": "0tGPJ0bkWOUmH7MEOR77qc",
    "images": [
      {
        "height": 640,
        "url": "https://i.scdn.co/image/966ade7a8c43b72faa53822b74a899c675aaafee",
        "width": 640
      },
      {
        "height": 300,
        "url": "https://i.scdn.co/image/107819f5dc557d5d0a4b216781c6ec1b2f3c5ab2",
        "width": 300
      },
      {
        "height": 64,
        "url": "https://i.scdn.co/image/5a73a056d0af707b4119a883d87285feda543fbb",
        "width": 64
      }
    ],
    "name": "Cut To The Feeling",
    "release_date": "2017-05-26",
    "release_date_precision": "day",
    "total_tracks": 1,
    "type": "album",
    "uri": "spotify:album:0tGPJ0bkWOUmH7MEOR77qc"
  },
  "artists": [
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/6sFIWsNpZYqfjUpaCgueju"
      },
      "href": "https://api.spotify.com/v1/artists/6sFIWsNpZYqfjUpaCgueju",
      "id": "6sFIWsNpZYqfjUpaCgueju",
      "name": "Carly Rae Jepsen",
      "type": "artist",
      "uri": "spotify:artist:6sFIWsNpZYqfjUpaCgueju"
    }
  ],
  "disc_number": 1,
  "duration_ms": 207959,
  "explicit": false,
  "external_ids": {
    "isrc": "USUM71703861"
  },
  "external_urls": {
    "spotify": "https://open.spotify.com/track/6EJiVf7U0p1BBfs0qqeb1f"
  },
  "href": "https://api.spotify.com/v1/tracks/6EJiVf7U0p1BBfs0qqeb1f",
  "id": "6EJiVf7U0p1BBfs0qqeb1f",
  "is_local": false,
  "is_playable": true,
  "linked_from": {
    "external_urls": {
      "spotify": "https://open.spotify.com/track/11dFghVXANMlKmJXsNCbNl"
    },
    "href": "https://api.spotify.com/v1/tracks/11dFghVXANMlKmJXsNCbNl",
    "id": "11dFghVXANMlKmJXsNCbNl",
    "type": "track",
    "uri": "spotify:track:11dFghVXANMlKmJXsNCbNl"
  },
  "name": "Cut To The Feeling",
  "popularity": 70,
  "preview_url": "https://p.scdn.co/mp3-preview/229bb6a4c7011158cc7e1aff11957e274dc05e84?cid=774b29d4f13844c495f206cafdad9c86",
  "track_number": 1,
  "type": "track",
  "uri": "spotify:track:6EJiVf7U0p1BBfs0qqeb1f"
}
"""

_jtrackmarkets = """
{
  "album": {
    "album_type": "album",
    "artists": [
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/4UHzJP2iKVf0RhKIv7ZE2l"
        },
        "href": "https://api.spotify.com/v1/artists/4UHzJP2iKVf0RhKIv7ZE2l",
        "id": "4UHzJP2iKVf0RhKIv7ZE2l",
        "name": "Black Moth Super Rainbow",
        "type": "artist",
        "uri": "spotify:artist:4UHzJP2iKVf0RhKIv7ZE2l"
      }
    ],
    "available_markets": [
      "AD",
      "AE",
      "AR",
      "AT",
      "AU",
      "BE",
      "BG",
      "BH",
      "BO",
      "BR",
      "CA",
      "CH",
      "CL",
      "CO",
      "CR",
      "CY",
      "CZ",
      "DE",
      "DK",
      "DO",
      "DZ",
      "EC",
      "EE",
      "EG",
      "ES",
      "FI",
      "FR",
      "GB",
      "GR",
      "GT",
      "HK",
      "HN",
      "HU",
      "ID",
      "IE",
      "IL",
      "IN",
      "IS",
      "IT",
      "JO",
      "JP",
      "KW",
      "LB",
      "LI",
      "LT",
      "LU",
      "LV",
      "MA",
      "MC",
      "MT",
      "MX",
      "MY",
      "NI",
      "NL",
      "NO",
      "NZ",
      "OM",
      "PA",
      "PE",
      "PH",
      "PL",
      "PS",
      "PT",
      "PY",
      "QA",
      "RO",
      "SA",
      "SE",
      "SG",
      "SK",
      "SV",
      "TH",
      "TN",
      "TR",
      "TW",
      "US",
      "UY",
      "VN",
      "ZA"
    ],
    "external_urls": {
      "spotify": "https://open.spotify.com/album/6Ey14uD5ZqvAX19FVEHr6Q"
    },
    "href": "https://api.spotify.com/v1/albums/6Ey14uD5ZqvAX19FVEHr6Q",
    "id": "6Ey14uD5ZqvAX19FVEHr6Q",
    "images": [
      {
        "height": 640,
        "url": "https://i.scdn.co/image/bf33e13dd697687d4da21931d5b5a96325af52bb",
        "width": 640
      },
      {
        "height": 300,
        "url": "https://i.scdn.co/image/62bf0667ac2ed580ea8c4f9d00404a7a5787b3f2",
        "width": 300
      },
      {
        "height": 64,
        "url": "https://i.scdn.co/image/177f8d411105795d749726057e8bdff53be35205",
        "width": 64
      }
    ],
    "name": "Seefu Lilac",
    "release_date": "2016-02-05",
    "release_date_precision": "day",
    "total_tracks": 9,
    "type": "album",
    "uri": "spotify:album:6Ey14uD5ZqvAX19FVEHr6Q"
  },
  "artists": [
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/4UHzJP2iKVf0RhKIv7ZE2l"
      },
      "href": "https://api.spotify.com/v1/artists/4UHzJP2iKVf0RhKIv7ZE2l",
      "id": "4UHzJP2iKVf0RhKIv7ZE2l",
      "name": "Black Moth Super Rainbow",
      "type": "artist",
      "uri": "spotify:artist:4UHzJP2iKVf0RhKIv7ZE2l"
    }
  ],
  "available_markets": [
    "AD",
    "AE",
    "AR",
    "AT",
    "AU",
    "BE",
    "BG",
    "BH",
    "BO",
    "BR",
    "CA",
    "CH",
    "CL",
    "CO",
    "CR",
    "CY",
    "CZ",
    "DE",
    "DK",
    "DO",
    "DZ",
    "EC",
    "EE",
    "EG",
    "ES",
    "FI",
    "FR",
    "GB",
    "GR",
    "GT",
    "HK",
    "HN",
    "HU",
    "ID",
    "IE",
    "IL",
    "IN",
    "IS",
    "IT",
    "JO",
    "JP",
    "KW",
    "LB",
    "LI",
    "LT",
    "LU",
    "LV",
    "MA",
    "MC",
    "MT",
    "MX",
    "MY",
    "NI",
    "NL",
    "NO",
    "NZ",
    "OM",
    "PA",
    "PE",
    "PH",
    "PL",
    "PS",
    "PT",
    "PY",
    "QA",
    "RO",
    "SA",
    "SE",
    "SG",
    "SK",
    "SV",
    "TH",
    "TN",
    "TR",
    "TW",
    "US",
    "UY",
    "VN",
    "ZA"
  ],
  "disc_number": 1,
  "duration_ms": 153120,
  "explicit": false,
  "external_ids": {
    "isrc": "QMDA71524270"
  },
  "external_urls": {
    "spotify": "https://open.spotify.com/track/0YgC0Gbx7zDuA7PPpH3HvA"
  },
  "href": "https://api.spotify.com/v1/tracks/0YgC0Gbx7zDuA7PPpH3HvA",
  "id": "0YgC0Gbx7zDuA7PPpH3HvA",
  "is_local": false,
  "name": "Seefu Lilac",
  "popularity": 33,
  "preview_url": "https://p.scdn.co/mp3-preview/70e002da9eccdfbb2ad03ba54897cc3bbce05595?cid=774b29d4f13844c495f206cafdad9c86",
  "track_number": 1,
  "type": "track",
  "uri": "spotify:track:0YgC0Gbx7zDuA7PPpH3HvA"
}
"""

track_relinked = json.loads(_jtrack)
track_w_markets = json.loads(_jtrackmarkets)
