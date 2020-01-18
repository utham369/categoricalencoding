# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:47:27 2019

@author: Admin
"""

import requests
import json


data = {
        "text": "This is my third message!keep going"
        }

#webhook = os.environ.get("slack_webhook")
#webhook = "https://hooks.slack.com/services/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"
#requests.post(webhook , json.dumps(data))


#import sandesh
#loss = 0.15
#msg = f"Training loss was {loss} adsasd"
#sandesh.send(msg , webhook = webhook)
#
#
#import collections
#import sandesh
#
#log = collections.OrderedDict([
#        ('training_epoch', 5),
#        ('loss', 0.08)
#    ])
#sandesh.send(log, webhook = webhook)


#msg = ['traning loss : 0.3' , 'test_loss : 0.2']
def sendNotification(key ,msg):
      msg = [ key + " : " +msg]
      webhook = "https://hooks.slack.com/services/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"
      data["text"] = '\n'.join(msg)
      requests.post(webhook, json.dumps(data))

#sendNotification(msg)