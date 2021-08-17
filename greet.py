from flask import Flask
greet=Flask(__name__)

@greet.route('/')
def greet_world():
    return 'Hi World!'