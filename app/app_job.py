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
    
    def get_content_metadata(content):
        

class read_operations():
    @staticmethod
    def get_directory_contents(request_path):
        path = Path(request_path)
        contents = [] 
        for content in path.iterdir():
            filename = content.name
            meta = os.stat(content)
            print(meta)
            size, mtime = meta.st_size, meta.st_mtime
            if content.is_file():
                contents.append({"name" : filename,"type" : "file", "size": size, "mtime" : mtime})
            elif content.is_dir():
                contents.append({"name" : filename,"type" : "dir","size": size, "mtime" : mtime})
            else:
                pass
        return True, "Success.", contents
