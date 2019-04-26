import json
import requests
from flask import Flask, Response
import os
import logger
import cherrypy
from flask import render_template
from SubmitJwt import SubmitJwt

app = Flask(__name__)
logger = logger.Logger('entities-viewer-service')
sesam_api = os.environ.get('SESAM_API_URL', 'http://sesam-node:9042/api')


@app.route("/<path:path>", methods=["GET", "POST"])
def get(path):
    form = SubmitJwt()

    if form.validate_on_submit():
        request_url = sesam_api + "/publishers/" + path + "/entities"
        logger.info("Requesting entities from url: " + request_url)
        request = requests.get(url=request_url,
                               headers={'Accept': 'application/zip', 'Authorization': 'bearer ' + form.jwt.data})

        json_response = json.dumps(request.json())
        response = Response(json_response, content_type='application/json; charset=utf-8')
        response.headers.add('content-length', len(json_response))
        response.status_code = request.status_code

        logger.info("Request status: " + str(request.status_code))
        if request.status_code != 200:
            logger.info(json_response)

        return response
    else:
        return render_template('SubmitJwt.html', title='JWT', form=form)


if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'lasciate ogni sperantza voi chi entrate qui'
    cherrypy.tree.graft(app, '/')

    # Set the configuration of the web server to production mode
    cherrypy.config.update({
        'environment': 'production',
        'engine.autoreload_on': False,
        'log.screen': True,
        'server.socket_port': 5001,
        'server.socket_host': '0.0.0.0'
    })

    # Start the CherryPy WSGI web server
    cherrypy.engine.start()
    cherrypy.engine.block()
