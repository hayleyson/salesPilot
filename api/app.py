from flask import Flask, jsonify, request
# from flask import Flask, render_template, request, redirect, session
from distilgpt import predict

app = Flask(__name__)
dialogue_history = []

@app.route("/api/request_answer", methods=['POST'])
def my_api():
    """
    API route to generate response based on dialogue history and user input text and return 
    
    Parameters:
        request (JSON): the input from the user.
    Returns:
        JSON: A JSON object containing the input text and the predicted tags.
    """
    global dialogue_history
    input_text = request.form.get('input_text')
    response, dialogue_history = predict(input_text, dialogue_history)
    
    data = {
        "response_text": response
    }
    
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)