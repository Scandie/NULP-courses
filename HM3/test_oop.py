from unittest import TestCase, main
from oop_homework import EmailValidator, CustomValidationError


class EmailValidatorTesting(TestCase):
    def setUp(self):
        self.mail = EmailValidator()

    def test_email_regex_raise(self):
        self.assertRaisesRegexp(CustomValidationError, self.mail.message, self.mail, 'unpropermail')

if __name__ == '__main__':
    main()
