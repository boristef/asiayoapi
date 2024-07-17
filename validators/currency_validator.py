class CurrencyValidator:
    def validate(self, data):
        errors = []
        currency = data.get('currency', None)
        if currency is None:
            errors.append('400 - currency is required')
            return errors
        if currency not in ['TWD', 'USD']:
            errors.append('400 - currency format is wrong')
        return errors
