from flask import Flask

app = Flask(__name__)

# Import the routes from all controllers
from api.examples import get_example

if __name__ == "__main__":
    app.run()
