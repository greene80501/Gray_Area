from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Route for the main index page
@app.route('/')
def index():
    return render_template('index.html')

# Route to serve the resume PDF file
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('static', filename, as_attachment=True)
@app.route('/Wyatts/file1.html')
def wyatts_portfolio():
    return render_template('Wyatts/file1.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)