#!/usr/bin/env python3

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/alexa', methods=['POST', 'GET'])
def alexa():
  data = request.get_json()

  request_type = data['request']['type']
  if request_type == 'LaunchRequest':
    jsonify({
      'version': '0.1',
      'response': {
        'outputSpeech': {
          'type': 'PlainText',
          'text': 'Hello, welcome to my shrug',
        },
      },
    })

  if request_type != 'IntentRequest':
    raise Exception(f'unhandled request type {request_type}')

  query = data['request']['intent']['slots']['query']['value']
  print(f'handling query: `{query}')
  if 'boat' in query:
    response_text = 'I hear you like boats'
  else:
    response_text = 'Say something nautical, not ' + query

  return jsonify({
    'version': '0.1',
    'response': {
      'outputSpeech': {
        'type': 'PlainText',
        'text': response_text,
      },
    },
  })

if __name__ == '__main__':
  app.run(debug=True)
