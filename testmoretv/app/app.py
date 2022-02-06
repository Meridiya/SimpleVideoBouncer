import os

from sanic import Request, Sanic, response

from testmoretv.utils import helpers

CDN_URL = os.getenv("CDN_HOST")

app = Sanic(name="TestMoreTV")
app.ctx.counter = 0


@app.route("/")
async def video_bouncer(request, methods=["GET"]):
    video_url = request.args.get("video")

    if not video_url:
        return response.text('Must provide "video" query param', status=400)

    parsed_url = helpers.parse_url(video_url)

    if not parsed_url:
        return response.text('Bad param "video"', status=422)

    counter = app.ctx.counter
    app.ctx.counter += 1

    if counter % 10 == 0:
        return response.redirect(video_url, status=301)
    else:
        new_url = helpers.create_cdn_url(parsed_url, app.config.CDN_URL)
        return response.redirect(new_url, status=301)


def main():
    if not CDN_URL:
        raise ValueError('"CDN_HOST" env must be provided')
    app.config.CDN_URL = CDN_URL
    app.run(host="0.0.0.0", port=8000, fast=True)
