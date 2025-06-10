# ac-2c - parse SSP and determine whether all users have a NIST valid email

from utils import *

print_current_control(__file__)

if len(EMAIL_DOMAIN) == 0:
    print("Ensure email domain is defined in constants.py")
    sys.exit(1)


expr_emails = f"//oscal:party/oscal:email-address/text()"

get_emails = run_ssp_expr(expr_emails)

print("SSP description:\n")
print(get_ssp_statement_description("c") + "\n")
print("SAP description:\n")
print(get_sap_task_description("c") + "\n")

print(f"{get_emails=}")

get_valid_emails = []
for email in get_emails:
    email = str(email)
    if email.endswith(EMAIL_DOMAIN):
        get_valid_emails.append(email)

result = "Pass" if len(get_emails) == len(get_valid_emails) else "Fail"
print("Result: " + result)
