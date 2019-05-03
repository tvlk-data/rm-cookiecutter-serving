from flask import Flask, jsonify, request


def format_response(message):
    resp = jsonify(message)
    resp.status_code = message.get('status_code')

    return resp


app = Flask(__name__)
MODEL_INFO_PATH = "./info.yaml"


HTTP_OK = 200
HTTP_INTERNAL_SERVER_ERROR = 500
HTTP_BAD_REQUEST = 400


@app.errorhandler(HTTP_BAD_REQUEST)
def invalid_input(msg):
    logging.exception("Bad request: %s" % str(msg))
    return format_response({
        'status_code': HTTP_BAD_REQUEST,
        'message': str(msg),
        'status': 'Request Error'
    })


@app.errorhandler(HTTP_INTERNAL_SERVER_ERROR)
def invalid_process(msg, filename=None):
    exception_msg = "Server error: %s" % str(msg)
    if filename:
        exception_msg += "\nFilename: %s" % filename

    logging.exception(exception_msg)
    return format_response({
        'status_code': HTTP_INTERNAL_SERVER_ERROR,
        'message': str(msg),
        'status': 'Something wrong happened. Please try again'
    })


# check the server status
@app.route('/health')
def health():
    HTTP_STATUS = HTTP_OK
    return format_response({
        "status_code": HTTP_STATUS,
        "message": "HEALTHY"
    })


# get the metadata of the model
@app.route('/info')
def info():
    try:
        with open(MODEL_INFO_PATH, 'r') as infoFile:
            data = infoFile.read().replace('\n','<br>')
        return format_response({
            "status_code": HTTP_STATUS,
            "message": data
        })
    except (OSError, IOError) as e:
        return invalid_process(e)
