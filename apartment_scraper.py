#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Check for new apartments on Wahlins Fastigheter website

Every now and then Wahlins Fastigheter puts up rental apartments

http://wahlinfastigheter.se/lediga-objekt/lagenhet/
"""

# import system packages
import sys
import urllib2
from twilio.rest import TwilioRestClient


def get_download_url():
    return "http://wahlinfastigheter.se/lediga-objekt/lagenhet/"


def get_headers():
    return {'User-Agent': "Magic Browser"}


def get_account_sid():
    return 'secret'


def get_auth_token():
    return 'secret'


def get_twilio_number():
    return 'secret'


def get_my_number():
    return 'secret'


def send_report(content):
    twilio_client = TwilioRestClient(get_account_sid(), get_auth_token())
    body = 'There are new apartments available at %s' % (content)
    twilio_client.messages.create(body=body, from_=get_twilio_number(), to=get_my_number())


def download_url(url, headers):
    content = "%s" % (get_download_url())
    test = False
    req = urllib2.Request(url, headers=headers)
    con = urllib2.urlopen(req)
    for line in con.readlines():
        if line.strip() == "<!-- Start lediga lägenheter -->":
            test = True
        elif line.strip() == "<!-- Slut lediga lägenheter -->":
            break
        elif test:
            if line.strip() == "<h3>Just nu har vi tyvärr inga lediga lägenheter att förmedla här.</h3>":
                return
    send_report(content)


def main(argv):
    download_url(get_download_url(), get_headers())

if __name__ == '__main__':
    main(sys.argv[1:])
    sys.exit(0)
