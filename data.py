from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Public Google Sheets link in CSV format
SHEET_URL = "https://docs.google.com/spreadsheets/d/1Zj2-dQq57-6NtL-y5AU-WIOauSdgb_F4/export?format=csv"

@app.route('/data', methods=['GET'])
def get_data():
    try:
        df = pd.read_csv(SHEET_URL)
        return jsonify(df.to_dict(orient="records"))  # Convert DataFrame to JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
