from flask import Flask, jsonify, redirect, render_template

import config
from common.satconnectserver import PostgreDatabase

app = Flask(__name__, static_folder='assets')
db = PostgreDatabase(
    host=config.DB_HOST,
    port=config.DB_PORT,
    database=config.DB_NAME,
    username=config.DB_USER,
    password=config.DB_PASS,
    logName=config.LOG_NAME)


@app.route('/', methods=['GET'])
def index():
    return redirect('/form')


@app.route('/form', methods=['GET'])
def form():
    return render_template('form.html')


@app.route('/datatable', methods=['GET'])
def datatable():
    return render_template('datatable.html')


@app.route('/api/mahasiswa', methods=['POST'])
def apiMahasiswa():
    status, data = db.select(
        'SELECT * FROM mahasiswa_baru WHERE nim LIKE %(nim)s',
        nim='672000%'
    )
    if status:
        return jsonify({'data': data}), 200
    else:
        return jsonify({'data': data}), 500


if __name__ == '__main__':
    app.env = 'development'
    app.run(
        host='localhost',
        port=8000,
        debug=True)
