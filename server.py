from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()

        # Safety check in case data is not sent
        if data is None:
            return jsonify({'error': 'No data received'}), 400

        # Extract and convert input values
        rent = int(data.get('rent', 0))
        food = int(data.get('food', 0))
        elec = int(data.get('elec', 0))
        unit = int(data.get('unit', 0))
        members = int(data.get('members', 1))

        if members == 0:
            return jsonify({'error': 'Number of members cannot be zero'}), 400

        # Perform calculation
        elec_bill = elec * unit
        total_spend = rent + food + elec_bill
        per_head = total_spend // members

        return jsonify({'per_head': per_head})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
