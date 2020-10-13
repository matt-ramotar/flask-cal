from app import app

@app.route('/')
def index():
  return '<h1>Sample App</h1>'
