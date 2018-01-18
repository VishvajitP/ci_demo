'''
This Module for contains the route for uploading a file and resturning the same
file data back in the response once stored.
'''
import os
from flask import (Flask,
				   render_template,
				   request)
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'img')


@app.route('/', methods=['POST'])
def upload():
	'''
	This route saves the file uploaded in the form and returns the same file
	in the response
	'''
	file = request.files['file']
	filename = secure_filename(file.filename)
	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	return render_template('show-image.html', filename=filename)

@app.route("/", methods=['GET'])
def home():
	'''
	This route renders the HTML page to show basic form for file upload
	'''
	return render_template('home.html')

if __name__ == '__main__':
	app.run(port=80, host='0.0.0.0')

