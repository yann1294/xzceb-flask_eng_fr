from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench(english_text):
    # Write your code here
    textToTranslate = translator.english_to_french(english_text)
    return textToTranslate

@app.route("/frenchToEnglish")
def frenchToEnglish(french_text):
    # Write your code here
    textToTranslate = translator.french_to_english(french_text)
    return textToTranslate

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('/templates/index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
