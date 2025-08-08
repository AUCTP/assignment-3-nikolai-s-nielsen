import re

def validate_email(email):
    reg = re.compile("[a-z][a-z]+(@)(hr|it|fin|mkt|ops)\.(company)\.(com)")
    m = reg.match(email)
    if m:
        return True
    else:
        return False


def get_department(email):
    reg2 = re.compile("(hr|it|fin|mkt|ops)")
    m = reg2.search(email)
    if m:
        return m.group()
    else:
        return None


def categorize_emails(email_list):
    emails = {}

    for email in email_list:
        department = get_department(email)
        if department:
            if department not in emails:
                emails[department] = []
            emails[department].append(email)
    return emails

email_list = ["jdoe@hr.company.com", "tdoe@fin.company.com"]
email = "jdoe@hr.company.com"
print(validate_email(email))
print(get_department(email))
print(categorize_emails(email_list))



# reg = re.compile("(https?://)?www\.[a-z.]+-?[a-z.]+\.(de|com|org|net|edu|co\.uk)(/[a-z]+)*")

# m = reg.match("www.google.com")
# print(m)