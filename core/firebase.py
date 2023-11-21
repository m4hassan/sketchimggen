import pyrebase
import os

FIREBASE_CONFIG = {
    "apiKey": "AIzaSyCQwpqUF4Rr68gg9fvc7RucD7ZC9utJw_Y",
    "authDomain": "djangoimggen.firebaseapp.com",
    "projectId": "djangoimggen",
    "storageBucket": "djangoimggen.appspot.com",
    "messagingSenderId": "48530110881",
    "appId": "1:48530110881:web:fa655bf59100f6ead4f3e0",
    "measurementId": "G-5P9RPKFG4K",
    "databaseURL": ""
  }

def fb_storage(config, file):
  fire_base = pyrebase.initialize_app(config)
  storage = fire_base.storage()
  storage.child('file/'+ file.name).put(file)
  download_url = storage.child('file/'+file.name).get_url(None)
  print("url: ",download_url)
  return download_url
