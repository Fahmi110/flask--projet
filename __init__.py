
from flask import Flask 

app=Flask(__name__)



def create_app():
    app = ...
    # existing code omitted

    from . import db
    db.init_app(app)

    return app





if __name__ =='__main__':
    app.run(debug= True )