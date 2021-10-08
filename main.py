from flask import Flask, jsonify,  render_template, request
import redis
# mengimport function randint
from random import randint


conn = redis.Redis(host='localhost', port=6379, db=0)
app = Flask(__name__, static_folder='assets')

@app.route('/form', methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/form2', methods=['GET'])
def form2():
    return render_template('form2.html')

@app.route('/form3', methods=['GET'])
def form3():
    return render_template('form3.html')

@app.route('/form4', methods=['GET'])
def form4():
    return render_template('form4.html')

kodefix=[]
@app.route('/register', methods=['POST'])
def register_Data():
    # mengenerate 5 bil bulat 0 s/d 10
    kode = randint(1000, 9999)
    kodefix.append(kode)
    data=[]
    nama = request.form.get('nama')
    email= request.form.get('email')
    password= request.form.get('password')
    data.append(nama)
    data.append(email)
    data.append(password)
    data.append(kode)
    print(data)
    conn.publish("register",str(data))
    return jsonify({'message': 'Silahkan aktivasi cek email anda untuk aktivasi!'})

@app.route('/konfirmasi_Kode', methods=['POST'])
def kode():
    kode = request.form.get('kode')
    print(kode)
    print(kodefix[0])
    if kode == str(kodefix[0]):
        result = jsonify({'message': 'Registrasi Berhasil'})
    else:
        result = jsonify({'message': 'Kode Registrasi Salah'})
    return result

if __name__ == '__main__':
    app.env = 'development'
    app.run(
        host='localhost',
        port=8000,
        debug=True)
