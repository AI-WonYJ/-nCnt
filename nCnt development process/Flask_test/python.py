from flask import Flask
from datetime import datetime
now = datetime.now()

app = Flask(__name__)

print(now)
@app.route('/')
def hello_world():
  return now

if __name__ == '__main__':
  app.run()