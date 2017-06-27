#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

#  ==============================================
#  ·
#  · Author: Mogei Wang
#  ·
#  · mogeiwang@gmail.com
#  ·
#  · COPYRIGHT 2017
#  ·
#  ==============================================

from flask import Flask, request, make_response, redirect
app = Flask(__name__)

html_head = '''
    <html>
    <link rel="icon" href="data:,">

    <head>
    <meta charset="utf-8">
    <title>real-deep-mining</title>
    </head>

    <body>

    <h2> real-deep-mining </h2>
'''

html_tail = '''
    </body>
    </html>
'''

html_form = '''
    <form class="form-horizontal" method="post">
        <div class="col-sm-13">
            <input type="text" class="form-control" id="cmd"
            size="150" maxlength="250"
            name="cmd" placeholder="cmd" autofocus="true">
        </div>
    </form>
'''

html_par0 = '''
    <p>watching the <i>market</i> and your <i>position</i> ... </p>
'''

html_para = ''
html_doc = ''
para_ls = []
command = ''
has_new_cmd = False


@app.route('/')
def index():
    return update_html()

@app.route('/', methods=['POST'])
def resp_req_pst():
    # get cmd
    cmd = request.form.get('cmd', '') # default is ''
    # process
    if cmd != '': # not really necessary
        command = cmd
        has_new_cmd = True
        print('PST <<', cmd)
    # response
    return make_response(update_html())

@app.route('/<cmd>', methods=['GET'])
def resp_req_get(cmd):
    # process this ^
    if cmd != '': # not really necessary
        command = cmd
        has_new_cmd = True
        print('GET <<', cmd)
    # response
    return redirect('/')

def compose_para():
    html_para = html_par0 + ''.join(para_ls)

def update_html():
    compose_para()
    html_doc = ( html_head + html_form + html_para + html_tail )
    return html_doc

def get_new_command():
    if has_new_cmd:
        return command
    else:
        return ''


if __name__ == '__main__':
    app.run(port=5800)
