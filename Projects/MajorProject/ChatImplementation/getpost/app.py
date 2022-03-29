from flask import Flask, render_template, request
import yake
import wikipedia
import spacy
from flask import send_file

app = Flask(__name__)
app.static_folder = 'static'

def getanswer(message):
    text=message
    language="en"
    max_ngram_size=3
    deduplication_threshold=0.9
    numOfKeywords=20
    custom_kw_extractor=yake.KeywordExtractor(lan=language,n=max_ngram_size,dedupLim=deduplication_threshold,top=numOfKeywords,features=None)
    keywords=custom_kw_extractor.extract_keywords(text)
    print("Extracted keywords are: ")
    print(keywords)
    try:
        for i in range(len(keywords)):
            text=wikipedia.summary(keywords[i][0])
            return (text)
            # doc=nlp(text)
            # print("Suggested Keywords: ")
            # print(doc.ents)
            # flag=input("Satisfied with current answer? Y/N: ")
            # if flag=="y" or flag=="Y":
            #     break
    except wikipedia.exceptions.DisambiguationError as opt:
        return (opt)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    # return chatbot_response(userText)
    return str(getanswer(userText))


if __name__ == "__main__":
    app.run()