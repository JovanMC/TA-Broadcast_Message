import smtplib
import redis
import ast

# untuk membuat koneksi ke redis
conn = redis.Redis(host='localhost', port=6379, db=0)
p = conn.pubsub()
p.subscribe('register')

while True:
    message = p.get_message()
    if message and not message['data'] == 1:
        data = message['data'].decode('utf-8')
        value = ast.literal_eval(data)  # untuk mengubah string menjadi list menggunakan ast
        gmail_user = 'taftiuksw08@gmail.com'
        gmail_app_password = 'akatsuki077'

        sent_from = gmail_user
        sent_to = [value[1]]
        sent_subject = "Registrasi PubSub Redis"
        sent_body = ("Registrasi PUBSUB Succesfull")
        email_text = """\
        Terima kasih sudah melakukan registrasi di PubSub\n
        Kode Registrasi anda adalah : %s
        """ % (value[3])
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                    """ % (sent_from, ", ".join(sent_to), sent_subject, email_text)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_app_password)
            server.sendmail(sent_from, sent_to, message)
            server.close()
            print('Email sent to %s', value[1])
        except Exception as exception:
            print("Error: %s!\n\n" % exception)