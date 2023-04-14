from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

@app.route('/vip-list')
def vip_list():
    conn = psycopg2.connect(
        host='mydb',
        dbname='postgres',
        user='postgres',
        password='secret',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM vip")
    vip_data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('vip_list.html', vip_data=vip_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
