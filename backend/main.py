from flask import Flask, render_template, request, redirect, session, jsonify
from funcs.distilgpt import predict
import openai
import json
import os

app = Flask(__name__)

openai.api_key="<your-api-key>"

@app.route("/")
def default():
    return "Hello World"

@app.route("/api/request_answer", methods=['POST'])
def my_api():
    """
    API route to generate response based on dialogue history and user input text and return 
    
    Parameters:
        request (JSON): the input from the user.
    Returns:
        JSON: A JSON object containing the input text and the predicted tags.
    """
    request_data = json.loads(request.json)
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=request_data.get("messages")
        )
    
    data = {
        "response": response.choices[0]["message"]["content"]
    }
    
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)