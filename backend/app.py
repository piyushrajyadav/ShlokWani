from flask import Flask, jsonify, request
import json
from flask_cors import CORS  # CORS to handle cross-origin issues for React

app = Flask(__name__)
CORS(app)  # Allow all cross-origin requests

@app.route('/get-shlok/<int:chapter>/<int:shlok>', methods=['GET'])
def get_shlok(chapter, shlok):
    try:
        file_name = f"bhagavadgita_chapter_{chapter}_slok_{shlok}.json"
        # Open the file and load it as a JSON object
        with open(f"gita_data/{file_name}", 'r', encoding='utf-8') as file:
            shlok_data = json.load(file)  # Convert JSON string to a Python dictionary
        return jsonify(shlok_data), 200  # Return the data as JSON with a 200 OK status
    except FileNotFoundError:
        return jsonify({"error": "Shlok not found"}), 404  # If file is not found, return 404 error
    except UnicodeDecodeError as e:
        return jsonify({"error": f"Unicode decoding error: {str(e)}"}), 500  # Handle file decoding issues
    except json.JSONDecodeError as e:
        return jsonify({"error": f"JSON decoding error: {str(e)}"}), 500  # Handle JSON decoding issues

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
