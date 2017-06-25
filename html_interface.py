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

class HTMLinterface():

    from flask import Flask, request, make_response, redirect
    app = Flask(__name__)

    html_head = '''
        <html>
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

    html_para0 = '''
        <p>watching the <i>market</i> and your <i>position</i> ... </p>
    '''

    html_para = ''
    html_doc = ''
    para_ls = []
    command = ''
    has_new_cmd = False

    def __init__(self):
        self.html_doc = (
                self.html_head + self.html_form +
                self.html_para + self.html_tail )

    @app.route('/')
    def index(self):
        return self.html_doc

    @app.route('/', methods=['POST'])
    def resp_req_pst(self):
        # get cmd
        cmd = request.form.get('cmd', '') # default is ''
        # process
        if cmd != '': # not really necessary
            self.command = cmd
            self.has_new_cmd = True
            print('PST <<', cmd)
        # response
        # retrun make_response(html_doc)
        return redirect('/')

    @app.route('/<cmd>', methods=['GET'])
    def resp_req_get(self, cmd):
        # process this ^
        if cmd != '': # not really necessary
            self.command = cmd
            self.has_new_cmd = True
            print('GET <<', cmd)
        # response
        # return make_response(html_doc)
        return redirect('/')

    def compose_para(self):
        self.html_para = self.html_para0+''.join(self.para_ls)

    def update_html(self):
        self.html_doc = (
                self.html_head + self.html_form +
                self.html_para + self.html_tail )

    def get_new_command(self):
        if self.has_new_cmd:
            return self.command
        else:
            return ''

if __name__ == '__main__':
    gui = HTMLinterface()
    gui.app.run()
