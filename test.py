from flask import Flask     
app = Flask(__name__)   # Flask constructor 
  
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/')       
def hello(): 
    return '<h1>hello world</h1>'
  
if __name__=='__main__': 
   app.run() 
