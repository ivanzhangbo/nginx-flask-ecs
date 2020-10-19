from flask import Flask, render_template,request
import boto3

client = boto3.client('s3')

app = Flask(__name__)


@app.route('/')
def index():
    reqs=request.headers
    return render_template('index.html',reqs=reqs)
    
    
@app.route('/s3')
def s3():
    response = client.list_buckets()
    return response

if __name__ == '__main__':
  app.run()
 