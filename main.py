from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Convert the list to a dictionary for faster lookups
STUDENT_DATA = {student["name"]: student["marks"] for student in [
    {"name": "mGtnrgW", "marks": 37},
    {"name": "pTRJKlmua", "marks": 90},
    {"name": "u", "marks": 44},
    {"name": "n3yP83W", "marks": 95},
    {"name": "iCLK1UBz3E", "marks": 58},
    {"name": "IB69T", "marks": 15},
    {"name": "66yv58", "marks": 93},
    {"name": "GlXD13", "marks": 51},
    {"name": "XeV", "marks": 35},
    {"name": "AzNNt5q", "marks": 28},
    {"name": "AQLHcS", "marks": 49},
    {"name": "yE9j", "marks": 71},
    {"name": "92", "marks": 57},
    {"name": "MMIXcq", "marks": 54},
    {"name": "tCkOmyz2iG", "marks": 52},
    {"name": "Ku1kl", "marks": 91},
    {"name": "RdwBMdvvE", "marks": 65},
    {"name": "WoZ18HMgh6", "marks": 69},
    {"name": "FqwrDzTp", "marks": 45},
    {"name": "pbrFuzIl", "marks": 90}
]}

@app.route('/', methods=['GET'])
@app.route('/api', methods=['GET'])
def get_marks():
    # Get the list of names from the query string
    names = request.args.getlist('name')
    
    if not names:
        return jsonify({"error": "No names provided"}), 400

    # Fetch marks using dictionary lookup
    marks = [STUDENT_DATA.get(name, 0) for name in names]

    return jsonify({"marks": marks})

# if __name__ == '__main__':
#     app.run(debug=True)
