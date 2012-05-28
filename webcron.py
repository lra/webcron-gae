from google.appengine.api import urlfetch
from google.appengine.api import mail


def output_http(message):
    print 'Content-Type: text/plain'
    print ''
    print message


def mail_text(message):
    sender = "update-playlist@webcron-gae.appspotmail.com"
    subject = "Trouble while updating the FG playlist DB"
    mail.send_mail_to_admins(sender, subject, message)


def output_and_email(message):
    mail_text(message)
    output_http(message)


def get_url_and_send_output(url):
    result = urlfetch.fetch(url)
    if result.status_code == 200:
        if result.content:
            output_and_email(result.content)
    else:
        output_and_email('Could not get {} =( Error {}'
                         .format(url, result.status_code))
