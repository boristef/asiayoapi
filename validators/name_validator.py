import re

class NameValidator:
    def validate(self, data):
        errors = []
        name = data.get('name', None)
        if name is None:
            errors.append('400 - name is required')
            return errors
        if not re.match(r'^[A-Za-z\s]+$', name):
            errors.append('400 - name contains non-english characters')
        if not all(word[0].isupper() for word in name.split()):
            errors.append('400 - name is not capitalized')
        return errors

