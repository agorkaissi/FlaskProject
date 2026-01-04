from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
@app.route("/")
def home():
    db = sqlite3.connect('movies.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM movies')
    all_movies = cursor.fetchall()
    return render_template('home.html',movies = all_movies)
@app.route("/",methods=['POST'])
def remove_movie():
    if request.method == 'POST':
        movies_to_remove_ids = request.form.getlist('movieToRemove')
        db = sqlite3.connect('movies.db')
        cursor = db.cursor()
        for movie_id in movies_to_remove_ids:
            cursor.execute('DELETE FROM movies WHERE id = ?', (movie_id,))
        db.commit()
        db.close()
    return redirect(url_for('home'))

@app.route("/addMovie", methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        movieTitle = request.form.get('title')
        movieYear = request.form.get('year')
        movieActors = request.form.get('actors')
        db = sqlite3.connect('movies.db')
        cursor = db.cursor()
        cursor.execute('INSERT INTO movies (title, year, actors) VALUES (?,?,?)', (movieTitle,movieYear,movieActors))
        db.commit()
        db.close()
        return redirect(url_for('home'))
    return render_template('add.html')

if __name__ == "__main__":
    app.run()
