import re

def validate_email(email):
    reg = re.compile("[a-z][a-z]+(@)(hr|it|fin|mkt|ops)\.(company)\.(com)")
    m = reg.match(email)
    if m:
        return "The email is valid: True"
    else:
        return "The email is valid: False"


def get_department(email):
    reg2 = re.compile("[a-z][a-z]+(@)(hr|it|fin|mkt|ops)\.(company)\.(com)")
    m = reg2.search(email)
    if m:
        return f'Department: {m.group(2)}'  # returns group 2 in reg2 e.g. the department name (here there are 4 groups defined by () in reg2)
    else:
        return "Department: None"


def categorize_emails(email_list):
    emails = {}

    for email in email_list:
        department = get_department(email)
        if department:
            if department not in emails:
                emails[department] = []
            emails[department].append(email)
    return emails

email = "jdoe@hr.company.com"
email_list = ["jdoe@hr.company.com", "tdoe@fin.company.com", "rdoe@mkt.company.com", "sdoe@hr.company.com"]
print(validate_email(email))
print(get_department(email))
print(f'The dictionary of emails: {categorize_emails(email_list)}')
