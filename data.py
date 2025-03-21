from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Public Google Sheets link in CSV format
SHEET_URL = "https://docs.google.com/spreadsheets/d/1Zj2-dQq57-6NtL-y5AU-WIOauSdgb_F4/export?format=csv"

@app.route('/data', methods=['GET'])
def get_data():
    """Fetch all order data from Google Sheets."""
    try:
        df = pd.read_csv(SHEET_URL)
        return jsonify(df.to_dict(orient="records"))  # Convert DataFrame to JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/orderstatus/<order_id>', methods=['GET'])
def order_status(order_id):
    """Fetch the status of an order by Order ID."""
    try:
        df = pd.read_csv(SHEET_URL)

        # Check if Order ID exists
        order = df[df['Order ID'] == order_id]
        if not order.empty:
            status = order.iloc[0]['Status']
            return jsonify({"Order ID": order_id, "Status": status})
        else:
            return jsonify({"error": "Order not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
