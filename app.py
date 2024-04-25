from flask import Flask,render_template, request, flash ,url_for

app=Flask(__name__)
app.config ['SECRET-KEY'] = 'mykey'

@app.route('/')
def home():
    return render_template('index.html' )


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
def formatiion():
    return render_template('formation.html' )


@app.route('/signup',methods=['GET','POST'])
def signup(): 
        if request.form =='POST':
                email = request.form('email')
                firstName = request.form ('firstName')
                password1 = request.form('password1')
                password2 = request.form ('password2')  
                if len(email) < 4 :  
                    flash("email must be greater tha 4 characters." ) 

                elif len(firstName) < 2:
                    flash("firstname must be greater than 2 characters.") 
                
                elif password1 != password2:
                        flash("pasword don\'t match." ) 
                elif len(password1) < 7:
                    flash("password  must be greater tha 7 characters.")
                else:
                    flash ('welcome ')  
        return render_template("signup.html")
       
    

if __name__ =='__main__':
    app.run(debug= True )

