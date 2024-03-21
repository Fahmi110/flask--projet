from flask import Flask,render_template

app=Flask(__name__)




@app.route('/formation')
def formation():
    return render_template('formation.html' )


if __name__ =='__main__':
    app.run(debug= True )