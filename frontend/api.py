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

    try:
        file_name = download_url(url)
    except DownloadError:
        return Response(f'Invalid url: "{url}"', status=422)
    
    return send_file(join(DESTINATION, file_name), attachment_filename=file_name, as_attachment=True)

    