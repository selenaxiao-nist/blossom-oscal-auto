# ac-2d - parse users in ACL and match with SSP

from lxml import etree
from pprint import pprint
from ..constants import NAMESPACES, SSP_FILE, ACL_FILE

query = f"//aws:Grantee[aws:ID and aws:DisplayName]" # Get Grantee (user) elements that contain ID (UUID) and DisplayName (role). Some Grantee elements aren't users.

tree = etree.parse(ACL_FILE)
root = tree.getroot()

get_users_acl = root.xpath(query, namespaces=NAMESPACES)

users_acl_result = {}
for user in get_users_acl:
    uuid = user.xpath('aws:ID/text()', namespaces=NAMESPACES)[0]
    role = user.xpath('aws:DisplayName/text()', namespaces=NAMESPACES)[0]

    if uuid not in users_acl_result:
        users_acl_result[uuid] = {'uuid': uuid, 'role':role}

users_acl_list = list(users_acl_result.values())

# pprint(f"{users_acl_list=}")
for user in users_acl_list:
    pprint(user)

roles = ["system-owner"]

# Match with SSP
query = f"//oscal:responsible-party[@role-id='system-owner']/oscal:party-uuid/text()"
tree = etree.parse(SSP_FILE)
root = tree.getroot()
ssp_system_owners = root.xpath(query, namespaces=NAMESPACES)
pprint(f"{ssp_system_owners=}")

# 1. read ssp responsible parties for users, then check those users exist in ACL (contains only users in the cloud), Cognito, chaincode (acquisition officer, authorizing official, license owner)

