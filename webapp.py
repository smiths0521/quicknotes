from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
notes = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        note = request.form.get('note')
        if note:
            notes.append(note)
    return render_template('index.html', notes=notes)

@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    if 0 <= index < len(notes):
        del notes[index]
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
