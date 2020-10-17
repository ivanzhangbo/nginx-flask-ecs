from flask import Flask, render_template,request
app = Flask(__name__)


@app.route('/')
def index():
    reqs=request.headers
    return render_template('index.html',reqs=reqs)

if __name__ == '__main__':
  app.run()
 