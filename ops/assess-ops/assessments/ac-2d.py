# ac-2d - parse users in ACL and match with SSP

from utils import run_ssp_expr, run_acl_expr, get_ssp_statement_description, get_sap_task_description
from pprint import pprint

print("SSP description:\n")
print(get_ssp_statement_description("d.1") + "\n")
print("SAP description:\n")
print(get_sap_task_description("d.1") + "\n")

expr = f"//aws:Grantee[aws:ID and aws:DisplayName]" # Get Grantee (user) elements that contain ID (UUID) and DisplayName (role). Some Grantee elements aren't users.

get_users_acl = run_acl_expr(expr)

users_acl_result = {}
for user in get_users_acl:
    uuid = run_acl_expr('aws:ID/text()', user)[0]
    role = run_acl_expr('aws:DisplayName/text()', user)[0]

    if uuid not in users_acl_result:
        users_acl_result[uuid] = {'uuid': uuid, 'role':role}

users_acl_list = list(users_acl_result.values())

pprint(f"{users_acl_list=}")
# for user in users_acl_list:
#     pprint(user)

roles = ["system-owner"]

# Match with SSP
expr = f"//oscal:responsible-party[@role-id='system-owner']/oscal:party-uuid/text()"
ssp_system_owners = run_ssp_expr(expr)
pprint(f"{ssp_system_owners=}")

# 1. read ssp responsible parties for users, then check those users exist in ACL (contains only users in the cloud), Cognito, chaincode (acquisition officer, authorizing official, license owner)

