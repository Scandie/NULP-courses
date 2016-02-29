import re
""" Task #1 : Create a class Lonely, which can have only one Instance """
print """
Task #1:
"""


class Lonely(object):
    my_instance = None

    def __new__(cls, name, age):
        if cls.my_instance is None:
            cls.my_instance = object.__new__(cls)
        return cls.my_instance

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Lonely(my name is:{} and i am {})'.format(self.name, self.age)


a = Lonely('Ann', 19)
print a
b = Lonely('Bob', 48)
print b


""" Task #2 : Create class Observable.
a)which can take **kwargs as arguments and assign all values from it to new Instance.
Example:
    obs = Observable(name='Jack', work='dev', jobs=('developer', '2 year'), titles={'senior dev': 'Google'})
    print obs.name
    >> Jack
b) Modify class that when you print Object of this class  in python interpreter it will show
you all params with which object was created(order is not required)
Example:
    print obs
    Observable(titles:{'senior dev': 'Google'},work:dev,jobs:('developer', '2 year'),name:Jack)
 """

print """
Task #2:
"""


class Observable(object):

    def __str__(self):
        result = 'Observable('
        for i in range(len(self.keys)):
            message = '{}:{}'.format(self.keys[i], self.values[i])
            if i != len(self.keys)-1:
                result += message + ','
            else:
                result += message
        return result + ')'

    def __init__(self, **kwargs):
        self.keys = []
        self.values = []
        for key, value in kwargs.items():
            self.__setattr__(key, value)
            self.keys.append(key)
            self.values.append(self.__getattribute__(key))

obs = Observable(name='Jack', work='dev', jobs=('developer', '2 year'), titles={'senior dev': 'Google'})
print obs.name
print obs


""" Task #3 :
a) Create class RegexValidator with attributes regex and message. Regex attribute will be used for further
validation, and message - for custom Error messages in case of ValidationError occur.
Instances of this class should have possibility to be called. Same as you call a function - function_stupid(1,2,3),
instance of validator described above should have possibility to be called and validate input with regex that it have in
attributes.

b) Create EmailValidator that will inherit from RegexValidator and validate emails in same fashion as parent
validator does(except it should validate emails).Also it should rise appropriate Exception, like 'This email is not
valid'.
Note: do not bother much about validation for email. It should be enough that email should have '@' and '.'. Main idea
of these exercises  is OOP.

 """

print """
Task #3:
"""


class CustomValidationError(Exception):
    pass


class RegexValidator(object):

    def __init__(self, regex, message):
        self.regex = regex
        self.message = message

    def __call__(self, some_text):
        self.some_text = some_text
        if not re.match(self.regex, self.some_text):
            raise CustomValidationError(self.message)
        else:
            print (str(self.some_text) + " is valid value")

validator = RegexValidator(regex='^[A-Z]$', message='Ouch! your input is not valid!')
validator('K')
#validator('f*ck')


class EmailValidator(RegexValidator):

        def __init__(self):
            RegexValidator.__init__(self, regex='[\w.]+[@][\w.][a-z]', message='Something wrong with your address!')


mail_validator = EmailValidator()
mail_validator('grizly.vl@gmail.com')
mail_validator('johnycage@mortalkomb.at.net')
mail_validator('howtoemail.net')




