# ac-2a - parse SSP and determine whether privileged and non-privileged roles are documented

from utils import run_ssp_expr, get_ssp_statement_description, get_sap_task_description

# user_type = 'privileged' # privileged or non-privileged
# expr = f"//oscal:role[oscal:prop[@name='privilege-level' and @value='{user_type}']]/@id"
expr_privileged = f"//oscal:role[oscal:prop[@name='privilege-level' and @value='privileged']]/@id"
expr_nonprivileged = f"//oscal:role[oscal:prop[@name='privilege-level' and @value='non-privileged']]/@id"

get_privileged_roles = run_ssp_expr(expr_privileged)
get_nonprivileged_roles = run_ssp_expr(expr_nonprivileged)

print("SSP description:\n")
print(get_ssp_statement_description("a") + "\n")
print("SAP description:\n")
print(get_sap_task_description("a") + "\n")

# print(user_type)
print(f"{get_privileged_roles=}")
print(f"{get_nonprivileged_roles=}")

result = "Pass" if get_privileged_roles and get_nonprivileged_roles else "Fail"
print("Result: " + result)
