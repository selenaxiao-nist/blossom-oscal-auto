# ac-2b - account managers are assigned

from utils import run_ssp_query

# get uuids listed in system-owner responsible party = account managers are assigned (SSP defines system owners as account managers)
query = f"//oscal:responsible-party[@role-id='system-owner']/oscal:party-uuid/text()"

account_managers = run_ssp_query(query)
print(f"{account_managers=}")
result = "Pass" if account_managers else "Fail"
print("Result: " + result)
