from flask import Flask 
app = Flask(__name__)
@app.route('/')
def head():
     return "Hello World Fatih"

@app.route('/second')
def second():
   return "This is second Page"

@app.route('/third')
def third():
   return "This is third Page"

@app.route('/fourth/<string:id>')
def fourth():
   return f'Id of this page {id}'

if __name__ == '__main__':

     #app.run(debug=True)
     app.run(host= '0.0.0.0', port=8080)