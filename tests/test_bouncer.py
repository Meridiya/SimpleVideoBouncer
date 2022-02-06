from testmoretv.app.app import app

amount_of_requests = 11


def test_video_bouncer(client):
    base_url = "/?video=http://s1.video.url/video.m3u8"
    for i in range(amount_of_requests):
        _, resp = client.get(base_url, gather_request=False)
        if i % 10 == 0:
            assert resp.status == 301
            assert resp.next_request.url == "http://s1.video.url/video.m3u8"
        else:
            assert resp.status == 301
            assert (
                resp.next_request.url
                == f"http://{app.config.CDN_URL}/s1/video.m3u8"
            )
