import json

_jplaylistpartial = """
{
  "description": "Having friends over for dinner? Here's the perfect playlist.",
  "id": "59ZbFPES4DQwEjBpWHzrtC",
  "name": "Dinner with Friends",
  "tracks": {
    "items": [
      {
        "track": {
          "id": "2zhk0kypGeOPsaaZcjyc14",
          "name": "Burning House",
          "uri": "spotify:track:2zhk0kypGeOPsaaZcjyc14"
        }
      },
      {
        "track": {
          "id": "10tMVFMvd9224Zcq4A5dRL",
          "name": "Collide - Chris Lord-Alge Mix aka Radio Edit",
          "uri": "spotify:track:10tMVFMvd9224Zcq4A5dRL"
        }
      },
      {
        "track": {
          "id": "2RttW7RAu5nOAfq6YFvApB",
          "name": "Happier",
          "uri": "spotify:track:2RttW7RAu5nOAfq6YFvApB"
        }
      },
      {
        "track": {
          "id": "1sXUWdKx03aP9Gmzft58rt",
          "name": "Issues",
          "uri": "spotify:track:1sXUWdKx03aP9Gmzft58rt"
        }
      },
      {
        "track": {
          "id": "2pV8RpdLemcyMWko8dASVt",
          "name": "Like I'm Gonna Lose You",
          "uri": "spotify:track:2pV8RpdLemcyMWko8dASVt"
        }
      },
      {
        "track": {
          "id": "3CtuvNHSsSwXe1y4lqDSkh",
          "name": "Gotta Thing About You - Acoustic Version",
          "uri": "spotify:track:3CtuvNHSsSwXe1y4lqDSkh"
        }
      },
      {
        "track": {
          "id": "6xM8oBy40nK1rOd8WmoOPx",
          "name": "Last Request",
          "uri": "spotify:track:6xM8oBy40nK1rOd8WmoOPx"
        }
      },
      {
        "track": {
          "id": "0xBsZrUrsZcCCrpxryZDHc",
          "name": "Liability",
          "uri": "spotify:track:0xBsZrUrsZcCCrpxryZDHc"
        }
      },
      {
        "track": {
          "id": "4qqwyDhp0p0kwJMZULa0VN",
          "name": "Empty Pack Of Cigarettes - From \\"Fifty Shades Darker (Original Motion Picture Soundtrack)\\"",
          "uri": "spotify:track:4qqwyDhp0p0kwJMZULa0VN"
        }
      },
      {
        "track": {
          "id": "429EttO8gs0bDo2SQfUNSm",
          "name": "Georgia",
          "uri": "spotify:track:429EttO8gs0bDo2SQfUNSm"
        }
      },
      {
        "track": {
          "id": "2pJZ1v8HezrAoZ0Fhzby92",
          "name": "What Do I Know?",
          "uri": "spotify:track:2pJZ1v8HezrAoZ0Fhzby92"
        }
      },
      {
        "track": {
          "id": "3uBbvynFWlF041WzNVHd1d",
          "name": "Used to Love U",
          "uri": "spotify:track:3uBbvynFWlF041WzNVHd1d"
        }
      },
      {
        "track": {
          "id": "5hYTyyh2odQKphUbMqc5gN",
          "name": "How Far I'll Go - From \\"Moana\\"",
          "uri": "spotify:track:5hYTyyh2odQKphUbMqc5gN"
        }
      },
      {
        "track": {
          "id": "3cNjgVBKTJ1SvKhunrCdVy",
          "name": "Please Don't Go",
          "uri": "spotify:track:3cNjgVBKTJ1SvKhunrCdVy"
        }
      },
      {
        "track": {
          "id": "6CAJfBlMsYUtkI7fBAXE6Y",
          "name": "I'm In Love with You",
          "uri": "spotify:track:6CAJfBlMsYUtkI7fBAXE6Y"
        }
      },
      {
        "track": {
          "id": "1Pw5C4N6Fn5E4mGCxmbbVa",
          "name": "Say You Won't Let Go",
          "uri": "spotify:track:1Pw5C4N6Fn5E4mGCxmbbVa"
        }
      },
      {
        "track": {
          "id": "5jRMDFLiQaa4PKfabTMNYQ",
          "name": "Water Under the Bridge",
          "uri": "spotify:track:5jRMDFLiQaa4PKfabTMNYQ"
        }
      },
      {
        "track": {
          "id": "2JR7RCUN6pZIoyNzaqxdUa",
          "name": "Cassidy",
          "uri": "spotify:track:2JR7RCUN6pZIoyNzaqxdUa"
        }
      },
      {
        "track": {
          "id": "2rizacJSyD9S1IQUxUxnsK",
          "name": "All We Know",
          "uri": "spotify:track:2rizacJSyD9S1IQUxUxnsK"
        }
      },
      {
        "track": {
          "id": "0j2WBxWZnWti5TpSxjJvPb",
          "name": "Love on the Weekend",
          "uri": "spotify:track:0j2WBxWZnWti5TpSxjJvPb"
        }
      },
      {
        "track": {
          "id": "1bpAGufvAgqEIob4V1k7mP",
          "name": "Nervous",
          "uri": "spotify:track:1bpAGufvAgqEIob4V1k7mP"
        }
      },
      {
        "track": {
          "id": "5vGpdYEtZbiBVq1dT6SCqI",
          "name": "Home",
          "uri": "spotify:track:5vGpdYEtZbiBVq1dT6SCqI"
        }
      },
      {
        "track": {
          "id": "02WacdrRpm4zlP8H7X6bnQ",
          "name": "Dancing On My Own",
          "uri": "spotify:track:02WacdrRpm4zlP8H7X6bnQ"
        }
      },
      {
        "track": {
          "id": "6SJ1qt2W5A4AEdxjqajMWU",
          "name": "I Just Wanna Love You",
          "uri": "spotify:track:6SJ1qt2W5A4AEdxjqajMWU"
        }
      },
      {
        "track": {
          "id": "5ULRlgiSPSKTaJN1vU9yso",
          "name": "Shape of You - Acoustic",
          "uri": "spotify:track:5ULRlgiSPSKTaJN1vU9yso"
        }
      },
      {
        "track": {
          "id": "6aG68QSwv0hgNTq90I2GOE",
          "name": "Everglow - Single Version, Radio Edit",
          "uri": "spotify:track:6aG68QSwv0hgNTq90I2GOE"
        }
      },
      {
        "track": {
          "id": "2TKdUg2cI4b44M6XSKF2QG",
          "name": "Reflection",
          "uri": "spotify:track:2TKdUg2cI4b44M6XSKF2QG"
        }
      },
      {
        "track": {
          "id": "0MYplMrSTCJ6WnTNqAOd1P",
          "name": "WALLS",
          "uri": "spotify:track:0MYplMrSTCJ6WnTNqAOd1P"
        }
      },
      {
        "track": {
          "id": "7fa1oiFqQFhlO8ghtLIGpR",
          "name": "Beautiful To Me",
          "uri": "spotify:track:7fa1oiFqQFhlO8ghtLIGpR"
        }
      },
      {
        "track": {
          "id": "6BWTZwXamKhjdYlicjjVjB",
          "name": "Think About You",
          "uri": "spotify:track:6BWTZwXamKhjdYlicjjVjB"
        }
      },
      {
        "track": {
          "id": "10THcVz6xpbsdmxzdqCVZV",
          "name": "Something Worth Saving",
          "uri": "spotify:track:10THcVz6xpbsdmxzdqCVZV"
        }
      },
      {
        "track": {
          "id": "5P6ZBMWS66FVo6deJaDdHy",
          "name": "Dust to Dust",
          "uri": "spotify:track:5P6ZBMWS66FVo6deJaDdHy"
        }
      },
      {
        "track": {
          "id": "4h0zU3O9R5xzuTmNO7dNDU",
          "name": "Lost Boy",
          "uri": "spotify:track:4h0zU3O9R5xzuTmNO7dNDU"
        }
      },
      {
        "track": {
          "id": "059ACLUOyEcdruA2m9f2jd",
          "name": "Unstoppable",
          "uri": "spotify:track:059ACLUOyEcdruA2m9f2jd"
        }
      },
      {
        "track": {
          "id": "351JigVlGvReFbzSv6G318",
          "name": "In The Meantime",
          "uri": "spotify:track:351JigVlGvReFbzSv6G318"
        }
      },
      {
        "track": {
          "id": "48EjSdYh8wz2gBxxqzrsLe",
          "name": "Cranes in the Sky",
          "uri": "spotify:track:48EjSdYh8wz2gBxxqzrsLe"
        }
      },
      {
        "track": {
          "id": "1obcO5plIza6FtGmMD9ceN",
          "name": "Running Out - Live From The Studio / 2016",
          "uri": "spotify:track:1obcO5plIza6FtGmMD9ceN"
        }
      },
      {
        "track": {
          "id": "4CHJIqkY1bvrvfpP3qb2qi",
          "name": "Stitches - Acoustic Version",
          "uri": "spotify:track:4CHJIqkY1bvrvfpP3qb2qi"
        }
      },
      {
        "track": {
          "id": "5JhtfNV7PsT5L5nrIJ4IUp",
          "name": "Dandelion",
          "uri": "spotify:track:5JhtfNV7PsT5L5nrIJ4IUp"
        }
      },
      {
        "track": {
          "id": "5TGZ9gUY5LoJLxDg7B5H7w",
          "name": "Summertime of Our Lives",
          "uri": "spotify:track:5TGZ9gUY5LoJLxDg7B5H7w"
        }
      },
      {
        "track": {
          "id": "5fMInRpERS8jP2zPz6QyUI",
          "name": "Love And Happiness",
          "uri": "spotify:track:5fMInRpERS8jP2zPz6QyUI"
        }
      },
      {
        "track": {
          "id": "7ilS0BPWS8ek2P2GaxH3cP",
          "name": "When We Were Young",
          "uri": "spotify:track:7ilS0BPWS8ek2P2GaxH3cP"
        }
      },
      {
        "track": {
          "id": "4T2SmVJPtDdugk5j5xV1d5",
          "name": "You And Me",
          "uri": "spotify:track:4T2SmVJPtDdugk5j5xV1d5"
        }
      },
      {
        "track": {
          "id": "7rR5X9RKz5VprclstYOLb5",
          "name": "Breakers Roar",
          "uri": "spotify:track:7rR5X9RKz5VprclstYOLb5"
        }
      },
      {
        "track": {
          "id": "6OiZEXU5hBZHmnvRhaKbl5",
          "name": "Attention",
          "uri": "spotify:track:6OiZEXU5hBZHmnvRhaKbl5"
        }
      },
      {
        "track": {
          "id": "5GkqK9pWQDOSZ1NKA1hCmD",
          "name": "To Lose Someone",
          "uri": "spotify:track:5GkqK9pWQDOSZ1NKA1hCmD"
        }
      },
      {
        "track": {
          "id": "37R0bQOQj5a7DOqh1TGzvB",
          "name": "One Call Away",
          "uri": "spotify:track:37R0bQOQj5a7DOqh1TGzvB"
        }
      },
      {
        "track": {
          "id": "25IjPQGriH6U43pgITzSQz",
          "name": "After All This Time",
          "uri": "spotify:track:25IjPQGriH6U43pgITzSQz"
        }
      },
      {
        "track": {
          "id": "2HLd7alxKkXHU2KmbGUUVm",
          "name": "Bridge",
          "uri": "spotify:track:2HLd7alxKkXHU2KmbGUUVm"
        }
      },
      {
        "track": {
          "id": "2so9nFRdufwNO4A5Bmhqwd",
          "name": "Diamond Mind",
          "uri": "spotify:track:2so9nFRdufwNO4A5Bmhqwd"
        }
      },
      {
        "track": {
          "id": "1X0mseEKRtcotfixQOCNR3",
          "name": "The Desert Babbler",
          "uri": "spotify:track:1X0mseEKRtcotfixQOCNR3"
        }
      },
      {
        "track": {
          "id": "3AbBnwdMSurOx3KgsyBdXe",
          "name": "Better Now",
          "uri": "spotify:track:3AbBnwdMSurOx3KgsyBdXe"
        }
      },
      {
        "track": {
          "id": "6SdUtkLRQtzXzsEHjEGHna",
          "name": "Here Is Where Your Love Belongs",
          "uri": "spotify:track:6SdUtkLRQtzXzsEHjEGHna"
        }
      },
      {
        "track": {
          "id": "06KyNuuMOX1ROXRhj787tj",
          "name": "We Don't Talk Anymore (feat. Selena Gomez)",
          "uri": "spotify:track:06KyNuuMOX1ROXRhj787tj"
        }
      },
      {
        "track": {
          "id": "5NerQeQcH7IbwZOEjCenst",
          "name": "Do You Remember",
          "uri": "spotify:track:5NerQeQcH7IbwZOEjCenst"
        }
      },
      {
        "track": {
          "id": "1JIonCKtbUUkRIeEJrQBGU",
          "name": "Comeback Kid",
          "uri": "spotify:track:1JIonCKtbUUkRIeEJrQBGU"
        }
      },
      {
        "track": {
          "id": "2Cj2XFOMBT8IrT0aapNTee",
          "name": "Heartbeat",
          "uri": "spotify:track:2Cj2XFOMBT8IrT0aapNTee"
        }
      },
      {
        "track": {
          "id": "5REdxRARKVoJuZppmwglN4",
          "name": "Solid Ground",
          "uri": "spotify:track:5REdxRARKVoJuZppmwglN4"
        }
      },
      {
        "track": {
          "id": "2WOpBtXX02RS4UCzBholDq",
          "name": "I Don't Want to Change You",
          "uri": "spotify:track:2WOpBtXX02RS4UCzBholDq"
        }
      },
      {
        "track": {
          "id": "6FOyzhp375u8DapDyQqGTh",
          "name": "Tiger Striped Sky",
          "uri": "spotify:track:6FOyzhp375u8DapDyQqGTh"
        }
      },
      {
        "track": {
          "id": "0n2bvWvMwr0gbjcuTm92eW",
          "name": "Love",
          "uri": "spotify:track:0n2bvWvMwr0gbjcuTm92eW"
        }
      },
      {
        "track": {
          "id": "0eCkBrobTQFiBVqa1p92KA",
          "name": "Birthday",
          "uri": "spotify:track:0eCkBrobTQFiBVqa1p92KA"
        }
      },
      {
        "track": {
          "id": "5fX2oPyLCe5mBKqGDbOWqC",
          "name": "When You Love Someone",
          "uri": "spotify:track:5fX2oPyLCe5mBKqGDbOWqC"
        }
      },
      {
        "track": {
          "id": "6xraWJ8FdIJ8c8HpwXhNgs",
          "name": "Windy",
          "uri": "spotify:track:6xraWJ8FdIJ8c8HpwXhNgs"
        }
      },
      {
        "track": {
          "id": "45tEJcu0I1GRXVwxpKeAS0",
          "name": "Hey Stranger",
          "uri": "spotify:track:45tEJcu0I1GRXVwxpKeAS0"
        }
      },
      {
        "track": {
          "id": "2nI6aT3cnPFoXQ1L705wcY",
          "name": "Some Type Of Love",
          "uri": "spotify:track:2nI6aT3cnPFoXQ1L705wcY"
        }
      },
      {
        "track": {
          "id": "1OBlp2GgUQbPMtGNYg4Kdn",
          "name": "Perfect Melody",
          "uri": "spotify:track:1OBlp2GgUQbPMtGNYg4Kdn"
        }
      },
      {
        "track": {
          "id": "7mNPYVxyHtEneLo7tjQJMj",
          "name": "Ugly Heart",
          "uri": "spotify:track:7mNPYVxyHtEneLo7tjQJMj"
        }
      },
      {
        "track": {
          "id": "7kgdVX2Mk8iJ6H3JDiktAM",
          "name": "Drunks",
          "uri": "spotify:track:7kgdVX2Mk8iJ6H3JDiktAM"
        }
      },
      {
        "track": {
          "id": "0ELQGxXgUafqOu80urrauc",
          "name": "Trust Somebody",
          "uri": "spotify:track:0ELQGxXgUafqOu80urrauc"
        }
      },
      {
        "track": {
          "id": "2kz40rIHjfGYxurLiuCBp9",
          "name": "Lost on You",
          "uri": "spotify:track:2kz40rIHjfGYxurLiuCBp9"
        }
      },
      {
        "track": {
          "id": "5TDxhVHsd9AxcWieCsYtcs",
          "name": "Stone",
          "uri": "spotify:track:5TDxhVHsd9AxcWieCsYtcs"
        }
      },
      {
        "track": {
          "id": "0VZ9xPNa6ROafP6GYYuv2S",
          "name": "Marry Me",
          "uri": "spotify:track:0VZ9xPNa6ROafP6GYYuv2S"
        }
      },
      {
        "track": {
          "id": "0NHCEt3hoIZX0o8mhohoZV",
          "name": "The Weight",
          "uri": "spotify:track:0NHCEt3hoIZX0o8mhohoZV"
        }
      },
      {
        "track": {
          "id": "3NdDpSvN911VPGivFlV5d0",
          "name": "I Don’t Wanna Live Forever (Fifty Shades Darker) - From \\"Fifty Shades Darker (Original Motion Picture Soundtrack)\\"",
          "uri": "spotify:track:3NdDpSvN911VPGivFlV5d0"
        }
      },
      {
        "track": {
          "id": "14919dFgTbT2Izd6WvWqqY",
          "name": "Move Along (feat. Norah Jones)",
          "uri": "spotify:track:14919dFgTbT2Izd6WvWqqY"
        }
      },
      {
        "track": {
          "id": "7d0R8oNJtqCqLHod83zhcx",
          "name": "Cottonwood Lullaby",
          "uri": "spotify:track:7d0R8oNJtqCqLHod83zhcx"
        }
      },
      {
        "track": {
          "id": "4ailHqDa2ThPlIsChM6neH",
          "name": "Roads",
          "uri": "spotify:track:4ailHqDa2ThPlIsChM6neH"
        }
      },
      {
        "track": {
          "id": "6i0V12jOa3mr6uu4WYhUBr",
          "name": "Heathens",
          "uri": "spotify:track:6i0V12jOa3mr6uu4WYhUBr"
        }
      },
      {
        "track": {
          "id": "6AQGlm2uDrOVXPVJE4hrNu",
          "name": "Lost In My Mind",
          "uri": "spotify:track:6AQGlm2uDrOVXPVJE4hrNu"
        }
      },
      {
        "track": {
          "id": "41uM9c2YVFDfEsoR2z6Su4",
          "name": "Shine On Rainy Day",
          "uri": "spotify:track:41uM9c2YVFDfEsoR2z6Su4"
        }
      },
      {
        "track": {
          "id": "1eftIypOTzVCDPv9xLZPDN",
          "name": "Only You (with James Corden)",
          "uri": "spotify:track:1eftIypOTzVCDPv9xLZPDN"
        }
      },
      {
        "track": {
          "id": "7fWSIddv6LJG8ZXJFNVQyi",
          "name": "Nothing Really Matters",
          "uri": "spotify:track:7fWSIddv6LJG8ZXJFNVQyi"
        }
      },
      {
        "track": {
          "id": "1fDm1kCj6dwmviArCtCsOA",
          "name": "Distance and Time",
          "uri": "spotify:track:1fDm1kCj6dwmviArCtCsOA"
        }
      },
      {
        "track": {
          "id": "4m8ttWM8IKXyhpv89E867J",
          "name": "Cherry Blossom Girl",
          "uri": "spotify:track:4m8ttWM8IKXyhpv89E867J"
        }
      },
      {
        "track": {
          "id": "5qRNkztzGTx4Wb0P6zff4z",
          "name": "C'est La Vie",
          "uri": "spotify:track:5qRNkztzGTx4Wb0P6zff4z"
        }
      },
      {
        "track": {
          "id": "6iDRG4bz5YdoKhmHfVRpZw",
          "name": "Tragedy",
          "uri": "spotify:track:6iDRG4bz5YdoKhmHfVRpZw"
        }
      },
      {
        "track": {
          "id": "7dEOgJZEDCsLkI3A7ifNzH",
          "name": "Bottle Tops",
          "uri": "spotify:track:7dEOgJZEDCsLkI3A7ifNzH"
        }
      }
    ]
  }
}
"""

playlist_partial = json.loads(_jplaylistpartial)
