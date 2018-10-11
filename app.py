from flask import Flask
from docker_helper import DockerHelper
from datetime import datetime
import os
import shutil

dc = DockerHelper()

app = Flask(__name__)

@app.route("/postgres")
def postgres():
    # create a docker postgres container
    return "docker postgres container"

@app.route("/postgres/build_and_run")
def build_and_run():
    return dc.build_and_run()