
import redis
from flask import jsonify, render_template, request, redirect, Flask
import re
import pickle
app = Flask(__name__, static_folder='assets')

conn = redis.Redis(host='localhost', port=6379, db=0)


@app.route('/', methods=['GET'])
def home():
    return redirect('/message')

@app.route('/message', methods=['GET'])
def message():
    return render_template('message.html')

@app.route('/sendMessage', methods=['POST'])
def send():
    message = request.form.get('message')
    title = request.form.get('title')
    channel = "Toko"
    status= sendMessage(channel, title, message)
    # saveData(channel,title,message)
    print(status)
    return status

def saveData(channel,title,message):

    dictSave = {"channel":channel,"kategori":title,"message":message}
    p_data = pickle.dumps(dictSave)

    dataKey = conn.keys("*")
    data = dataKey[len(dataKey)-1].decode('utf-8')
    a = re.findall("\d",data)
    keySave = f'message[{int(a[0])+1}]'
    conn.set(keySave,p_data)   



def sendMessage(channel,title,message):
    data=[]
    data.append(title)
    data.append(message)
    try:
        result = conn.publish(channel,data))
        print(type(result))
        return jsonify({'message': 'Kirim Pesan Berhasil'})
        
    except Exception as e:
        print(e) 
        return jsonify({'message': 'Kirim Pesan Gagal'}),500

if __name__ == '__main__':
    app.env = 'development'
    app.run(
        host='localhost',
        port=8000,
        debug=True)
