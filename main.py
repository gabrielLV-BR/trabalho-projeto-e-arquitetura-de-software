from flask import Flask
from view import student, course, institution, index
from loggers.logger import Logging
from loggers.console_logger import ConsoleLogger
from loggers.file_logger import FileLogger

app = Flask(__name__, static_folder='static')

@app.get('/')
def index():
    return app.send_static_file('index.html')

app.register_blueprint(course.blueprint)
app.register_blueprint(student.blueprint)
app.register_blueprint(institution.blueprint)

Logging.subscribe(ConsoleLogger())
Logging.subscribe(FileLogger('log.txt'))

if __name__ == "__main__":
    app.run(port=8000)

