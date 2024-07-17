from flask import Flask, request, jsonify
import logging
from validators import NameValidator, PriceValidator, CurrencyValidator
from transformers import CurrencyTransformer
from services import OrderProcessor

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/api/orders', methods=['POST'])
def process_order():
    data = request.json
    app.logger.debug(f"Received data: {data}")

    # Validators and Transformers
    validators = [NameValidator(), PriceValidator(), CurrencyValidator()]
    transformers = [CurrencyTransformer()]

    # Process order
    processor = OrderProcessor(validators, transformers)
    result, status_code = processor.process(data)
    app.logger.debug(f"Processing result: {result}")

    return jsonify(result), status_code

if __name__ == '__main__':
    app.run(debug=True)
