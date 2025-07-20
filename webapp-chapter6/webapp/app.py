import os
import swimclub

from flask import Flask
app = Flask(__name__)

# @app.get("/")
# def index():
#     return "This is a placeholder for your webapp's opening page."

@app.get("/swimmers")
def index():
    swimmerrs = {}
    swimfiles = os.listdir(swimclub.FOLDER)
    swimfiles.remove('.DS_Store')
    for swmFile in swimfiles:
        name, *_ = swimclub.read_swim_data(swmFile)
        if name  not in swimmerrs:
            swimmerrs[name] = []
            swimmerrs[name].append(swmFile)
    return str(sorted(swimmerrs))
if __name__ == "__main__":
    app.run()