from flask import Flask, request, jsonify
import re
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

class OrderValidator:
    def __init__(self, data):
        self.data = data
        self.errors = []

    def validate(self):
        self.validate_name()
        self.validate_price()
        self.validate_currency()
        return self.errors

    def validate_name(self):
        name = self.data.get('name', '')
        if not re.match(r'^[A-Za-z\s]+$', name):
            self.errors.append('400 - name contains non-english characters')
        if not all(word[0].isupper() for word in name.split()):
            self.errors.append('400 - name is not capitalized')

    def validate_price(self):
        try:
            price = float(self.data.get('price', 0))
        except ValueError:
            self.errors.append('400 - price must be a number')
            return
        if price > 2000:
            self.errors.append('400 - price is over 2000')

    def validate_currency(self):
        currency = self.data.get('currency', '')
        if currency not in ['TWD', 'USD']:
            self.errors.append('400 - currency format is wrong')

class OrderService:
    def __init__(self, data):
        self.data = data
        self.errors = []

    def transform(self):
        if self.data['currency'] == 'USD':
            original_price = float(self.data['price'])
            if original_price > 65:
                self.errors.append('400 - price is over 2000')
                return None
            converted_price = round(original_price * 31, 2)
            if converted_price > 2000:
                self.errors.append('400 - price after conversion is over 2000')
                return None
            self.data['price'] = converted_price
            self.data['currency'] = 'TWD'
        return self.data

@app.route('/api/orders', methods=['POST'])
def process_order():
    data = request.json
    app.logger.debug(f"Received data: {data}")
    
    # Step 1: Form validation
    validator = OrderValidator(data)
    errors = validator.validate()
    app.logger.debug(f"Validation errors: {errors}")
    if errors:
        return jsonify({'errors': errors}), 400
    
    # Step 2: Service (Format checking & transform)
    service = OrderService(data)
    transformed_data = service.transform()
    
    if transformed_data is None:
        return jsonify({'errors': service.errors}), 400
    
    app.logger.debug(f"Transformed data: {transformed_data}")

    # Step 3: Response
    return jsonify(transformed_data), 200

if __name__ == '__main__':
    app.run(debug=True)
