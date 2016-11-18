from flask import render_template
from flask import Flask
app = Flask(__name__)


__version__     = "1.0.0"
__maintainer__  = "Andrew Amesbury"
__email__       = "andrew [at] amesbury.it"
__copyright__   = "Andrew Amesbury 2016"
__license__     = "MIT License"


@app.route('/', methods=['GET'])
@app.route('/<thing>', methods=['GET'])
@app.route('/<thing>/', methods=['GET'])
def yeah_nah(thing=None):
    return render_template('yeahnah.html', thing=thing)


@app.errorhandler(404)
def page_not_found(e):
    return yeah_nah("Wat? %s" % e)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("80")
    )
