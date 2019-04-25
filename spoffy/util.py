def get_page_url(page, direction="next") -> str:
    target_keys = ["artists", "playlists", "albums", "tracks"]
    page_url: str = getattr(page, direction, None)
    if page_url:
        return page_url

    for key in target_keys:
        nested = getattr(page, key, None)
        if nested:
            page_url = getattr(nested, direction)
    if page_url:
        return page_url
    raise AttributeError(
        "{} url not found on object of type {}".format(direction, type(page))
    )
