# ac-2b - account managers are assigned

from lxml import etree

# get uuids listed in system-owner responsible party = account managers are assigned (SSP defines system owners as account managers)
query = f"//xmlns:responsible-party[@role-id='system-owner']/xmlns:party-uuid/text()"

ssp_file=''
tree = etree.parse(ssp_file)
root = tree.getroot()

namespaces = {'xmlns': 'http://csrc.nist.gov/ns/oscal/1.0'}

account_managers = root.xpath(query, namespaces=namespaces)
print(f"{account_managers=}")
result = "Pass" if account_managers else "Fail"
print("Result: " + result)
