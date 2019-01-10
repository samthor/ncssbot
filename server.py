#!/usr/bin/env python3

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'Hello, World!'


def alexa_response(text, shouldEndSession=False):
  text = text.replace('<', '&lt;')
  text = text.replace('>', '&gt;')
  return jsonify({
    'version': '0.1',
    'response': {
      'outputSpeech': {
        'type': 'SSML',
        'ssml': f"""<speak><voice name="Joey">{text}</voice></speak>"""
      },
      'shouldEndSession': shouldEndSession
    }
  })


@app.route('/alexa_necsus', methods=['POST', 'GET'])
def alexa_necsus():
  data = request.get_json()

  request_type = data['request']['type']
  try:
    query = data['request']['intent']['slots']['query']['value']
  except:
    query = ''

  words = query.split()
  noun = None
  for word in words:
    noun = word
    if word[0].isupper():
      break

  output = 'Welcome to NeCSuS, who would you like to kill?'
  should_end_session = False

  if noun:
    noun = noun.lower()
    if noun == 'stop':
      should_end_session = True
      output = 'Good night, children'
    elif noun == 'nicky' or noun == 'nikki':
      output = 'Nicky is literally unkillable'
    elif noun == 'tim':
      output = 'Tim stares deep into your soul and asks how your project is going'
    else:
      output = 'Psych, you\'re dead!'

  return alexa_response(output, should_end_session)


@app.route('/alexa', methods=['POST', 'GET'])
def alexa():
  data = request.get_json()

  request_type = data['request']['type']
  session_id = data['session']['sessionId']
  print(f'got request_type={request_type}, sessionId={session_id}')

  if request_type == 'LaunchRequest':
    return alexa_response('Hello, welcome to my shrug')

  if request_type != 'IntentRequest':
    raise Exception(f'unhandled request type {request_type}')

  query = data['request']['intent']['slots']['query']['value']
  print(f'handling query: `{query}')
  if 'boat' in query:
    response_text = 'I hear you like boats'
  else:
    response_text = 'Say something nautical, not ' + query

  return alexa_response(response_text)

if __name__ == '__main__':
  app.run(debug=True)
