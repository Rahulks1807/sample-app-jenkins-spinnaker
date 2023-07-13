from flask import Flask
app = Flask('hello-world')
@app.route("/")
def hello_world():
    return "<p>This is a Hello World application</p>"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8080 , debug=True)
    # End of hello app 
    