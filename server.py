from flask_app import app

from flask_app.controller import users

from flask_app.controller import cars

if __name__ == "__main__":
    app.run(debug=True, port=5001)