import models

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    data = {
        'message': 'Hello, World!',
        'developer': models.User.getUserWithUsername('develop').to_json()
    }

    return jsonify(**data)

# run the app.
if __name__ == "__main__":
    # reset the entire database before launching the web application
    models.drop_db()
    models.init_db()

    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run(port=3000)
