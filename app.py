from flask import Flask

app=Flask(__name__)

from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')







@app.route('/contact')
def contact():
    return render_template('contact.html' )


@app.route('/propos')
def propos():
    return render_template('propos.html'  )




if __name__ =='__main__':
    app.run(debug= True )


