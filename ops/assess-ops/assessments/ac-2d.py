# ac-2d - parse users in ACL and match with SSP

from utils import *
from pprint import pprint
from constants import ROLES

print_current_control(__file__)

print("SSP description:\n")
print(get_ssp_statement_description("d.1") + "\n")
print("SAP description:\n")
print(get_sap_task_description("d.1") + "\n")

expr = f"//aws:Grantee[aws:ID and aws:DisplayName]" # Get Grantee (user) elements that contain ID (UUID) and DisplayName (role). Some Grantee elements aren't users.

get_acl_users = run_acl_expr(expr)

acl_users_result = {}
for user in get_acl_users:
    uuid = run_acl_expr('aws:ID/text()', user)[0]
    role = run_acl_expr('aws:DisplayName/text()', user)[0]

    if uuid not in acl_users_result:
        acl_users_result[uuid] = {'uuid': uuid, 'role':role}

acl_users_list = list(acl_users_result.values())
# pprint(f"{users_acl_list=}")
acl_users_dict = {}
for user in acl_users_list:
    uuid = user['uuid']
    role = user['role']
    acl_users_dict[uuid] = role
pprint(f"{acl_users_dict=}")

# for user in users_acl_list:
#     pprint(user)

# Match with SSP
# 1. read ssp responsible parties for users, then check those users exist in ACL (contains only users in the cloud), Cognito, chaincode (acquisition officer, authorizing official, license owner)

# ac-2.d.1 - match users
expr = f"//oscal:responsible-party[@role-id='{role}']/oscal:party-uuid/text()"

# ac-2.d.2 - match roles
for role in ROLES:
    expr = f"//oscal:responsible-party[@role-id='{role}']/oscal:party-uuid/text()"
    ssp_users = run_ssp_expr(expr)
    print(role + ": ")
    pprint(f"{ssp_users=}")

    result = "Pass, " + role + " users in ACL are defined as " + role + " users in SSP" 
    for ssp_system_owner_uuid in ssp_users:
        check_acl = acl_users_dict[ssp_system_owner_uuid]
        if check_acl != role:
            print("User " + ssp_system_owner_uuid + " does not match in ACL (" + check_acl + ") and SSP (" + role + ")")
            result = "Fail, users in ACL don't match the SSP."

    print("Result: " + result)

# ac-2.d.3 - match privileges

