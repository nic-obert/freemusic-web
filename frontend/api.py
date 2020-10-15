from os.path import join

from flask import Flask, send_file, render_template, request

from .api_settings import HOMEPAGE, DOWNLOAD_PAGE
from backend.downloader import download_url, DESTINATION


app = Flask(__name__)



@app.route(HOMEPAGE)
def home():
   
   return render_template('index.html')


@app.route(DOWNLOAD_PAGE)
def get(url: str):
    
    file_name = download_url(url)
    
    return send_file(join(DESTINATION, file_name), attachment_filename=file_name)

    