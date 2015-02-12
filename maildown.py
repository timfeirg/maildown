# -*- coding: utf-8 -*-


import os
import pypandoc
import smtplib
from pynliner import Pynliner
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


class MailMan(object):

    def __init__(self, settings=None):
        """
        settings -- dict or str containing filepath
        """
        self.user = settings['user']
        self.pw = settings['password']
        self.server = settings['server']

    def send_mail(self, nickname='', to=[], title='Untitled', content='',
                  mode='markdown', css=None, debug=False):
        """
        send mail to one or more recipients, all should be ascii or unicode
        * nickname -- name displayed at mail, e.g. 'batman <bruce@gmail.com>',
        default to your email address
        * to -- recipients email address, str or list of str
        * title -- email title, default to 'Untitled'
        * content -- default empty str
        * mode -- if markdown, parse content as markdown, otherwise plain text
        * css -- css file path or plain css string, if css is a file path, check
        if the file exists, otherwise the program thinks it's a css string
        * debug -- if True, print the corresponding html and exit, you can std
        output to file and inspect it with chrome
        """
        if not isinstance(to, list):
            to = [to]

        tos = ','.join(to)

        msg = MIMEMultipart()
        msg['From'] = nickname or self.user
        msg['To'] = tos
        msg['Subject'] = title

        if mode == 'markdown':
            message = pypandoc.convert(content, 'html', format='md')
            mime_mode = 'html'
        else:
            message = content
            mime_mode = 'plain'

        # consolidate html with css
        if css:
            if os.path.isfile(css):
                with open(css, 'rb') as f:
                    css = f.read()

            p = Pynliner()
            p.from_string(message).with_cssString(css)
            message = p.run().encode('utf-8')

        if debug:
            print(message)
            return

        msg.attach(MIMEText(message, mime_mode))

        session = smtplib.SMTP(host=self.server)
        session.ehlo()
        session.starttls()
        session.ehlo()
        session.login(self.user, self.pw)
        res = session.sendmail(self.user, to, msg.as_string())
        print(res)
