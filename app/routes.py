from flask import redirect, render_template, url_for, jsonify, request
from app.app_job import general_operations, read_operations

FILE_SVC_PREFIX = "/file"

def routes(app):
    @app.route(FILE_SVC_PREFIX+"/get_directory", methods=["GET"])
    def _svc_get_directory():
        request_path = request.args.get("path")
        if not request_path:
            request_path = "/home/can"
        status, resultMessage, response_data = read_operations.get_directory_contents(request_path)
        return general_operations.create_json_response(status, resultMessage, response_data)  

