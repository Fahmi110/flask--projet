from flask import Flask,render_template,request,flash

app=Flask(__name__)




@app.route('/formation')
def formation():
    return render_template('formation.html' )



@app.route('/signup',methods=['GET','POST'])
def signup():

    if request.form =='POST':
         email = request.form ('email')
         firstName = request.form('firstName')
         password1 = request.form('password1')
         password2 = request.form ('password2')  
         if len(email) < 4 :  
              flash("email must be greater tha 4 characters." ) 

         elif len('firtsName') < 2:
               flash("firstname must be greater than 2 characters.") 
        
         elif password1 != password2:
                  flash("pasword don\'t match." ) 
         elif len('password1') < 7:
               flash("password  must be greater tha 7 characters.")
         else:
              flash ('welcome ')  
             
             

             

    {% with messages=  get-flashed-messages ()  %}
    {% if messages%}
  {% for messages in messaeges%}
    {% endfor%}

    {% endif%} 
    {% endwith%} 

#          return render_template('log.html')
             
# # if __name__ =='__main__':
#     app.run(debug= True )