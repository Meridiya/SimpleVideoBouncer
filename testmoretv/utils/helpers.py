from urllib.parse import urlparse


def parse_url(url):
    try:
        result = urlparse(url)
        if not all([result.scheme, result.netloc]):
            return False
        return result
    except:
        return False


def create_cdn_url(original_url, cdn_base):
    cluster_number = original_url.netloc.split(".", 1)[0]
    return original_url._replace(
        netloc=cdn_base, path=f"/{cluster_number}{original_url.path}"
    ).geturl()
