# ac-2b - account managers are assigned

from utils import *

print_current_control(__file__)

# get uuids listed in system-owner responsible party = account managers are assigned (SSP defines system owners as account managers)
expr = f"//oscal:responsible-party[@role-id='system-owner']/oscal:party-uuid/text()"

print("SSP description:\n")
print(get_ssp_statement_description("b") + "\n")
print("SAP description:\n")
print(get_sap_task_description("b") + "\n")

account_managers = run_ssp_expr(expr)
print(f"{account_managers=}")
result = "Pass" if account_managers else "Fail"
print("Result: " + result)
