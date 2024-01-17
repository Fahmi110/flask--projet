from flask import Flask

app=Flask(__name__)

from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/levels')
def levels():
    return render_template('levels.html' )


@app.route('/propos')
def propos():
    return render_template('propos.html'  )


@app.route('/se connecter')
def   seConnecter():
    return render_template('se connecter.html'  )
    

@app.route('/user')
def user():
    return render_template('user.html'  )

# @app.route('/user')
# def layout():
#     return render_template('user.html'  )

if __name__ =='__main__':
    app.run(debug= True )


