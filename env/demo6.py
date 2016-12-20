from flask import Flask

app = Flask(__name__)

app.logger.error('An error eccurred')


if __name__ == '__main__':
    app.run()