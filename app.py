from flask import Flask, render_template
import os

app = Flask(__name__)

BASE_MUSIC_PATH = "static/source"

@app.route("/")
def index():
    music_data = {}

    for folder in sorted(os.listdir(BASE_MUSIC_PATH)):
        folder_path = os.path.join(BASE_MUSIC_PATH, folder)

        if os.path.isdir(folder_path):
            songs = [
                song for song in os.listdir(folder_path)
                if song.lower().endswith(".mp3")
            ]
            if songs:
                music_data[folder] = songs

    return render_template("index.html", music=music_data)

if __name__ == "__main__":
    app.run(debug=True)
