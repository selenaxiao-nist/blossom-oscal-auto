# ac-2b - account managers are assigned

from lxml import etree
from ..constants import NAMESPACES, SSP_FILE

# get uuids listed in system-owner responsible party = account managers are assigned (SSP defines system owners as account managers)
query = f"//xmlns:responsible-party[@role-id='system-owner']/xmlns:party-uuid/text()"

tree = etree.parse(SSP_FILE)
root = tree.getroot()

account_managers = root.xpath(query, namespaces=NAMESPACES)
print(f"{account_managers=}")
result = "Pass" if account_managers else "Fail"
print("Result: " + result)
