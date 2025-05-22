import sys
from lxml import etree
from constants import *

def check_file_path(file_path: str) -> bool:
    if len(file_path) == 0:
        print("Ensure all file paths are defined in constants.py")
        return False
    return True

def get_elementtree_root(file: str):
    if not check_file_path(file):
        sys.exit(1)
    
    tree = etree.parse(file) # type: ignore (uses default parameter)
    root = tree.getroot()
    return root

def run_acl_expr(expr: str, node=None):
    if node is None:
        node = get_elementtree_root(ACL_FILE)
    return node.xpath(expr, namespaces=NAMESPACES)

def run_ssp_expr(expr: str, node=None):
    if node is None:
        node = get_elementtree_root(SSP_FILE)
    return node.xpath(expr, namespaces=NAMESPACES)

def run_sap_expr(expr: str, node=None):
    if node is None:
        node = get_elementtree_root(SAP_FILE)
    return node.xpath(expr, namespaces=NAMESPACES)

def get_ssp_statement_description(statement_id: str) -> str:
    expr_ssp_description = f"//oscal:statement[@statement-id='{SSP_STATEMENT_ID_PREFIX}{statement_id}']/oscal:by-component/oscal:description/*/descendant-or-self::text()"
    get_ssp_description = run_ssp_expr(expr_ssp_description)
    ssp_description = ''
    for i in get_ssp_description:
        ssp_description += (i + " ")
    return ssp_description

def get_sap_task_description(statement_id: str) -> str:
    expr_sap_description = f"//oscal:task[oscal:prop[@value='{SAP_STATEMENT_ID_PREFIX}{statement_id}']]/oscal:description/*/descendant-or-self::text()"
    get_sap_description = run_sap_expr(expr_sap_description)
    sap_description = ''
    for i in get_sap_description:
        sap_description += (i + " ")
    return sap_description