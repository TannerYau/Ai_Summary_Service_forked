from flask import Flask, jsonify, request
from Ai_service import call_gemini_summary
# creating a Flask app

'''
Create a venv:
python -m venv .venv

After download:
select the venv interpreter
To actitivate in the terminal:
.venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt
'''

# on the terminal type: curl http://127.0.0.1:5000/
app = Flask(__name__)

# Post route for the API ai service
@app.route('/api/ai_summary_service', methods = ['POST'])
def summary_request():
    # handles post request
    try:
        json_data_to_summarize = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON format in request body"}), 400

    if not json_data_to_summarize:
        return jsonify({"error": "Request body is empty"}), 400
    
    # Get params 
    summary_length = json_data_to_summarize.get("summary_length", "short")
    additional_info = json_data_to_summarize.get("additional_info", "no")
    content_to_summarize = json_data_to_summarize.get("content")

    # Call the service function 
    summary_response_data, status_code = call_gemini_summary(
        content_to_summarize, summary_length, additional_info
    )

    # Return the response
    return jsonify(summary_response_data), status_code

if __name__ == '__main__':
    # Run the service on a specific port
    app.run(host='0.0.0.0', port=5001, debug=True)