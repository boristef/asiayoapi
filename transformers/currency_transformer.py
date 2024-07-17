class CurrencyTransformer:
    def transform(self, data):
        if data['currency'] == 'USD':
            data['price'] = round(float(data['price']) * 31, 2)
            if data['price'] > 2000:
                data['errors'] = ['400 - price is over 2000']
            data['currency'] = 'TWD'
        return data
