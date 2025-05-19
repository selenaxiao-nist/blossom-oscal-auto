# ac-2a - parse SSP and determine whether privileged and non-privileged roles are documented

from lxml import etree
from ..constants import NAMESPACES, SSP_FILE

# user_type = 'privileged' # privileged or non-privileged
# query = f"//xmlns:role[xmlns:prop[@name='privilege-level' and @value='{user_type}']]/@id"
query_privileged = f"//xmlns:role[xmlns:prop[@name='privilege-level' and @value='privileged']]/@id"
query_nonprivileged = f"//xmlns:role[xmlns:prop[@name='privilege-level' and @value='non-privileged']]/@id"

tree = etree.parse(SSP_FILE)
root = tree.getroot()

get_privileged_roles = root.xpath(query_privileged, namespaces=NAMESPACES)
get_nonprivileged_roles = root.xpath(query_nonprivileged, namespaces=NAMESPACES)
# print(user_type)
print(f"{get_privileged_roles=}")
print(f"{get_nonprivileged_roles=}")
result = "Pass" if get_privileged_roles and get_nonprivileged_roles else "Fail"
print("Result: " + result)
