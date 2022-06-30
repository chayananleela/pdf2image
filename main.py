from itertools import count
from flask import Flask, render_template, request, send_file
from pdf2image import convert_from_path

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def main():
        
    if  request.method == 'POST':
        f = request.files['file']
        images = convert_from_path(f.filename)
        for i in range(len(images)):
            images[i].save('page'+ str(i) + '.jpg', 'JPEG')
        return send_file(f, 
        mimetype="image/jpeg",
        as_attachment=True,
        download_name=f"{f}.jpg"
        )
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
