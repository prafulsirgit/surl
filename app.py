from flask import Flask, request, redirect, render_template, url_for, flash
import sqlite3
import string, random
from datetime import datetime, timedelta
import os

app = Flask(__name__)
app.secret_key = 'secret_key'  # this is temprory can be use .env to replace this

DB_NAME = 'short.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY,
                original_url TEXT NOT NULL,
                short_code TEXT UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
init_db()

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def delete_expired():
    expiration_time = datetime.now() - timedelta(days=3)
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('DELETE FROM urls WHERE created_at <= ?', (expiration_time,))
        conn.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']
        custom_alias = request.form.get('custom_alias')

        delete_expired() 

        if not original_url:
            flash("URL is required!", "error")
            return redirect(url_for('index'))

        short_code = custom_alias if custom_alias else generate_code()

        with sqlite3.connect(DB_NAME) as conn:
            cur = conn.cursor()

            # Check for alias conflict
            cur.execute('SELECT * FROM urls WHERE short_code = ?', (short_code,))
            if cur.fetchone():
                flash("Custom alias already in use.", "error")
                return redirect(url_for('index'))

            cur.execute('INSERT INTO urls (original_url, short_code) VALUES (?, ?)', (original_url, short_code))
            conn.commit()

        short_url = request.host_url + short_code
        return render_template('index.html', short_url=short_url)

    return render_template('index.html')

@app.route('/<short_code>')
def redirect_to_original(short_code):
    delete_expired()

    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute('SELECT original_url FROM urls WHERE short_code = ?', (short_code,))
        result = cur.fetchone()
        if result:
            return redirect(result[0])
        else:
            return "Link not found or expired.", 404

if __name__ == '__main__':
    app.run(debug=True)