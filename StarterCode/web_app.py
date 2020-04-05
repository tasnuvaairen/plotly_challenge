import os
import sys
import numpy as np
import pandas as pd

import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template, request

#from scrape_mars import scrape
#from scrape_mars import show_scarpped_html

app = Flask (__name__, template_folder='', static_url_path='/static')

@app.route("/root")
def welcome ():
    return (
        f"Root.<br/>\n"
)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")
    #return app.send_static_file('index.html')

if __name__ == '__main__':
	#scrape()
	app.run()    