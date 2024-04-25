from flask import Flask
app=Flask(__name__)
@app.route("/")

def index():
    return "this is chat gpt clone"

if __name__=="__main__":
    app.run(debug=True)