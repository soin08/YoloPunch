from django.core.validators import RegexValidator


class UsernameValidator(RegexValidator):
    def __init__(self):
        regex='^[a-z0-9.-_]{3,20}$'
        message = 'Username is not valid'
        super(RegexValidator, self).__init__(regex=regex, message=message)
