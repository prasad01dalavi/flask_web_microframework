from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)

# 2nd argument says that type of media to be uploaded
photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/images'
# specify the directory to store the images
configure_uploads(app, photos)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        print 'File saved successfully!'
        # when uploaded file is saved it return the file name
        return filename
    # render the upload template when GET requested to the upload url
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)

# Note: Visit https://pythonhosted.org/Flask-Uploads/ for further details
