from flask import Flask # This imports the Flask Class from the flask framework

app = Flask(__name__) # this creates an instance of a Flask app
                      # __name__ is a special variable in python that is set to __main__
                      # when the script is run directly, and to the module name when imported


app.route("/")  # a decorateur which tells Flask which URL should trigger the function below
def home():     # the function which is executed when the URL of the decorateur is visited
    return "Hello, Flask"

if __name__ == "_main__"  # standard python check to ensure that the script is being run directly
    app.run(port=5000, debug=True) # starts the flask development server
                                   # runs the app on port 5000 (default)
                                   # debug mode auto reloads the app on changes
                                   # shows detailed error messages in the bowser if sth goes wrong

