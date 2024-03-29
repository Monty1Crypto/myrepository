# Import Flask modules
from flask import Flask, render_template #render tremplate is used to render HTML templates

# Create an object named app 
app = Flask(__name__)

# Create a function named head which shows the massage as "This is my first conditions experience" in `index.html` 
# and assign to the route of ('/')
@app.route('/')
def haed():
    return render_template('index.html', message='This is my first conditions experience')  

# Create a function named header which prints the elements of a list of your choice one by one in `body.html` 
# and assign to the route of ('/mylist')
@app.route('/mylist')
def header():
    myfriends=['Monty', 'Mehdi', 'Zack']
    return render_template('body.html', object=myfriends) 

# run this app in debug mode on your local.
if __name__ == "__main__": 
    app.run(debug=True)
