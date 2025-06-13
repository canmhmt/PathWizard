import os
import shutil
from pathlib import Path
from flask import jsonify

class general_operations():
    @staticmethod
    def create_json_response(status, resultMessage, resultSet):
        return jsonify(
                {
                    "status" : status,
                    "resultMessage" : resultMessage,
                    "resultSet" : resultSet
                })

class read_operations():
    @staticmethod
    def get_directory_contents(request_path):
        path = Path(request_path)
        filename = path.name
        contents = [] 
        for content in path.iterdir():
            if content.is_file():
                contents.append({"name" : filename,"type" : "file"})
            elif content.is_dir():
                contents.append({"name" : filename,"type" : "dir"})
            else:
                pass
        return True, "Success.", contents



