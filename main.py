import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from utils.image_utils import ImageUtils
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

upload_folder = os.getenv('UPLOAD_FOLDER', os.path.join('static', 'uploads'))
app.config['UPLOAD_FOLDER'] = upload_folder

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

max_content_length = os.getenv('MAX_CONTENT_LENGTH', 16 * 1024 * 1024)
app.config['MAX_CONTENT_LENGTH'] = int(max_content_length)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}

image_utils = ImageUtils()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Dosya seçilmedi')
            return redirect(url_for('home'))
        
        file = request.files['file']
        
        if file.filename == '':
            flash('Dosya seçilmedi')
            return redirect(url_for('home'))
        
        if not allowed_file(file.filename):
            flash('Desteklenmeyen dosya formatı. Lütfen JPG, PNG, GIF, BMP veya WEBP formatında bir dosya yükleyin.')
            return redirect(url_for('home'))
        
        try:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            color_stats = image_utils.analyze(file_path)
            file_url = url_for('static', filename=f"uploads/{filename}")
            
            flash('Dosya başarıyla yüklendi')
            return render_template('home.html', filename=file_url, color_stats=color_stats)
        
        except Exception as e:
            flash(f'Bir hata oluştu: {str(e)}')
            return redirect(url_for('home'))
    
    return render_template('home.html')




if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug_mode, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))