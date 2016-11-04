# -*- coding: utf-8 -*-
import string
import random
from optparse import OptionParser
from flask import Flask, render_template, request


app = Flask(__name__)

def generate_random_code(count=5):
    LENGTH_CODE = count
    alnum = string.ascii_uppercase + string.digits
    return ''.join([random.choice(alnum) for i in range(LENGTH_CODE)])


def make_coupon_code(count):
    users = ['ks', 'dc', 'jb', 'jj', 'hw', 'hm', 'rd', 'mk', 'ky', 'yc', 'jc',
             'dm', 'dh', 'sw', 'jy', 'kh', 'jo', 'js', 'ep', 'fl', 'ot']
    entry = []
    for u in users:
        entry.append('d3-%s-%s' % (u, generate_random_code(count)))
    return entry
        

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def create():
    count = request.form.get('count', 5)
    try:
        count = int(count)
        if count < 1:
            return render_template('index.html', error=True)
    except ValueError as e:
        return render_template('index.html', error=True)
    data = make_coupon_code(count)
    return render_template('index.html', error=False, data=data)


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--port', dest='port', default=None, type='int')
    parser.add_option('--debug', dest='debug', default=False, action="store_true")
    (options, args) = parser.parse_args()
    port = options.port
    debug = options.debug

    app.run(host='0.0.0.0', port=port, debug=debug)
