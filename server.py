#!/usr/bin/env python3

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/alexa', methods=['POST', 'GET'])
def alexa():
  return jsonify({
    'version': '0.1',
    'response': {
      'outputSpeech': {
        'type': 'PlainText',
        'text': 'Hello, welcome to my shrug',
      },
    },
  })

if __name__ == '__main__':
  app.run(debug=True)
