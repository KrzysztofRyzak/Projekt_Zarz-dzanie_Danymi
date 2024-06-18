from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('car_dealership.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    search = request.args.get('search')
    sort_by = request.args.get('sort_by')
    
    conn = get_db_connection()
    query = 'SELECT * FROM cars'
    if search:
        query += ' WHERE name LIKE ?'
        cars = conn.execute(query, ('%' + search + '%',)).fetchall()
    else:
        cars = conn.execute(query).fetchall()
    
    if sort_by:
        if sort_by == 'name':
            cars.sort(key=lambda car: car['name'])
        elif sort_by == 'brand':
            cars.sort(key=lambda car: car['brand'])
        elif sort_by == 'year':
            cars.sort(key=lambda car: car['year'])
        elif sort_by == 'type':
            cars.sort(key=lambda car: car['type'])

    conn.close()
    return render_template('index.html', cars=cars, search=search, sort_by=sort_by)

@app.route('/add', methods=('GET', 'POST'))
def add_car():
    if request.method == 'POST':
        name = request.form['name']
        brand = request.form['brand']
        year = request.form['year']
        type = request.form['type']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO cars (name, brand, year, type) VALUES (?, ?, ?, ?)',
                     (name, brand, year, type))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('add_car.html')

@app.route('/delete/<int:id>')
def delete_car(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM cars WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/view/<int:id>')
def view_car(id):
    conn = get_db_connection()
    car = conn.execute('SELECT * FROM cars WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('view_car.html', car=car)

if __name__ == '__main__':
    app.run(debug=True)
