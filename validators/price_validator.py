class PriceValidator:
    def validate(self, data):
        errors = []
        price = data.get('price', None)
        if price is None:
            errors.append('400 - price is required')
            return errors
        try:
            price = float(price)
        except ValueError:
            errors.append('400 - price must be a number')
            return errors
        if price > 2000:
            errors.append('400 - price is over 2000')
        return errors
