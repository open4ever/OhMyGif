from flask import Flask, request, redirect, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from script.converter import Converter
import os


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"


@app.route("/")
def index():
    return redirect("/static/index.html")


@app.route("/sendfile", methods=["POST"])
def send_file():
    file_object = request.files["file2upload"]
    filename = secure_filename(file_object.filename)
    save_path = "{}/{}".format(app.config["UPLOAD_FOLDER"], filename)
    file_object.save(save_path)

    with open(save_path, "r") as f:
        pass
    c = Converter("seila", "30", save_path)
    c.video_to_png()
    c.png_to_gif()

    return redirect("/uploads/seila.gif")


@app.route("/uploads/<path:filename>")
def download_file(filename):
    return send_from_directory(
        app.config["UPLOAD_FOLDER"], "seila.gif", as_attachment=True
    )


@app.route("/filenames", methods=["GET"])
def get_filenames():
    filenames = os.listdir("uploads/")

    def modify_time_sort(file_name):
        file_path = "uploads/{}".format(file_name)
        file_stats = os.stat(file_path)
        last_access_time = file_stats.st_atime
        return last_access_time

    filenames = sorted(filenames, key=modify_time_sort)
    return_dict = dict(filenames=filenames)
    return jsonify(return_dict)


if __name__ == "__main__":
    app.run(debug=False)
