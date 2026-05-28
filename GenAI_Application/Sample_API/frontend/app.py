from flask import Flask, render_template, request
import requests
import markdown

app = Flask(__name__)

FASTAPI_URL = "http://127.0.0.1:8000/ask"

@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""

    if request.method == "POST":

        question = request.form.get("question")

        try:

            response = requests.post(
                FASTAPI_URL,
                json={"question": question}
            )

            data = response.json()

            raw_answer = data.get("response", "")

            answer = markdown.markdown(raw_answer)

        except Exception as e:

            answer = f"<p>Error: {e}</p>"

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)