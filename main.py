from flask import Flask, jsonify,  render_template, request
import redis
conn = redis.Redis(host='localhost', port=6379, db=0)
app = Flask(__name__, static_folder='assets')

@app.route('/', methods=['GET'])
def default():
    return render_template('form.html')

@app.route('/message', methods=['GET'])
def message():
    return render_template('message.html')

@app.route('/store', methods=['GET'])
def form():
    return render_template('store.html')

@app.route('/sendMessage', methods=['POST'])
def register_Data():
    data=[]
    message = request.form.get('message')
    title = request.form.get('title')
    data.append(title)
    data.append(message)
    try:
        conn.publish("TokoCabang",str(data))
        return jsonify({'message': 'Kirim Pesan Berhasil'})
    except: 
        return jsonify({'message': 'Kirim Pesan Gagal'})


if __name__ == '__main__':
    app.env = 'development'
    app.run(
        host='localhost',
        port=8000,
        debug=True)
