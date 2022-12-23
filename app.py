from flask import *
from werkzeug.utils import secure_filename
import json
import os


app = Flask(__name__)

UPLOAD_FOLDER = './db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def write_json(new_data, filename):
    with open(filename,'r+') as file:
        data = json.load(file)
        data["files"].append(new_data)
        file.seek(0)
        json.dump(data, file, indent = 4)


@app.route('/', methods=['Get', 'Post'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        file_metadata = {
            "file_name": filename
        }
        write_json(file_metadata, "./db/dbfiles.json")

        
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True)

