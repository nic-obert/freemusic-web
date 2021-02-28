from os.path import join
from youtube_dl.utils import DownloadError
from flask import Flask, send_file, render_template, request, Response

from .api_settings import HOMEPAGE, DOWNLOAD_PAGE
from backend.downloader import download_url, DESTINATION


app = Flask(__name__)



@app.route(HOMEPAGE)
def home():
   
   return render_template('index.html')


@app.route(DOWNLOAD_PAGE)
def get():
    
    url = request.args.get('url')
    if url is None:
        return Response('Url not provided', status=400)

    download_type = request.args.get('downloadtype')
    if download_type is None:
        return Response('Download type not provided. Choose between "video" and "audio"', status=400)

    auto_rename = request.args.get('autorename')
    if auto_rename is None:
        auto_rename = False

    try:
        file_name = download_url(url, download_type, auto_rename)
    except DownloadError:
        return Response(f'Invalid url: "{url}"', status=422)
    
    return send_file(join(DESTINATION, file_name), attachment_filename=file_name, as_attachment=True)

    