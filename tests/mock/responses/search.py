import json

_jartists = """
{
  "artists": {
    "href": "https://api.spotify.com/v1/search?query=elvis&type=artist&market=CA&offset=0&limit=20",
    "items": [
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
        },
        "followers": {
          "href": null,
          "total": 2884872
        },
        "genres": [
          "adult standards",
          "christmas",
          "rock-and-roll",
          "rockabilly"
        ],
        "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
        "id": "43ZHCT0cAZBISjO8DG9PnE",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/5629fbf1c4e0bc4155eca3e08a2b98065eedd305",
            "width": 640
          },
          {
            "height": 320,
            "url": "https://i.scdn.co/image/de7df722a14208c879f169e26bd7792a9902c7ba",
            "width": 320
          },
          {
            "height": 160,
            "url": "https://i.scdn.co/image/11386c4abb5bdf71a86862cdb1a5390f37a7d8a5",
            "width": 160
          }
        ],
        "name": "Elvis Presley",
        "popularity": 79,
        "type": "artist",
        "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/1c22GXH30ijlOfXhfLz9Df"
        },
        "followers": {
          "href": null,
          "total": 315875
        },
        "genres": [
          "latin",
          "merengue",
          "tropical"
        ],
        "href": "https://api.spotify.com/v1/artists/1c22GXH30ijlOfXhfLz9Df",
        "id": "1c22GXH30ijlOfXhfLz9Df",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/4015340d49d93b66d9efeb688ad5f083057d3da6",
            "width": 640
          },
          {
            "height": 320,
            "url": "https://i.scdn.co/image/7180815f504e15f44c1f2a3ab30f2efc7e823a0a",
            "width": 320
          },
          {
            "height": 160,
            "url": "https://i.scdn.co/image/b67850e102412a69f0c9a2b6d1d30139e42facb6",
            "width": 160
          }
        ],
        "name": "Elvis Crespo",
        "popularity": 70,
        "type": "artist",
        "uri": "spotify:artist:1c22GXH30ijlOfXhfLz9Df"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/2pHk4wAmL7ofTAuvCIUWtv"
        },
        "followers": {
          "href": null,
          "total": 289346
        },
        "genres": [
          "belgian hip hop",
          "french hip hop"
        ],
        "href": "https://api.spotify.com/v1/artists/2pHk4wAmL7ofTAuvCIUWtv",
        "id": "2pHk4wAmL7ofTAuvCIUWtv",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/87b22aed5822224ae73df0424f50b4a3391f0d6d",
            "width": 640
          },
          {
            "height": 320,
            "url": "https://i.scdn.co/image/c00bba6cfa45ec5dd7ec870f2ced9f851bb70b1c",
            "width": 320
          },
          {
            "height": 160,
            "url": "https://i.scdn.co/image/845659ae01abe307a3ef1e2dfbf7d9a31da1e1b0",
            "width": 160
          }
        ],
        "name": "Roméo Elvis",
        "popularity": 74,
        "type": "artist",
        "uri": "spotify:artist:2pHk4wAmL7ofTAuvCIUWtv"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/2BGRfQgtzikz1pzAD0kaEn"
        },
        "followers": {
          "href": null,
          "total": 242810
        },
        "genres": [
          "art rock",
          "dance rock",
          "folk",
          "folk rock",
          "mellow gold",
          "new wave pop",
          "permanent wave",
          "power pop",
          "pub rock",
          "rock",
          "roots rock",
          "singer-songwriter"
        ],
        "href": "https://api.spotify.com/v1/artists/2BGRfQgtzikz1pzAD0kaEn",
        "id": "2BGRfQgtzikz1pzAD0kaEn",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/4859994e51f330b31d9321f97ce07af06b6a4b80",
            "width": 640
          },
          {
            "height": 320,
            "url": "https://i.scdn.co/image/bfbaf6cbf1ee268cd1a68d1a70486dfd55adf005",
            "width": 320
          },
          {
            "height": 160,
            "url": "https://i.scdn.co/image/28c42faa94107cee6ccd9a4f4e892beb0d3aa66c",
            "width": 160
          }
        ],
        "name": "Elvis Costello",
        "popularity": 58,
        "type": "artist",
        "uri": "spotify:artist:2BGRfQgtzikz1pzAD0kaEn"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/4qmHkMxr6pTWh5Zo74odpH"
        },
        "followers": {
          "href": null,
          "total": 106662
        },
        "genres": [
          "art rock",
          "dance rock",
          "folk rock",
          "mellow gold",
          "new wave",
          "new wave pop",
          "power pop",
          "pub rock",
          "rock",
          "roots rock"
        ],
        "href": "https://api.spotify.com/v1/artists/4qmHkMxr6pTWh5Zo74odpH",
        "id": "4qmHkMxr6pTWh5Zo74odpH",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/c14ffeb7855625383c266c9c04faa75516a25503",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/f3d1971157cbcb3d270aa3a7642baaadd65fa4f3",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/5baaf4b7373d0bb0d85f0100a24279c30be9d999",
            "width": 64
          }
        ],
        "name": "Elvis Costello & The Attractions",
        "popularity": 57,
        "type": "artist",
        "uri": "spotify:artist:4qmHkMxr6pTWh5Zo74odpH"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/5a31Ij1sTxY9LUYVwgBp8m"
        },
        "followers": {
          "href": null,
          "total": 62544
        },
        "genres": [
          "anti-folk",
          "asheville indie",
          "indie garage rock",
          "indie psych-pop",
          "lo-fi",
          "preverb",
          "shimmer psych",
          "small room"
        ],
        "href": "https://api.spotify.com/v1/artists/5a31Ij1sTxY9LUYVwgBp8m",
        "id": "5a31Ij1sTxY9LUYVwgBp8m",
        "images": [
          {
            "height": 666,
            "url": "https://i.scdn.co/image/1f257d7db77ece9d6477b0e0461a8c9a7b4be62f",
            "width": 1000
          },
          {
            "height": 426,
            "url": "https://i.scdn.co/image/2fcfac0d66a4f06b2161bd0010b5bef63ee98c67",
            "width": 640
          },
          {
            "height": 133,
            "url": "https://i.scdn.co/image/ff84fdc0393731c1bc4c79f5a7f191684a201c13",
            "width": 200
          },
          {
            "height": 43,
            "url": "https://i.scdn.co/image/8bb2d03100fe06a4cf29238c3e3bc5a9d2b96c57",
            "width": 64
          }
        ],
        "name": "Elvis Depressedly",
        "popularity": 47,
        "type": "artist",
        "uri": "spotify:artist:5a31Ij1sTxY9LUYVwgBp8m"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/66U02qGDesTqZImnLSiYeE"
        },
        "followers": {
          "href": null,
          "total": 68934
        },
        "genres": [
          "bachata",
          "dominican pop",
          "latin",
          "tropical"
        ],
        "href": "https://api.spotify.com/v1/artists/66U02qGDesTqZImnLSiYeE",
        "id": "66U02qGDesTqZImnLSiYeE",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/0b005147ce72f6fdb1c2fa1fdee08e13f6fd8899",
            "width": 640
          },
          {
            "height": 320,
            "url": "https://i.scdn.co/image/1d47b66fae8a204c07785a3ad7b195e58fafa196",
            "width": 320
          },
          {
            "height": 160,
            "url": "https://i.scdn.co/image/8b65818bc7a8b794cb84535a3d0c053a27ad2201",
            "width": 160
          }
        ],
        "name": "Elvis Martinez",
        "popularity": 45,
        "type": "artist",
        "uri": "spotify:artist:66U02qGDesTqZImnLSiYeE"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/70eE3MS4oHZvZVLLY2fU8B"
        },
        "followers": {
          "href": null,
          "total": 11743
        },
        "genres": [
          "indie folk",
          "stomp and holler"
        ],
        "href": "https://api.spotify.com/v1/artists/70eE3MS4oHZvZVLLY2fU8B",
        "id": "70eE3MS4oHZvZVLLY2fU8B",
        "images": [
          {
            "height": 1024,
            "url": "https://i.scdn.co/image/f65f52d8c5a042f447dc81100119134e27108958",
            "width": 683
          },
          {
            "height": 960,
            "url": "https://i.scdn.co/image/be45cfcc780db63094f9578ed62df61c37a3da00",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/2942a9223645286aaaa8c6281bd046e414bf9c5f",
            "width": 200
          },
          {
            "height": 96,
            "url": "https://i.scdn.co/image/d1b02fb45993e0723b9e8eba70a97f34ff4c97fa",
            "width": 64
          }
        ],
        "name": "Elvis Perkins",
        "popularity": 32,
        "type": "artist",
        "uri": "spotify:artist:70eE3MS4oHZvZVLLY2fU8B"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/1U1tfTJHxezIBnlay13sVA"
        },
        "followers": {
          "href": null,
          "total": 10935
        },
        "genres": [
          "french indie pop",
          "french indietronica",
          "french rock",
          "rock alternatif francais"
        ],
        "href": "https://api.spotify.com/v1/artists/1U1tfTJHxezIBnlay13sVA",
        "id": "1U1tfTJHxezIBnlay13sVA",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/70f680dc2e8054493960d3e95ea53ed8a941e8da",
            "width": 640
          },
          {
            "height": 320,
            "url": "https://i.scdn.co/image/f969f0e0b4012c1536a1cb166e73763f1da8822b",
            "width": 320
          },
          {
            "height": 160,
            "url": "https://i.scdn.co/image/863833100979c9ecd7274766ba05d3d1f3d8c6dc",
            "width": 160
          }
        ],
        "name": "Radio Elvis",
        "popularity": 37,
        "type": "artist",
        "uri": "spotify:artist:1U1tfTJHxezIBnlay13sVA"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/4P95HBikaVomMvtD6vg1vD"
        },
        "followers": {
          "href": null,
          "total": 10704
        },
        "genres": [
          "v-pop",
          "vietnamese bolero",
          "vietnamese pop"
        ],
        "href": "https://api.spotify.com/v1/artists/4P95HBikaVomMvtD6vg1vD",
        "id": "4P95HBikaVomMvtD6vg1vD",
        "images": [
          {
            "height": 600,
            "url": "https://i.scdn.co/image/c60985519dbe3f1a1f12b2c06ae15c20f7ba5563",
            "width": 600
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/da608414ad81f7120a30d85e555fd4934aa74914",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/cce2efca1810c8406b43dc09a04863eafd86a65e",
            "width": 64
          }
        ],
        "name": "Elvis Phuong",
        "popularity": 32,
        "type": "artist",
        "uri": "spotify:artist:4P95HBikaVomMvtD6vg1vD"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/6iMOh5TVCz6rLsI6CxYn83"
        },
        "followers": {
          "href": null,
          "total": 154
        },
        "genres": [],
        "href": "https://api.spotify.com/v1/artists/6iMOh5TVCz6rLsI6CxYn83",
        "id": "6iMOh5TVCz6rLsI6CxYn83",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/0abcdfe4accb3bb6edbcb0f4e5476849333a518d",
            "width": 640
          },
          {
            "height": 320,
            "url": "https://i.scdn.co/image/2940c625416333df41e5d786c40e93283a9cb47c",
            "width": 320
          },
          {
            "height": 160,
            "url": "https://i.scdn.co/image/87a314354ad517486c3c28249345981e1823dfde",
            "width": 160
          }
        ],
        "name": "Elvis Brown",
        "popularity": 32,
        "type": "artist",
        "uri": "spotify:artist:6iMOh5TVCz6rLsI6CxYn83"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/0iDx57ZX3eCX4LIc5Ie01d"
        },
        "followers": {
          "href": null,
          "total": 193
        },
        "genres": [],
        "href": "https://api.spotify.com/v1/artists/0iDx57ZX3eCX4LIc5Ie01d",
        "id": "0iDx57ZX3eCX4LIc5Ie01d",
        "images": [],
        "name": "Elvis-Kingtinued",
        "popularity": 28,
        "type": "artist",
        "uri": "spotify:artist:0iDx57ZX3eCX4LIc5Ie01d"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/02p6EaTq8nO9jBFxZYPhl4"
        },
        "followers": {
          "href": null,
          "total": 2444
        },
        "genres": [],
        "href": "https://api.spotify.com/v1/artists/02p6EaTq8nO9jBFxZYPhl4",
        "id": "02p6EaTq8nO9jBFxZYPhl4",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/7fe8e8938db4c2164208b18d92b8318a9d012294",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/a8e8329815879922de2819aed1a69f34a459b61d",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/40b64bc53d0eafe5ddd283ef152f31cb08d92a5b",
            "width": 64
          }
        ],
        "name": "Elvis Presley with Orchestra",
        "popularity": 28,
        "type": "artist",
        "uri": "spotify:artist:02p6EaTq8nO9jBFxZYPhl4"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/6ZZDnzyqRRFwQJDDKdQhmu"
        },
        "followers": {
          "href": null,
          "total": 7
        },
        "genres": [],
        "href": "https://api.spotify.com/v1/artists/6ZZDnzyqRRFwQJDDKdQhmu",
        "id": "6ZZDnzyqRRFwQJDDKdQhmu",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/78df8821aa040150c4296629f0e46cf7aaac5313",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/d7379c3b417ac43b54e2f1e31888bfc4763bba76",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/20c1635f99282f9366cde25e7ddd681d5ecaf52d",
            "width": 64
          }
        ],
        "name": "Elvis Who",
        "popularity": 24,
        "type": "artist",
        "uri": "spotify:artist:6ZZDnzyqRRFwQJDDKdQhmu"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/761s7ARkOG0L11knEZ0WhF"
        },
        "followers": {
          "href": null,
          "total": 995
        },
        "genres": [
          "uk contemporary r&b"
        ],
        "href": "https://api.spotify.com/v1/artists/761s7ARkOG0L11knEZ0WhF",
        "id": "761s7ARkOG0L11knEZ0WhF",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/d961fe6239ce8b71ebf94e7f29b224cfcd4c72d3",
            "width": 640
          },
          {
            "height": 320,
            "url": "https://i.scdn.co/image/f57a542046b00b400e712dc8472f4599df842617",
            "width": 320
          },
          {
            "height": 160,
            "url": "https://i.scdn.co/image/cb1bccf8f543f299eea53ce48d4c52c5b4fa558f",
            "width": 160
          }
        ],
        "name": "Jesse Elvis",
        "popularity": 27,
        "type": "artist",
        "uri": "spotify:artist:761s7ARkOG0L11knEZ0WhF"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/5uaPSAp8fyAv9eAcWKwNIx"
        },
        "followers": {
          "href": null,
          "total": 6244
        },
        "genres": [],
        "href": "https://api.spotify.com/v1/artists/5uaPSAp8fyAv9eAcWKwNIx",
        "id": "5uaPSAp8fyAv9eAcWKwNIx",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/57d0f881a5cdf85ee7615cf75f0b308b96a7eb1a",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/9a856f29304386d32975204fc4b036c74250f293",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/e8eacdd269cffc6669723f39fa9661f9c64958c0",
            "width": 64
          }
        ],
        "name": "Elvis Costello And The Roots",
        "popularity": 28,
        "type": "artist",
        "uri": "spotify:artist:5uaPSAp8fyAv9eAcWKwNIx"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/0uGbw6mYrgcAV4q35AQJxp"
        },
        "followers": {
          "href": null,
          "total": 376
        },
        "genres": [],
        "href": "https://api.spotify.com/v1/artists/0uGbw6mYrgcAV4q35AQJxp",
        "id": "0uGbw6mYrgcAV4q35AQJxp",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/dfb01bcc5d9fd00822b6b132b241de0647d46bbe",
            "width": 640
          },
          {
            "height": 320,
            "url": "https://i.scdn.co/image/c87deb63865cee8ad08a3b501a3bec24060a5eef",
            "width": 320
          },
          {
            "height": 160,
            "url": "https://i.scdn.co/image/eff09a63a9d35780acf5f16294e1a6b7a43e0be6",
            "width": 160
          }
        ],
        "name": "Elvis vs. Spankox",
        "popularity": 27,
        "type": "artist",
        "uri": "spotify:artist:0uGbw6mYrgcAV4q35AQJxp"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/6rUNYES6q7IfMNapFY6Uvm"
        },
        "followers": {
          "href": null,
          "total": 35
        },
        "genres": [],
        "href": "https://api.spotify.com/v1/artists/6rUNYES6q7IfMNapFY6Uvm",
        "id": "6rUNYES6q7IfMNapFY6Uvm",
        "images": [],
        "name": "Elvis Crespo, Ilegales",
        "popularity": 27,
        "type": "artist",
        "uri": "spotify:artist:6rUNYES6q7IfMNapFY6Uvm"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/1QjKfAozX9saH9OA370QTW"
        },
        "followers": {
          "href": null,
          "total": 393
        },
        "genres": [],
        "href": "https://api.spotify.com/v1/artists/1QjKfAozX9saH9OA370QTW",
        "id": "1QjKfAozX9saH9OA370QTW",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ec2448f0b0ceaef1e5897e9a733e8470dcd702ab",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/cb52d1a3f454b02e413b01d09a65e3189143cb0d",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/5dd832de0574ffa34efbeff6e017289b824deadc",
            "width": 64
          }
        ],
        "name": "Tokyo Elvis",
        "popularity": 20,
        "type": "artist",
        "uri": "spotify:artist:1QjKfAozX9saH9OA370QTW"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/6Vqm13QDZriNExERh317XN"
        },
        "followers": {
          "href": null,
          "total": 65
        },
        "genres": [],
        "href": "https://api.spotify.com/v1/artists/6Vqm13QDZriNExERh317XN",
        "id": "6Vqm13QDZriNExERh317XN",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/c23b2fb364d3fdd024af1026f90c8a4772148fa5",
            "width": 640
          },
          {
            "height": 320,
            "url": "https://i.scdn.co/image/5e8cc11a996400131b67e33a012a464d2a350387",
            "width": 320
          },
          {
            "height": 160,
            "url": "https://i.scdn.co/image/34d1cbfdb4f6108ac9df5713da0e0b465e315b9d",
            "width": 160
          }
        ],
        "name": "Mike Elvis",
        "popularity": 18,
        "type": "artist",
        "uri": "spotify:artist:6Vqm13QDZriNExERh317XN"
      }
    ],
    "limit": 20,
    "next": "https://api.spotify.com/v1/search?query=elvis&type=artist&market=CA&offset=20&limit=20",
    "offset": 0,
    "previous": null,
    "total": 523
  }
}
"""

_jalltypes = """
{
  "albums": {
    "href": "https://api.spotify.com/v1/search?query=elvis&type=album&market=CA&offset=0&limit=10",
    "items": [
      {
        "album_type": "album",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
            },
            "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
            "id": "43ZHCT0cAZBISjO8DG9PnE",
            "name": "Elvis Presley",
            "type": "artist",
            "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
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
          "spotify": "https://open.spotify.com/album/0C3t1htEDTFKcg7F2rNbek"
        },
        "href": "https://api.spotify.com/v1/albums/0C3t1htEDTFKcg7F2rNbek",
        "id": "0C3t1htEDTFKcg7F2rNbek",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/f3c95ddbd77813737616eb327b4e31106d0b2bab",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/cc7323d63e79dd46fea998f99ef459544114b01c",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/3cbd4a9b70b83f98d8ef8691c6a5f1c2c32f1bcc",
            "width": 64
          }
        ],
        "name": "Elvis' Golden Records",
        "release_date": "1958-03-21",
        "release_date_precision": "day",
        "total_tracks": 14,
        "type": "album",
        "uri": "spotify:album:0C3t1htEDTFKcg7F2rNbek"
      },
      {
        "album_type": "compilation",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
            },
            "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
            "id": "43ZHCT0cAZBISjO8DG9PnE",
            "name": "Elvis Presley",
            "type": "artist",
            "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
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
          "spotify": "https://open.spotify.com/album/0QVoYzGd1p8Z3ohEaM0lsc"
        },
        "href": "https://api.spotify.com/v1/albums/0QVoYzGd1p8Z3ohEaM0lsc",
        "id": "0QVoYzGd1p8Z3ohEaM0lsc",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/efa549a3619dffcbf31e937b3419750195f42282",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/97f5e9a283a428ab4dbd32ece5009f46f079ab62",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/f49f7c681ed6a4548328875ee36e9a8f462c59cf",
            "width": 64
          }
        ],
        "name": "Elvis 30 #1 Hits",
        "release_date": "2002-09-24",
        "release_date_precision": "day",
        "total_tracks": 31,
        "type": "album",
        "uri": "spotify:album:0QVoYzGd1p8Z3ohEaM0lsc"
      },
      {
        "album_type": "album",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
            },
            "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
            "id": "43ZHCT0cAZBISjO8DG9PnE",
            "name": "Elvis Presley",
            "type": "artist",
            "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
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
          "spotify": "https://open.spotify.com/album/3ekkFrfotMsEAKc5g71GHk"
        },
        "href": "https://api.spotify.com/v1/albums/3ekkFrfotMsEAKc5g71GHk",
        "id": "3ekkFrfotMsEAKc5g71GHk",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/3a36159ea0439cd53d807ef0643d4e228406381a",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/d7bfcff6020fd48921a9f154a4266d7f4851cfa9",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/303c5223ef3da80078bdaedf50dceacbb951dc23",
            "width": 64
          }
        ],
        "name": "From Elvis in Memphis",
        "release_date": "1969-06-17",
        "release_date_precision": "day",
        "total_tracks": 16,
        "type": "album",
        "uri": "spotify:album:3ekkFrfotMsEAKc5g71GHk"
      },
      {
        "album_type": "album",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
            },
            "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
            "id": "43ZHCT0cAZBISjO8DG9PnE",
            "name": "Elvis Presley",
            "type": "artist",
            "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
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
          "spotify": "https://open.spotify.com/album/7xe8VI48TxUpU1IIo0RfGi"
        },
        "href": "https://api.spotify.com/v1/albums/7xe8VI48TxUpU1IIo0RfGi",
        "id": "7xe8VI48TxUpU1IIo0RfGi",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ef0dc94d4a69ad10da0fa3768db0b0a1601df668",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/be0a2916a8b5aa16e90a471cb5a53d92a233a6dc",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/dd5d7f28db5df5d620eed297eaf91e0ea790eeb3",
            "width": 64
          }
        ],
        "name": "Blue Hawaii",
        "release_date": "1961-10-20",
        "release_date_precision": "day",
        "total_tracks": 14,
        "type": "album",
        "uri": "spotify:album:7xe8VI48TxUpU1IIo0RfGi"
      },
      {
        "album_type": "album",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
            },
            "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
            "id": "43ZHCT0cAZBISjO8DG9PnE",
            "name": "Elvis Presley",
            "type": "artist",
            "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
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
          "spotify": "https://open.spotify.com/album/3gpHiNAmT5oXVxe6ewTGuN"
        },
        "href": "https://api.spotify.com/v1/albums/3gpHiNAmT5oXVxe6ewTGuN",
        "id": "3gpHiNAmT5oXVxe6ewTGuN",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/7a1a08f2c1b22eca8b9b775d002c4a6d248a6c9b",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/690a5b3dfd767eb234e7efd168867d7106457619",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/a58c531a579e9e0fb9367a59ee1bc50a912dfc01",
            "width": 64
          }
        ],
        "name": "Elvis (Fool)",
        "release_date": "1973-07-16",
        "release_date_precision": "day",
        "total_tracks": 16,
        "type": "album",
        "uri": "spotify:album:3gpHiNAmT5oXVxe6ewTGuN"
      },
      {
        "album_type": "album",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
            },
            "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
            "id": "43ZHCT0cAZBISjO8DG9PnE",
            "name": "Elvis Presley",
            "type": "artist",
            "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
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
          "spotify": "https://open.spotify.com/album/1vaQwUom5fWnLNJDcabU01"
        },
        "href": "https://api.spotify.com/v1/albums/1vaQwUom5fWnLNJDcabU01",
        "id": "1vaQwUom5fWnLNJDcabU01",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/06cc0468438b701783a1d1ebd02802a728c2b909",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/5880be08bc3120fc3b3f6fb8363fec1316e672d7",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/4bcb84a5575bf407f4a21a74990d694eace474d4",
            "width": 64
          }
        ],
        "name": "The Best of The '68 Comeback Special",
        "release_date": "2019-02-15",
        "release_date_precision": "day",
        "total_tracks": 19,
        "type": "album",
        "uri": "spotify:album:1vaQwUom5fWnLNJDcabU01"
      },
      {
        "album_type": "album",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
            },
            "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
            "id": "43ZHCT0cAZBISjO8DG9PnE",
            "name": "Elvis Presley",
            "type": "artist",
            "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
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
          "spotify": "https://open.spotify.com/album/5Iec810oL6PorbyBVjLnmD"
        },
        "href": "https://api.spotify.com/v1/albums/5Iec810oL6PorbyBVjLnmD",
        "id": "5Iec810oL6PorbyBVjLnmD",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/3aef61e227c3c7e3f43813e4b54b79dfb0d4ac3e",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/8b1e46ec3642db578ff480db73655fd6fdf0634b",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/7321e74664f3660f621b138f953766acc3b6f9d8",
            "width": 64
          }
        ],
        "name": "Elvis' Golden Records, Vol. 3",
        "release_date": "1963-08-11",
        "release_date_precision": "day",
        "total_tracks": 12,
        "type": "album",
        "uri": "spotify:album:5Iec810oL6PorbyBVjLnmD"
      },
      {
        "album_type": "album",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
            },
            "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
            "id": "43ZHCT0cAZBISjO8DG9PnE",
            "name": "Elvis Presley",
            "type": "artist",
            "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
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
          "spotify": "https://open.spotify.com/album/7GXP5OhYyPVLmcVfO9Iqin"
        },
        "href": "https://api.spotify.com/v1/albums/7GXP5OhYyPVLmcVfO9Iqin",
        "id": "7GXP5OhYyPVLmcVfO9Iqin",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/b80a490aeb3916fdc1aa701eb70e201ce9419f42",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ee3032234b7a06fcfecb96a460297df42e9732c1",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/f85d77e3b0e19390eb8b7ae4e1942d40ccf3b7d9",
            "width": 64
          }
        ],
        "name": "Elvis Presley",
        "release_date": "1956-03-23",
        "release_date_precision": "day",
        "total_tracks": 12,
        "type": "album",
        "uri": "spotify:album:7GXP5OhYyPVLmcVfO9Iqin"
      },
      {
        "album_type": "compilation",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
            },
            "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
            "id": "43ZHCT0cAZBISjO8DG9PnE",
            "name": "Elvis Presley",
            "type": "artist",
            "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
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
          "spotify": "https://open.spotify.com/album/3X3rFfVKCW58sKMO0UXkwO"
        },
        "href": "https://api.spotify.com/v1/albums/3X3rFfVKCW58sKMO0UXkwO",
        "id": "3X3rFfVKCW58sKMO0UXkwO",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/b1b009453f4b960d17a6bac93e797da5215ff094",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/a00d29dc30c7559d910c660885c2dbc64f7308a1",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/96e5e24de5293f115f2b8e6524b2df87fd843403",
            "width": 64
          }
        ],
        "name": "The Essential Elvis Presley",
        "release_date": "2007",
        "release_date_precision": "year",
        "total_tracks": 40,
        "type": "album",
        "uri": "spotify:album:3X3rFfVKCW58sKMO0UXkwO"
      },
      {
        "album_type": "album",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
            },
            "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
            "id": "43ZHCT0cAZBISjO8DG9PnE",
            "name": "Elvis Presley",
            "type": "artist",
            "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
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
          "spotify": "https://open.spotify.com/album/6zk4RKl6JFlgLCV4Z7DQ7N"
        },
        "href": "https://api.spotify.com/v1/albums/6zk4RKl6JFlgLCV4Z7DQ7N",
        "id": "6zk4RKl6JFlgLCV4Z7DQ7N",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/938708427180880064ee3b63e1d379c60f44e110",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/56806ffd0bdbf2f4063d29bf284fed7c318480d8",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/a60e228b8350e8d166401c3f826b1cb8f4b428d2",
            "width": 64
          }
        ],
        "name": "Elvis' Christmas Album",
        "release_date": "1957-10-15",
        "release_date_precision": "day",
        "total_tracks": 12,
        "type": "album",
        "uri": "spotify:album:6zk4RKl6JFlgLCV4Z7DQ7N"
      }
    ],
    "limit": 10,
    "next": "https://api.spotify.com/v1/search?query=elvis&type=album&market=CA&offset=10&limit=10",
    "offset": 0,
    "previous": null,
    "total": 3227
  },
  "artists": {
    "href": "https://api.spotify.com/v1/search?query=elvis&type=artist&market=CA&offset=0&limit=10",
    "items": [
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
        },
        "followers": {
          "href": null,
          "total": 2884876
        },
        "genres": [
          "adult standards",
          "christmas",
          "rock-and-roll",
          "rockabilly"
        ],
        "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
        "id": "43ZHCT0cAZBISjO8DG9PnE",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/5629fbf1c4e0bc4155eca3e08a2b98065eedd305",
            "width": 640
          },
          {
            "height": 320,
            "url": "https://i.scdn.co/image/de7df722a14208c879f169e26bd7792a9902c7ba",
            "width": 320
          },
          {
            "height": 160,
            "url": "https://i.scdn.co/image/11386c4abb5bdf71a86862cdb1a5390f37a7d8a5",
            "width": 160
          }
        ],
        "name": "Elvis Presley",
        "popularity": 79,
        "type": "artist",
        "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/1c22GXH30ijlOfXhfLz9Df"
        },
        "followers": {
          "href": null,
          "total": 315875
        },
        "genres": [
          "latin",
          "merengue",
          "tropical"
        ],
        "href": "https://api.spotify.com/v1/artists/1c22GXH30ijlOfXhfLz9Df",
        "id": "1c22GXH30ijlOfXhfLz9Df",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/4015340d49d93b66d9efeb688ad5f083057d3da6",
            "width": 640
          },
          {
            "height": 320,
            "url": "https://i.scdn.co/image/7180815f504e15f44c1f2a3ab30f2efc7e823a0a",
            "width": 320
          },
          {
            "height": 160,
            "url": "https://i.scdn.co/image/b67850e102412a69f0c9a2b6d1d30139e42facb6",
            "width": 160
          }
        ],
        "name": "Elvis Crespo",
        "popularity": 70,
        "type": "artist",
        "uri": "spotify:artist:1c22GXH30ijlOfXhfLz9Df"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/2pHk4wAmL7ofTAuvCIUWtv"
        },
        "followers": {
          "href": null,
          "total": 289346
        },
        "genres": [
          "belgian hip hop",
          "french hip hop"
        ],
        "href": "https://api.spotify.com/v1/artists/2pHk4wAmL7ofTAuvCIUWtv",
        "id": "2pHk4wAmL7ofTAuvCIUWtv",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/87b22aed5822224ae73df0424f50b4a3391f0d6d",
            "width": 640
          },
          {
            "height": 320,
            "url": "https://i.scdn.co/image/c00bba6cfa45ec5dd7ec870f2ced9f851bb70b1c",
            "width": 320
          },
          {
            "height": 160,
            "url": "https://i.scdn.co/image/845659ae01abe307a3ef1e2dfbf7d9a31da1e1b0",
            "width": 160
          }
        ],
        "name": "Roméo Elvis",
        "popularity": 74,
        "type": "artist",
        "uri": "spotify:artist:2pHk4wAmL7ofTAuvCIUWtv"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/2BGRfQgtzikz1pzAD0kaEn"
        },
        "followers": {
          "href": null,
          "total": 242812
        },
        "genres": [
          "art rock",
          "dance rock",
          "folk",
          "folk rock",
          "mellow gold",
          "new wave pop",
          "permanent wave",
          "power pop",
          "pub rock",
          "rock",
          "roots rock",
          "singer-songwriter"
        ],
        "href": "https://api.spotify.com/v1/artists/2BGRfQgtzikz1pzAD0kaEn",
        "id": "2BGRfQgtzikz1pzAD0kaEn",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/4859994e51f330b31d9321f97ce07af06b6a4b80",
            "width": 640
          },
          {
            "height": 320,
            "url": "https://i.scdn.co/image/bfbaf6cbf1ee268cd1a68d1a70486dfd55adf005",
            "width": 320
          },
          {
            "height": 160,
            "url": "https://i.scdn.co/image/28c42faa94107cee6ccd9a4f4e892beb0d3aa66c",
            "width": 160
          }
        ],
        "name": "Elvis Costello",
        "popularity": 58,
        "type": "artist",
        "uri": "spotify:artist:2BGRfQgtzikz1pzAD0kaEn"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/4qmHkMxr6pTWh5Zo74odpH"
        },
        "followers": {
          "href": null,
          "total": 106663
        },
        "genres": [
          "art rock",
          "dance rock",
          "folk rock",
          "mellow gold",
          "new wave",
          "new wave pop",
          "power pop",
          "pub rock",
          "rock",
          "roots rock"
        ],
        "href": "https://api.spotify.com/v1/artists/4qmHkMxr6pTWh5Zo74odpH",
        "id": "4qmHkMxr6pTWh5Zo74odpH",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/c14ffeb7855625383c266c9c04faa75516a25503",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/f3d1971157cbcb3d270aa3a7642baaadd65fa4f3",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/5baaf4b7373d0bb0d85f0100a24279c30be9d999",
            "width": 64
          }
        ],
        "name": "Elvis Costello & The Attractions",
        "popularity": 57,
        "type": "artist",
        "uri": "spotify:artist:4qmHkMxr6pTWh5Zo74odpH"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/5a31Ij1sTxY9LUYVwgBp8m"
        },
        "followers": {
          "href": null,
          "total": 62545
        },
        "genres": [
          "anti-folk",
          "asheville indie",
          "indie garage rock",
          "indie psych-pop",
          "lo-fi",
          "preverb",
          "shimmer psych",
          "small room"
        ],
        "href": "https://api.spotify.com/v1/artists/5a31Ij1sTxY9LUYVwgBp8m",
        "id": "5a31Ij1sTxY9LUYVwgBp8m",
        "images": [
          {
            "height": 666,
            "url": "https://i.scdn.co/image/1f257d7db77ece9d6477b0e0461a8c9a7b4be62f",
            "width": 1000
          },
          {
            "height": 426,
            "url": "https://i.scdn.co/image/2fcfac0d66a4f06b2161bd0010b5bef63ee98c67",
            "width": 640
          },
          {
            "height": 133,
            "url": "https://i.scdn.co/image/ff84fdc0393731c1bc4c79f5a7f191684a201c13",
            "width": 200
          },
          {
            "height": 43,
            "url": "https://i.scdn.co/image/8bb2d03100fe06a4cf29238c3e3bc5a9d2b96c57",
            "width": 64
          }
        ],
        "name": "Elvis Depressedly",
        "popularity": 47,
        "type": "artist",
        "uri": "spotify:artist:5a31Ij1sTxY9LUYVwgBp8m"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/66U02qGDesTqZImnLSiYeE"
        },
        "followers": {
          "href": null,
          "total": 68934
        },
        "genres": [
          "bachata",
          "dominican pop",
          "latin",
          "tropical"
        ],
        "href": "https://api.spotify.com/v1/artists/66U02qGDesTqZImnLSiYeE",
        "id": "66U02qGDesTqZImnLSiYeE",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/0b005147ce72f6fdb1c2fa1fdee08e13f6fd8899",
            "width": 640
          },
          {
            "height": 320,
            "url": "https://i.scdn.co/image/1d47b66fae8a204c07785a3ad7b195e58fafa196",
            "width": 320
          },
          {
            "height": 160,
            "url": "https://i.scdn.co/image/8b65818bc7a8b794cb84535a3d0c053a27ad2201",
            "width": 160
          }
        ],
        "name": "Elvis Martinez",
        "popularity": 45,
        "type": "artist",
        "uri": "spotify:artist:66U02qGDesTqZImnLSiYeE"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/70eE3MS4oHZvZVLLY2fU8B"
        },
        "followers": {
          "href": null,
          "total": 11743
        },
        "genres": [
          "indie folk",
          "stomp and holler"
        ],
        "href": "https://api.spotify.com/v1/artists/70eE3MS4oHZvZVLLY2fU8B",
        "id": "70eE3MS4oHZvZVLLY2fU8B",
        "images": [
          {
            "height": 1024,
            "url": "https://i.scdn.co/image/f65f52d8c5a042f447dc81100119134e27108958",
            "width": 683
          },
          {
            "height": 960,
            "url": "https://i.scdn.co/image/be45cfcc780db63094f9578ed62df61c37a3da00",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/2942a9223645286aaaa8c6281bd046e414bf9c5f",
            "width": 200
          },
          {
            "height": 96,
            "url": "https://i.scdn.co/image/d1b02fb45993e0723b9e8eba70a97f34ff4c97fa",
            "width": 64
          }
        ],
        "name": "Elvis Perkins",
        "popularity": 32,
        "type": "artist",
        "uri": "spotify:artist:70eE3MS4oHZvZVLLY2fU8B"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/1U1tfTJHxezIBnlay13sVA"
        },
        "followers": {
          "href": null,
          "total": 10935
        },
        "genres": [
          "french indie pop",
          "french indietronica",
          "french rock",
          "rock alternatif francais"
        ],
        "href": "https://api.spotify.com/v1/artists/1U1tfTJHxezIBnlay13sVA",
        "id": "1U1tfTJHxezIBnlay13sVA",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/70f680dc2e8054493960d3e95ea53ed8a941e8da",
            "width": 640
          },
          {
            "height": 320,
            "url": "https://i.scdn.co/image/f969f0e0b4012c1536a1cb166e73763f1da8822b",
            "width": 320
          },
          {
            "height": 160,
            "url": "https://i.scdn.co/image/863833100979c9ecd7274766ba05d3d1f3d8c6dc",
            "width": 160
          }
        ],
        "name": "Radio Elvis",
        "popularity": 37,
        "type": "artist",
        "uri": "spotify:artist:1U1tfTJHxezIBnlay13sVA"
      },
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/4P95HBikaVomMvtD6vg1vD"
        },
        "followers": {
          "href": null,
          "total": 10704
        },
        "genres": [
          "v-pop",
          "vietnamese bolero",
          "vietnamese pop"
        ],
        "href": "https://api.spotify.com/v1/artists/4P95HBikaVomMvtD6vg1vD",
        "id": "4P95HBikaVomMvtD6vg1vD",
        "images": [
          {
            "height": 600,
            "url": "https://i.scdn.co/image/c60985519dbe3f1a1f12b2c06ae15c20f7ba5563",
            "width": 600
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/da608414ad81f7120a30d85e555fd4934aa74914",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/cce2efca1810c8406b43dc09a04863eafd86a65e",
            "width": 64
          }
        ],
        "name": "Elvis Phuong",
        "popularity": 32,
        "type": "artist",
        "uri": "spotify:artist:4P95HBikaVomMvtD6vg1vD"
      }
    ],
    "limit": 10,
    "next": "https://api.spotify.com/v1/search?query=elvis&type=artist&market=CA&offset=10&limit=10",
    "offset": 0,
    "previous": null,
    "total": 523
  },
  "tracks": {
    "href": "https://api.spotify.com/v1/search?query=elvis&type=track&market=CA&offset=0&limit=10",
    "items": [
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
              },
              "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
              "id": "43ZHCT0cAZBISjO8DG9PnE",
              "name": "Elvis Presley",
              "type": "artist",
              "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
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
            "spotify": "https://open.spotify.com/album/7xe8VI48TxUpU1IIo0RfGi"
          },
          "href": "https://api.spotify.com/v1/albums/7xe8VI48TxUpU1IIo0RfGi",
          "id": "7xe8VI48TxUpU1IIo0RfGi",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ef0dc94d4a69ad10da0fa3768db0b0a1601df668",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/be0a2916a8b5aa16e90a471cb5a53d92a233a6dc",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/dd5d7f28db5df5d620eed297eaf91e0ea790eeb3",
              "width": 64
            }
          ],
          "name": "Blue Hawaii",
          "release_date": "1961-10-20",
          "release_date_precision": "day",
          "total_tracks": 14,
          "type": "album",
          "uri": "spotify:album:7xe8VI48TxUpU1IIo0RfGi"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
            },
            "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
            "id": "43ZHCT0cAZBISjO8DG9PnE",
            "name": "Elvis Presley",
            "type": "artist",
            "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
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
        "duration_ms": 182360,
        "explicit": false,
        "external_ids": {
          "isrc": "USRC16101350"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/44AyOl4qVkzS48vBsbNXaC"
        },
        "href": "https://api.spotify.com/v1/tracks/44AyOl4qVkzS48vBsbNXaC",
        "id": "44AyOl4qVkzS48vBsbNXaC",
        "is_local": false,
        "name": "Can't Help Falling in Love",
        "popularity": 78,
        "preview_url": "https://p.scdn.co/mp3-preview/994ebd7f49e4e935df56d450b0c12d8bad8bb9f4?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 5,
        "type": "track",
        "uri": "spotify:track:44AyOl4qVkzS48vBsbNXaC"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/70kkdajctXSbqSMJbQO424"
              },
              "href": "https://api.spotify.com/v1/artists/70kkdajctXSbqSMJbQO424",
              "id": "70kkdajctXSbqSMJbQO424",
              "name": "Kacey Musgraves",
              "type": "artist",
              "uri": "spotify:artist:70kkdajctXSbqSMJbQO424"
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
            "spotify": "https://open.spotify.com/album/7f6xPqyaolTiziKf5R5Z0c"
          },
          "href": "https://api.spotify.com/v1/albums/7f6xPqyaolTiziKf5R5Z0c",
          "id": "7f6xPqyaolTiziKf5R5Z0c",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/74001b62726f25b6086a6f3626ba6478917c5d20",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/90d3e685558fa4c4ec88380616033ea32a1f3de5",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/5178be1a7f89b34d2dd197053d59a781d14543da",
              "width": 64
            }
          ],
          "name": "Golden Hour",
          "release_date": "2018-03-30",
          "release_date_precision": "day",
          "total_tracks": 13,
          "type": "album",
          "uri": "spotify:album:7f6xPqyaolTiziKf5R5Z0c"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/70kkdajctXSbqSMJbQO424"
            },
            "href": "https://api.spotify.com/v1/artists/70kkdajctXSbqSMJbQO424",
            "id": "70kkdajctXSbqSMJbQO424",
            "name": "Kacey Musgraves",
            "type": "artist",
            "uri": "spotify:artist:70kkdajctXSbqSMJbQO424"
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
        "duration_ms": 154386,
        "explicit": false,
        "external_ids": {
          "isrc": "USUM71800135"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/65krgqLiZqW12PZAUQ9l2x"
        },
        "href": "https://api.spotify.com/v1/tracks/65krgqLiZqW12PZAUQ9l2x",
        "id": "65krgqLiZqW12PZAUQ9l2x",
        "is_local": false,
        "name": "Velvet Elvis",
        "popularity": 68,
        "preview_url": null,
        "track_number": 9,
        "type": "track",
        "uri": "spotify:track:65krgqLiZqW12PZAUQ9l2x"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/3QVolfxko2UyCOtexhVTli"
              },
              "href": "https://api.spotify.com/v1/artists/3QVolfxko2UyCOtexhVTli",
              "id": "3QVolfxko2UyCOtexhVTli",
              "name": "Angèle",
              "type": "artist",
              "uri": "spotify:artist:3QVolfxko2UyCOtexhVTli"
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
            "spotify": "https://open.spotify.com/album/6KSvWFf4g4PrIldtchJsTC"
          },
          "href": "https://api.spotify.com/v1/albums/6KSvWFf4g4PrIldtchJsTC",
          "id": "6KSvWFf4g4PrIldtchJsTC",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/458c677e9ab27951f97257b35cbd19f77bbc846c",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/88517c497e3012c00167bcbf2194c25befc1964b",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/d2da735bd6d33096b8687794ecc4f8bf57ed66ab",
              "width": 64
            }
          ],
          "name": "Brol",
          "release_date": "2018-10-05",
          "release_date_precision": "day",
          "total_tracks": 12,
          "type": "album",
          "uri": "spotify:album:6KSvWFf4g4PrIldtchJsTC"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/3QVolfxko2UyCOtexhVTli"
            },
            "href": "https://api.spotify.com/v1/artists/3QVolfxko2UyCOtexhVTli",
            "id": "3QVolfxko2UyCOtexhVTli",
            "name": "Angèle",
            "type": "artist",
            "uri": "spotify:artist:3QVolfxko2UyCOtexhVTli"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2pHk4wAmL7ofTAuvCIUWtv"
            },
            "href": "https://api.spotify.com/v1/artists/2pHk4wAmL7ofTAuvCIUWtv",
            "id": "2pHk4wAmL7ofTAuvCIUWtv",
            "name": "Roméo Elvis",
            "type": "artist",
            "uri": "spotify:artist:2pHk4wAmL7ofTAuvCIUWtv"
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
        "duration_ms": 202120,
        "explicit": false,
        "external_ids": {
          "isrc": "BE8HB1800008"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/06O3hxudc6V0BOuoCFSy71"
        },
        "href": "https://api.spotify.com/v1/tracks/06O3hxudc6V0BOuoCFSy71",
        "id": "06O3hxudc6V0BOuoCFSy71",
        "is_local": false,
        "name": "Tout oublier",
        "popularity": 79,
        "preview_url": null,
        "track_number": 4,
        "type": "track",
        "uri": "spotify:track:06O3hxudc6V0BOuoCFSy71"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
              },
              "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
              "id": "43ZHCT0cAZBISjO8DG9PnE",
              "name": "Elvis Presley",
              "type": "artist",
              "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
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
            "spotify": "https://open.spotify.com/album/0C3t1htEDTFKcg7F2rNbek"
          },
          "href": "https://api.spotify.com/v1/albums/0C3t1htEDTFKcg7F2rNbek",
          "id": "0C3t1htEDTFKcg7F2rNbek",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/f3c95ddbd77813737616eb327b4e31106d0b2bab",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/cc7323d63e79dd46fea998f99ef459544114b01c",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/3cbd4a9b70b83f98d8ef8691c6a5f1c2c32f1bcc",
              "width": 64
            }
          ],
          "name": "Elvis' Golden Records",
          "release_date": "1958-03-21",
          "release_date_precision": "day",
          "total_tracks": 14,
          "type": "album",
          "uri": "spotify:album:0C3t1htEDTFKcg7F2rNbek"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
            },
            "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
            "id": "43ZHCT0cAZBISjO8DG9PnE",
            "name": "Elvis Presley",
            "type": "artist",
            "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
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
        "duration_ms": 146480,
        "explicit": false,
        "external_ids": {
          "isrc": "USRC15705223"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/4gphxUgq0JSFv2BCLhNDiE"
        },
        "href": "https://api.spotify.com/v1/tracks/4gphxUgq0JSFv2BCLhNDiE",
        "id": "4gphxUgq0JSFv2BCLhNDiE",
        "is_local": false,
        "name": "Jailhouse Rock",
        "popularity": 73,
        "preview_url": "https://p.scdn.co/mp3-preview/29990f669b5328b6c40320596a2b14d8660cdb54?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 5,
        "type": "track",
        "uri": "spotify:track:4gphxUgq0JSFv2BCLhNDiE"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
              },
              "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
              "id": "43ZHCT0cAZBISjO8DG9PnE",
              "name": "Elvis Presley",
              "type": "artist",
              "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
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
            "spotify": "https://open.spotify.com/album/3ekkFrfotMsEAKc5g71GHk"
          },
          "href": "https://api.spotify.com/v1/albums/3ekkFrfotMsEAKc5g71GHk",
          "id": "3ekkFrfotMsEAKc5g71GHk",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/3a36159ea0439cd53d807ef0643d4e228406381a",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/d7bfcff6020fd48921a9f154a4266d7f4851cfa9",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/303c5223ef3da80078bdaedf50dceacbb951dc23",
              "width": 64
            }
          ],
          "name": "From Elvis in Memphis",
          "release_date": "1969-06-17",
          "release_date_precision": "day",
          "total_tracks": 16,
          "type": "album",
          "uri": "spotify:album:3ekkFrfotMsEAKc5g71GHk"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
            },
            "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
            "id": "43ZHCT0cAZBISjO8DG9PnE",
            "name": "Elvis Presley",
            "type": "artist",
            "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
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
        "duration_ms": 261279,
        "explicit": false,
        "external_ids": {
          "isrc": "USRC16901355"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/1H5IfYyIIAlgDX8zguUzns"
        },
        "href": "https://api.spotify.com/v1/tracks/1H5IfYyIIAlgDX8zguUzns",
        "id": "1H5IfYyIIAlgDX8zguUzns",
        "is_local": false,
        "name": "Suspicious Minds",
        "popularity": 72,
        "preview_url": "https://p.scdn.co/mp3-preview/7a298f247198d8736393e166cb9f9e32227f1886?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 13,
        "type": "track",
        "uri": "spotify:track:1H5IfYyIIAlgDX8zguUzns"
      },
      {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/77AiFEVeAVj2ORpC85QVJs"
              },
              "href": "https://api.spotify.com/v1/artists/77AiFEVeAVj2ORpC85QVJs",
              "id": "77AiFEVeAVj2ORpC85QVJs",
              "name": "Steve Aoki",
              "type": "artist",
              "uri": "spotify:artist:77AiFEVeAVj2ORpC85QVJs"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/4VMYDCV2IEDYJArk749S6m"
              },
              "href": "https://api.spotify.com/v1/artists/4VMYDCV2IEDYJArk749S6m",
              "id": "4VMYDCV2IEDYJArk749S6m",
              "name": "Daddy Yankee",
              "type": "artist",
              "uri": "spotify:artist:4VMYDCV2IEDYJArk749S6m"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/7MP4jhYmFEgb0AtiOkw55s"
              },
              "href": "https://api.spotify.com/v1/artists/7MP4jhYmFEgb0AtiOkw55s",
              "id": "7MP4jhYmFEgb0AtiOkw55s",
              "name": "Play-N-Skillz",
              "type": "artist",
              "uri": "spotify:artist:7MP4jhYmFEgb0AtiOkw55s"
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
            "spotify": "https://open.spotify.com/album/5LSqEb2yiUoWM91rUnvDjS"
          },
          "href": "https://api.spotify.com/v1/albums/5LSqEb2yiUoWM91rUnvDjS",
          "id": "5LSqEb2yiUoWM91rUnvDjS",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/548bf2eeca2c064835f369bc1540c1ecbd803ab6",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/e31e580cfe49ac51ba1177e3824a565abbfb3c6c",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/d6718a0c1b267048eaef2d3bd4b74780b617d03b",
              "width": 64
            }
          ],
          "name": "Azukita (Steve Aoki, Daddy Yankee, Play-N-Skillz & Elvis Crespo)",
          "release_date": "2018-02-02",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:5LSqEb2yiUoWM91rUnvDjS"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/77AiFEVeAVj2ORpC85QVJs"
            },
            "href": "https://api.spotify.com/v1/artists/77AiFEVeAVj2ORpC85QVJs",
            "id": "77AiFEVeAVj2ORpC85QVJs",
            "name": "Steve Aoki",
            "type": "artist",
            "uri": "spotify:artist:77AiFEVeAVj2ORpC85QVJs"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4VMYDCV2IEDYJArk749S6m"
            },
            "href": "https://api.spotify.com/v1/artists/4VMYDCV2IEDYJArk749S6m",
            "id": "4VMYDCV2IEDYJArk749S6m",
            "name": "Daddy Yankee",
            "type": "artist",
            "uri": "spotify:artist:4VMYDCV2IEDYJArk749S6m"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7MP4jhYmFEgb0AtiOkw55s"
            },
            "href": "https://api.spotify.com/v1/artists/7MP4jhYmFEgb0AtiOkw55s",
            "id": "7MP4jhYmFEgb0AtiOkw55s",
            "name": "Play-N-Skillz",
            "type": "artist",
            "uri": "spotify:artist:7MP4jhYmFEgb0AtiOkw55s"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1c22GXH30ijlOfXhfLz9Df"
            },
            "href": "https://api.spotify.com/v1/artists/1c22GXH30ijlOfXhfLz9Df",
            "id": "1c22GXH30ijlOfXhfLz9Df",
            "name": "Elvis Crespo",
            "type": "artist",
            "uri": "spotify:artist:1c22GXH30ijlOfXhfLz9Df"
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
        "duration_ms": 226161,
        "explicit": false,
        "external_ids": {
          "isrc": "USUS11800006"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/5e45GhSF18JYoLpaq2F48h"
        },
        "href": "https://api.spotify.com/v1/tracks/5e45GhSF18JYoLpaq2F48h",
        "id": "5e45GhSF18JYoLpaq2F48h",
        "is_local": false,
        "name": "Azukita (Steve Aoki, Daddy Yankee, Play-N-Skillz & Elvis Crespo)",
        "popularity": 75,
        "preview_url": "https://p.scdn.co/mp3-preview/021f88c286e21750422783d802150296d275aaae?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:5e45GhSF18JYoLpaq2F48h"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/5MynxBz4ZMqvUzpcxTZl4C"
              },
              "href": "https://api.spotify.com/v1/artists/5MynxBz4ZMqvUzpcxTZl4C",
              "id": "5MynxBz4ZMqvUzpcxTZl4C",
              "name": "Therapie TAXI",
              "type": "artist",
              "uri": "spotify:artist:5MynxBz4ZMqvUzpcxTZl4C"
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
            "spotify": "https://open.spotify.com/album/1j4pZyBTGUSvp3e5loBgez"
          },
          "href": "https://api.spotify.com/v1/albums/1j4pZyBTGUSvp3e5loBgez",
          "id": "1j4pZyBTGUSvp3e5loBgez",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/6eaf8ec6c0676c11ddb57d1b3bcd37acb718e225",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/cedd63b6cdbb8d1ec856f12219371b62a3b792fc",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/3911377f69f16dfd0839e6fe1ec3cef5be0ae39a",
              "width": 64
            }
          ],
          "name": "Hit Sale",
          "release_date": "2018-02-02",
          "release_date_precision": "day",
          "total_tracks": 14,
          "type": "album",
          "uri": "spotify:album:1j4pZyBTGUSvp3e5loBgez"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5MynxBz4ZMqvUzpcxTZl4C"
            },
            "href": "https://api.spotify.com/v1/artists/5MynxBz4ZMqvUzpcxTZl4C",
            "id": "5MynxBz4ZMqvUzpcxTZl4C",
            "name": "Therapie TAXI",
            "type": "artist",
            "uri": "spotify:artist:5MynxBz4ZMqvUzpcxTZl4C"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2pHk4wAmL7ofTAuvCIUWtv"
            },
            "href": "https://api.spotify.com/v1/artists/2pHk4wAmL7ofTAuvCIUWtv",
            "id": "2pHk4wAmL7ofTAuvCIUWtv",
            "name": "Roméo Elvis",
            "type": "artist",
            "uri": "spotify:artist:2pHk4wAmL7ofTAuvCIUWtv"
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
        "duration_ms": 184400,
        "explicit": false,
        "external_ids": {
          "isrc": "FR7O51700210"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/3yndKI4zWEyC36BQYrdKBA"
        },
        "href": "https://api.spotify.com/v1/tracks/3yndKI4zWEyC36BQYrdKBA",
        "id": "3yndKI4zWEyC36BQYrdKBA",
        "is_local": false,
        "name": "Hit Sale (feat. Roméo Elvis)",
        "popularity": 69,
        "preview_url": "https://p.scdn.co/mp3-preview/d8a0f59d3ea2bc7fbede12123d66a7559c2e1c8c?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:3yndKI4zWEyC36BQYrdKBA"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
              },
              "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
              "id": "43ZHCT0cAZBISjO8DG9PnE",
              "name": "Elvis Presley",
              "type": "artist",
              "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
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
            "spotify": "https://open.spotify.com/album/0C3t1htEDTFKcg7F2rNbek"
          },
          "href": "https://api.spotify.com/v1/albums/0C3t1htEDTFKcg7F2rNbek",
          "id": "0C3t1htEDTFKcg7F2rNbek",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/f3c95ddbd77813737616eb327b4e31106d0b2bab",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/cc7323d63e79dd46fea998f99ef459544114b01c",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/3cbd4a9b70b83f98d8ef8691c6a5f1c2c32f1bcc",
              "width": 64
            }
          ],
          "name": "Elvis' Golden Records",
          "release_date": "1958-03-21",
          "release_date_precision": "day",
          "total_tracks": 14,
          "type": "album",
          "uri": "spotify:album:0C3t1htEDTFKcg7F2rNbek"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
            },
            "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
            "id": "43ZHCT0cAZBISjO8DG9PnE",
            "name": "Elvis Presley",
            "type": "artist",
            "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
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
        "duration_ms": 136026,
        "explicit": false,
        "external_ids": {
          "isrc": "USRC15602857"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/64Ny7djQ6rNJspquof2KoX"
        },
        "href": "https://api.spotify.com/v1/tracks/64Ny7djQ6rNJspquof2KoX",
        "id": "64Ny7djQ6rNJspquof2KoX",
        "is_local": false,
        "name": "Hound Dog",
        "popularity": 70,
        "preview_url": "https://p.scdn.co/mp3-preview/f683997c027a50649aa3b6c627cd67bd1a9364f5?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:64Ny7djQ6rNJspquof2KoX"
      },
      {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/6VD4UEUPvtsemqD3mmTqCR"
              },
              "href": "https://api.spotify.com/v1/artists/6VD4UEUPvtsemqD3mmTqCR",
              "id": "6VD4UEUPvtsemqD3mmTqCR",
              "name": "Deorro",
              "type": "artist",
              "uri": "spotify:artist:6VD4UEUPvtsemqD3mmTqCR"
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
            "spotify": "https://open.spotify.com/album/1tAISk8OvvhU8V5QGuXyJS"
          },
          "href": "https://api.spotify.com/v1/albums/1tAISk8OvvhU8V5QGuXyJS",
          "id": "1tAISk8OvvhU8V5QGuXyJS",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/0cad93a7dd99b14165d133284b2894c648d4a857",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/c939ab508d040f2ae48633e4aba57f90ba514181",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/6e055f6cff66c800a53a7797cb89a428be36391f",
              "width": 64
            }
          ],
          "name": "Bailar (Radio Edit)",
          "release_date": "2016-04-22",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:1tAISk8OvvhU8V5QGuXyJS"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6VD4UEUPvtsemqD3mmTqCR"
            },
            "href": "https://api.spotify.com/v1/artists/6VD4UEUPvtsemqD3mmTqCR",
            "id": "6VD4UEUPvtsemqD3mmTqCR",
            "name": "Deorro",
            "type": "artist",
            "uri": "spotify:artist:6VD4UEUPvtsemqD3mmTqCR"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1c22GXH30ijlOfXhfLz9Df"
            },
            "href": "https://api.spotify.com/v1/artists/1c22GXH30ijlOfXhfLz9Df",
            "id": "1c22GXH30ijlOfXhfLz9Df",
            "name": "Elvis Crespo",
            "type": "artist",
            "uri": "spotify:artist:1c22GXH30ijlOfXhfLz9Df"
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
        "duration_ms": 137661,
        "explicit": false,
        "external_ids": {
          "isrc": "USUS11600173"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/45sGyAtAxD6efaN0bJAFgh"
        },
        "href": "https://api.spotify.com/v1/tracks/45sGyAtAxD6efaN0bJAFgh",
        "id": "45sGyAtAxD6efaN0bJAFgh",
        "is_local": false,
        "name": "Bailar - Radio Edit",
        "popularity": 69,
        "preview_url": "https://p.scdn.co/mp3-preview/e40b1079f108752c2346088244baca7fe0e5229b?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:45sGyAtAxD6efaN0bJAFgh"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
              },
              "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
              "id": "43ZHCT0cAZBISjO8DG9PnE",
              "name": "Elvis Presley",
              "type": "artist",
              "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
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
            "spotify": "https://open.spotify.com/album/3gpHiNAmT5oXVxe6ewTGuN"
          },
          "href": "https://api.spotify.com/v1/albums/3gpHiNAmT5oXVxe6ewTGuN",
          "id": "3gpHiNAmT5oXVxe6ewTGuN",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/7a1a08f2c1b22eca8b9b775d002c4a6d248a6c9b",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/690a5b3dfd767eb234e7efd168867d7106457619",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/a58c531a579e9e0fb9367a59ee1bc50a912dfc01",
              "width": 64
            }
          ],
          "name": "Elvis (Fool)",
          "release_date": "1973-07-16",
          "release_date_precision": "day",
          "total_tracks": 16,
          "type": "album",
          "uri": "spotify:album:3gpHiNAmT5oXVxe6ewTGuN"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/43ZHCT0cAZBISjO8DG9PnE"
            },
            "href": "https://api.spotify.com/v1/artists/43ZHCT0cAZBISjO8DG9PnE",
            "id": "43ZHCT0cAZBISjO8DG9PnE",
            "name": "Elvis Presley",
            "type": "artist",
            "uri": "spotify:artist:43ZHCT0cAZBISjO8DG9PnE"
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
        "duration_ms": 170293,
        "explicit": false,
        "external_ids": {
          "isrc": "USRC18705934"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/7zMUCLm1TN9o9JlLISztxO"
        },
        "href": "https://api.spotify.com/v1/tracks/7zMUCLm1TN9o9JlLISztxO",
        "id": "7zMUCLm1TN9o9JlLISztxO",
        "is_local": false,
        "name": "Burning Love",
        "popularity": 69,
        "preview_url": "https://p.scdn.co/mp3-preview/8120be95b750b8783840768f7d458ba8a4a972fb?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 13,
        "type": "track",
        "uri": "spotify:track:7zMUCLm1TN9o9JlLISztxO"
      }
    ],
    "limit": 10,
    "next": "https://api.spotify.com/v1/search?query=elvis&type=track&market=CA&offset=10&limit=10",
    "offset": 0,
    "previous": null,
    "total": 36889
  },
  "playlists": {
    "href": "https://api.spotify.com/v1/search?query=elvis&type=playlist&market=CA&offset=0&limit=10",
    "items": [
      {
        "collaborative": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX50yT1VeARvT"
        },
        "href": "https://api.spotify.com/v1/playlists/37i9dQZF1DX50yT1VeARvT",
        "id": "37i9dQZF1DX50yT1VeARvT",
        "images": [
          {
            "height": null,
            "url": "https://pl.scdn.co/images/pl/default/44d9eb9343a18ffb8601eccf430249bb2f8b5a0d",
            "width": null
          }
        ],
        "name": "This Is Elvis Presley",
        "owner": {
          "display_name": "Spotify",
          "external_urls": {
            "spotify": "https://open.spotify.com/user/spotify"
          },
          "href": "https://api.spotify.com/v1/users/spotify",
          "id": "spotify",
          "type": "user",
          "uri": "spotify:user:spotify"
        },
        "primary_color": null,
        "public": null,
        "snapshot_id": "MTU1NDIxMzYzOSwwMDAwMDAyNjAwMDAwMTY5ZGU1YTE1MmIwMDAwMDE2OGUyNDEyYTM0",
        "tracks": {
          "href": "https://api.spotify.com/v1/playlists/37i9dQZF1DX50yT1VeARvT/tracks",
          "total": 70
        },
        "type": "playlist",
        "uri": "spotify:playlist:37i9dQZF1DX50yT1VeARvT"
      },
      {
        "collaborative": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/playlist/5DSH3KEuGZiqjBVP0sdd2s"
        },
        "href": "https://api.spotify.com/v1/playlists/5DSH3KEuGZiqjBVP0sdd2s",
        "id": "5DSH3KEuGZiqjBVP0sdd2s",
        "images": [
          {
            "height": null,
            "url": "https://pl.scdn.co/images/pl/default/1d96b157cd722cea16b7fa97df33d6e8136b1725",
            "width": null
          }
        ],
        "name": "Elvis Presley: Top Tracks",
        "owner": {
          "display_name": "Elvis Presley",
          "external_urls": {
            "spotify": "https://open.spotify.com/user/elvispresleymusic"
          },
          "href": "https://api.spotify.com/v1/users/elvispresleymusic",
          "id": "elvispresleymusic",
          "type": "user",
          "uri": "spotify:user:elvispresleymusic"
        },
        "primary_color": null,
        "public": null,
        "snapshot_id": "MjQ3LDM3YTJjYjVhMWE1NTcyMTdhNGQzMzFkYWU0MDkwNWE0MzQyMzVhNjk=",
        "tracks": {
          "href": "https://api.spotify.com/v1/playlists/5DSH3KEuGZiqjBVP0sdd2s/tracks",
          "total": 77
        },
        "type": "playlist",
        "uri": "spotify:playlist:5DSH3KEuGZiqjBVP0sdd2s"
      },
      {
        "collaborative": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/playlist/0FQnUrWmL0uI1F77pkI1Ez"
        },
        "href": "https://api.spotify.com/v1/playlists/0FQnUrWmL0uI1F77pkI1Ez",
        "id": "0FQnUrWmL0uI1F77pkI1Ez",
        "images": [
          {
            "height": null,
            "url": "https://pl.scdn.co/images/pl/default/35b44e892f216e8228539668c8edc831a1b4af27",
            "width": null
          }
        ],
        "name": "Elvis: Love",
        "owner": {
          "display_name": "Elvis Presley",
          "external_urls": {
            "spotify": "https://open.spotify.com/user/elvispresleymusic"
          },
          "href": "https://api.spotify.com/v1/users/elvispresleymusic",
          "id": "elvispresleymusic",
          "type": "user",
          "uri": "spotify:user:elvispresleymusic"
        },
        "primary_color": null,
        "public": null,
        "snapshot_id": "MzksNjlhNTFhYWNiODdhNDliNTBiOGYyOGZiM2FmMjUxMDRlN2M5ODQwOQ==",
        "tracks": {
          "href": "https://api.spotify.com/v1/playlists/0FQnUrWmL0uI1F77pkI1Ez/tracks",
          "total": 60
        },
        "type": "playlist",
        "uri": "spotify:playlist:0FQnUrWmL0uI1F77pkI1Ez"
      },
      {
        "collaborative": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/playlist/0Vj341QGojN4ybBbHhXseE"
        },
        "href": "https://api.spotify.com/v1/playlists/0Vj341QGojN4ybBbHhXseE",
        "id": "0Vj341QGojN4ybBbHhXseE",
        "images": [
          {
            "height": 640,
            "url": "https://mosaic.scdn.co/640/0fd54e67c0323f2a663030ee71e66b1c74bb20524a07294589615dcb58f1754c5003caca8cca841d952fe5480323198f9434bfbf4c49ac8062e50e10e97369caa1b9be314626c53ba8670d7560ce1f51",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://mosaic.scdn.co/300/0fd54e67c0323f2a663030ee71e66b1c74bb20524a07294589615dcb58f1754c5003caca8cca841d952fe5480323198f9434bfbf4c49ac8062e50e10e97369caa1b9be314626c53ba8670d7560ce1f51",
            "width": 300
          },
          {
            "height": 60,
            "url": "https://mosaic.scdn.co/60/0fd54e67c0323f2a663030ee71e66b1c74bb20524a07294589615dcb58f1754c5003caca8cca841d952fe5480323198f9434bfbf4c49ac8062e50e10e97369caa1b9be314626c53ba8670d7560ce1f51",
            "width": 60
          }
        ],
        "name": "Elvis Gospel",
        "owner": {
          "display_name": "Rebecca Blacksher",
          "external_urls": {
            "spotify": "https://open.spotify.com/user/1235084764"
          },
          "href": "https://api.spotify.com/v1/users/1235084764",
          "id": "1235084764",
          "type": "user",
          "uri": "spotify:user:1235084764"
        },
        "primary_color": null,
        "public": null,
        "snapshot_id": "MjAyLDcwYTdiOTQwMjAxODI5ZTMwOTMyNTVjZGRlYTY1NmYxMDZmODVlM2Q=",
        "tracks": {
          "href": "https://api.spotify.com/v1/playlists/0Vj341QGojN4ybBbHhXseE/tracks",
          "total": 114
        },
        "type": "playlist",
        "uri": "spotify:playlist:0Vj341QGojN4ybBbHhXseE"
      },
      {
        "collaborative": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX1b2I23e8eFe"
        },
        "href": "https://api.spotify.com/v1/playlists/37i9dQZF1DX1b2I23e8eFe",
        "id": "37i9dQZF1DX1b2I23e8eFe",
        "images": [
          {
            "height": null,
            "url": "https://pl.scdn.co/images/pl/default/dac2296141513c0b3d0306e98d90815e8d3348f3",
            "width": null
          }
        ],
        "name": "This Is Roméo Elvis",
        "owner": {
          "display_name": "Spotify",
          "external_urls": {
            "spotify": "https://open.spotify.com/user/spotify"
          },
          "href": "https://api.spotify.com/v1/users/spotify",
          "id": "spotify",
          "type": "user",
          "uri": "spotify:user:spotify"
        },
        "primary_color": null,
        "public": null,
        "snapshot_id": "MTU1MzY4NTg3NCwwMDAwMDAwNjAwMDAwMTY5YmVlNTA2OGYwMDAwMDE2OWJlZTRkYTU3",
        "tracks": {
          "href": "https://api.spotify.com/v1/playlists/37i9dQZF1DX1b2I23e8eFe/tracks",
          "total": 50
        },
        "type": "playlist",
        "uri": "spotify:playlist:37i9dQZF1DX1b2I23e8eFe"
      },
      {
        "collaborative": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX1dwn4H0X3oa"
        },
        "href": "https://api.spotify.com/v1/playlists/37i9dQZF1DX1dwn4H0X3oa",
        "id": "37i9dQZF1DX1dwn4H0X3oa",
        "images": [
          {
            "height": null,
            "url": "https://pl.scdn.co/images/pl/default/77dd3bd10f25851c4a2d5881dce6790a80348877",
            "width": null
          }
        ],
        "name": "This Is: Elvis Crespo",
        "owner": {
          "display_name": "Spotify",
          "external_urls": {
            "spotify": "https://open.spotify.com/user/spotify"
          },
          "href": "https://api.spotify.com/v1/users/spotify",
          "id": "spotify",
          "type": "user",
          "uri": "spotify:user:spotify"
        },
        "primary_color": null,
        "public": null,
        "snapshot_id": "MTU1MjA1NjkyNCwwMDAwMDAxNDAwMDAwMTY5NWRjZDM3ZDUwMDAwMDE2ODk4Y2RkYzMy",
        "tracks": {
          "href": "https://api.spotify.com/v1/playlists/37i9dQZF1DX1dwn4H0X3oa/tracks",
          "total": 46
        },
        "type": "playlist",
        "uri": "spotify:playlist:37i9dQZF1DX1dwn4H0X3oa"
      },
      {
        "collaborative": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX1sLrJlNJxjb"
        },
        "href": "https://api.spotify.com/v1/playlists/37i9dQZF1DX1sLrJlNJxjb",
        "id": "37i9dQZF1DX1sLrJlNJxjb",
        "images": [
          {
            "height": null,
            "url": "https://pl.scdn.co/images/pl/default/f9ced7811b2576fa52f2e1cc4d334430e490f89f",
            "width": null
          }
        ],
        "name": "This is Elvis Costello",
        "owner": {
          "display_name": "Spotify",
          "external_urls": {
            "spotify": "https://open.spotify.com/user/spotify"
          },
          "href": "https://api.spotify.com/v1/users/spotify",
          "id": "spotify",
          "type": "user",
          "uri": "spotify:user:spotify"
        },
        "primary_color": null,
        "public": null,
        "snapshot_id": "MTU0ODc1MDg0OCwwMDAwMDAwMzAwMDAwMTY2NjY2ZjQ0OWMwMDAwMDE2ODk4YmU4Mjlh",
        "tracks": {
          "href": "https://api.spotify.com/v1/playlists/37i9dQZF1DX1sLrJlNJxjb/tracks",
          "total": 76
        },
        "type": "playlist",
        "uri": "spotify:playlist:37i9dQZF1DX1sLrJlNJxjb"
      },
      {
        "collaborative": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/playlist/2KYWvSCwmk4naSndmgkwEX"
        },
        "href": "https://api.spotify.com/v1/playlists/2KYWvSCwmk4naSndmgkwEX",
        "id": "2KYWvSCwmk4naSndmgkwEX",
        "images": [
          {
            "height": null,
            "url": "https://pl.scdn.co/images/pl/default/bbff1bdc02e05bcf8e98b21f4b8a086fda3293d4",
            "width": null
          }
        ],
        "name": "Elvis: Gospel",
        "owner": {
          "display_name": "Elvis Presley",
          "external_urls": {
            "spotify": "https://open.spotify.com/user/elvispresleymusic"
          },
          "href": "https://api.spotify.com/v1/users/elvispresleymusic",
          "id": "elvispresleymusic",
          "type": "user",
          "uri": "spotify:user:elvispresleymusic"
        },
        "primary_color": null,
        "public": null,
        "snapshot_id": "NDEsMDIzY2MwZTg0ZTc5MWYwYjdmNGY5ZTdiNDI3MjMxMjlkOTE3NjExNg==",
        "tracks": {
          "href": "https://api.spotify.com/v1/playlists/2KYWvSCwmk4naSndmgkwEX/tracks",
          "total": 42
        },
        "type": "playlist",
        "uri": "spotify:playlist:2KYWvSCwmk4naSndmgkwEX"
      },
      {
        "collaborative": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/playlist/2dE8cHrGXMB9bgEQjzSzzT"
        },
        "href": "https://api.spotify.com/v1/playlists/2dE8cHrGXMB9bgEQjzSzzT",
        "id": "2dE8cHrGXMB9bgEQjzSzzT",
        "images": [
          {
            "height": 640,
            "url": "https://mosaic.scdn.co/640/08a03fd8e22d7dd838e49fdaa1b17cc1511571ea34c4de4539326548e34a21b49b70d11fca4cc9c2450e44e9dcc333ae2e77da8c354ada3286f5fbb19bc27ef6eca71df5faf0446237e8cc4a4ad1602b",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://mosaic.scdn.co/300/08a03fd8e22d7dd838e49fdaa1b17cc1511571ea34c4de4539326548e34a21b49b70d11fca4cc9c2450e44e9dcc333ae2e77da8c354ada3286f5fbb19bc27ef6eca71df5faf0446237e8cc4a4ad1602b",
            "width": 300
          },
          {
            "height": 60,
            "url": "https://mosaic.scdn.co/60/08a03fd8e22d7dd838e49fdaa1b17cc1511571ea34c4de4539326548e34a21b49b70d11fca4cc9c2450e44e9dcc333ae2e77da8c354ada3286f5fbb19bc27ef6eca71df5faf0446237e8cc4a4ad1602b",
            "width": 60
          }
        ],
        "name": "She – Elvis Costello",
        "owner": {
          "display_name": "Ingrid Schager",
          "external_urls": {
            "spotify": "https://open.spotify.com/user/ingridschager"
          },
          "href": "https://api.spotify.com/v1/users/ingridschager",
          "id": "ingridschager",
          "type": "user",
          "uri": "spotify:user:ingridschager"
        },
        "primary_color": null,
        "public": null,
        "snapshot_id": "NDUsYTYyNDAyOTQzZGFlNmE1NGY0Njk1ZTFkOGEyYTE4ZGQwNzVjMGI3NA==",
        "tracks": {
          "href": "https://api.spotify.com/v1/playlists/2dE8cHrGXMB9bgEQjzSzzT/tracks",
          "total": 55
        },
        "type": "playlist",
        "uri": "spotify:playlist:2dE8cHrGXMB9bgEQjzSzzT"
      },
      {
        "collaborative": false,
        "external_urls": {
          "spotify": "https://open.spotify.com/playlist/4BAYYDIepgalf2ESNCwUVa"
        },
        "href": "https://api.spotify.com/v1/playlists/4BAYYDIepgalf2ESNCwUVa",
        "id": "4BAYYDIepgalf2ESNCwUVa",
        "images": [
          {
            "height": null,
            "url": "https://pl.scdn.co/images/pl/default/833aef69641de10b5e4c09e608e1cbb159f91774",
            "width": null
          }
        ],
        "name": "Normal – Roméo Elvis",
        "owner": {
          "display_name": "funkyfreshofficial",
          "external_urls": {
            "spotify": "https://open.spotify.com/user/funkyfreshofficial"
          },
          "href": "https://api.spotify.com/v1/users/funkyfreshofficial",
          "id": "funkyfreshofficial",
          "type": "user",
          "uri": "spotify:user:funkyfreshofficial"
        },
        "primary_color": null,
        "public": null,
        "snapshot_id": "NDUxLDUyMWYwYzUyMDczNDlkY2FjNDQ0Njg4MGJmZDI4NWZjZjI5YWMzZDY=",
        "tracks": {
          "href": "https://api.spotify.com/v1/playlists/4BAYYDIepgalf2ESNCwUVa/tracks",
          "total": 29
        },
        "type": "playlist",
        "uri": "spotify:playlist:4BAYYDIepgalf2ESNCwUVa"
      }
    ],
    "limit": 10,
    "next": "https://api.spotify.com/v1/search?query=elvis&type=playlist&market=CA&offset=10&limit=10",
    "offset": 0,
    "previous": null,
    "total": 22930
  }
}
"""

artists = json.loads(_jartists)
all_types = json.loads(_jalltypes)
