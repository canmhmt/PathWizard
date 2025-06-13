from flask import redirect, render_template, url_for, jsonify, request
import os

FILE_SVC_PREFIX = "/file"

def routes(app):
    @app.route(FILE_SVC_PREFIX+"/control_panel")
    def wel():
        return render_template("control_panel/control_panel.html")

    @app.route('/api/list_dir')
    def list_dir():
        path = request.args.get('path')
        if not path or not os.path.exists(path):
            return jsonify({'error': 'Invalid path'}), 400
        try:
            dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
            files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
            return jsonify({'directories': dirs, 'files': files})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
