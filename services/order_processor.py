class OrderProcessor:
    def __init__(self, validators, transformers):
        self.validators = validators
        self.transformers = transformers

    def process(self, data):
        errors = []
        for validator in self.validators:
            errors.extend(validator.validate(data))
        if errors:
            return {'errors': errors}, 400

        for transformer in self.transformers:
            data = transformer.transform(data)
            if 'errors' in data:
                errors.extend(data['errors'])

        if errors:
            return {'errors': errors}, 400

        return data, 200
