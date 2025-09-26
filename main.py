from flask import Flask, render_template, request
import uuid
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()
    if request.method == "POST":
        rec_id = request.form.get("uuid")
        desc = request.form.get("text")
        input_files = []

        # Ensure directory exists
        target_dir = os.path.join(app.config['UPLOAD_FOLDER'], rec_id)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir, exist_ok=True)

        # Accept multiple files from `files` field
        files = request.files.getlist('files')
        # Fallback: also loop through any other file fields (backward compatibility)
        if not files:
            files = [f for _, f in request.files.items()]

        seen_names = set()
        for file in files:
            if file and file.filename:
                ext = file.filename.rsplit('.', 1)[-1].lower()
                if ext in ALLOWED_EXTENSIONS:
                    filename = secure_filename(file.filename)
                    if filename in seen_names:
                        continue
                    seen_names.add(filename)
                    file.save(os.path.join(target_dir, filename))
                    input_files.append(filename)

        # Save description
        if desc is not None:
            with open(os.path.join(target_dir, "desc.txt"), "w", encoding="utf-8") as f:
                f.write(desc)

        # Write input.txt for concatenation
        if input_files:
            with open(os.path.join(target_dir, "input.txt"), "w", encoding="utf-8") as f:
                for fl in input_files:
                    f.write(f"file '{fl}'\n")
                    f.write("duration 1\n")


    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html", reels=reels)

app.run(debug=True)