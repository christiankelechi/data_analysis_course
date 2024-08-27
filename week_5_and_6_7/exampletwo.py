import re
# Phone number validation
def validate_phone_number(number):
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    return bool(pattern.match(number))
# Email address validation
def validate_email(email):
    pattern = re.compile(r'^[\w-]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$')
    return bool(pattern.match(email))
# Zip code validation
def validate_zip_code(zip_code):
    pattern = re.compile(r'^\d{5}(?:[-\s]\d{4})?$')
    return bool(pattern.match(zip_code))
# Website validation
def validate_website(url):
    pattern = re.compile(r'^https?://(?:[-\w]+\.)?([-\w]+)\.[a-z]{2,6}(?:/[-\w\s./?%&=]*)?$')
    return bool(pattern.match(url))
# Testing the validation functions
phone_number = '123-456-7890'
if validate_phone_number(phone_number):
    print(f'{phone_number} is a valid phone number.')
else:
    print(f'{phone_number} is not a valid phone number.')
email_address = 'example@example.com'
if validate_email(email_address):
    print(f'{email_address} is a valid email address.')
else:
    print(f'{email_address} is not a valid email address.')
zip_code = '12345'
if validate_zip_code(zip_code):
    print(f'{zip_code} is a valid zip code.')
else:
    print(f'{zip_code} is not a valid zip code.')
website = 'https://www.example.com'
if validate_website(website):
    print(f'{website} is a valid website.')
else:
    print(f'{website} is not a valid website.')