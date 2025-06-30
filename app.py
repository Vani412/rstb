
from flask import Flask, render_template, request
import pdfplumber
from resume_scoring import score_resume

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    feedback = None
    pdf_text = ""
    if request.method == "POST":
        file = request.files["resume"]
        if file:
            with pdfplumber.open(file) as pdf:
                pdf_text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
            feedback = score_resume(pdf_text)
    return render_template("index.html", feedback=feedback, pdf_text=pdf_text)

if __name__ == "__main__":
    app.run(debug=True)
