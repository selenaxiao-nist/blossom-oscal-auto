# ac-2a - parse SSP and determine whether privileged and non-privileged roles are documented

from utils import run_ssp_query

# user_type = 'privileged' # privileged or non-privileged
# query = f"//oscal:role[oscal:prop[@name='privilege-level' and @value='{user_type}']]/@id"
query_privileged = f"//oscal:role[oscal:prop[@name='privilege-level' and @value='privileged']]/@id"
query_nonprivileged = f"//oscal:role[oscal:prop[@name='privilege-level' and @value='non-privileged']]/@id"

get_privileged_roles = run_ssp_query(query_privileged)
get_nonprivileged_roles = run_ssp_query(query_nonprivileged)

# print(user_type)
print(f"{get_privileged_roles=}")
print(f"{get_nonprivileged_roles=}")

result = "Pass" if get_privileged_roles and get_nonprivileged_roles else "Fail"
print("Result: " + result)
