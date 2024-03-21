from flask import Flask,render_template

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/se connecter')
def seConnecter():
    return render_template('se Connecter.html' )


@app.route('/propos')
def propos():
    return render_template('propos.html'  )


@app.route('/cours')
def cours():
    return render_template('cours.html'  )


@app.route('/formation')
def formation():
    return render_template('formation.html' )



if __name__ =='__main__':
    app.run(debug= True )


