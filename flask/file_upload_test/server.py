import os
from flask import Flask, render_template, request, flash, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "Sphinx of Black Quartz, Judge My Vow!"

UPLOAD_FOLDER = '/Users/Lucky/Desktop/CodingDojo/CodingDojo_TA/Ryan_Python_v21/flask/file_upload_test/static/img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = { 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif' }

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploader', methods=['GET','POST'])
def upload_file():
    # check if the post request has a file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect('/')
    
    file = request.files['file']

    # if the user does not select a file, browser submits an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect('/')

    # if valid file submitted
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return redirect('/')

if __name__=="__main__":
    app.run(debug = True)