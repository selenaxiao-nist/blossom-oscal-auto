import sys
from lxml import etree
from constants import NAMESPACES, ACL_FILE, SSP_FILE

def check_file_path(file_path: str) -> bool:
    if not file_path:
        print("Ensure SSP_FILE and ACL_FILE are defined in constants.py")
        return False
    return True

def get_elementtree_root(file: str):
    if not check_file_path(file):
        sys.exit(1)
    
    tree = etree.parse(file) # type: ignore (uses default parameter)
    root = tree.getroot()
    return root

def run_acl_query(query: str):
    root = get_elementtree_root(ACL_FILE)
    return root.xpath(query, namespaces=NAMESPACES)

def run_ssp_query(query: str):
    root = get_elementtree_root(SSP_FILE)
    return root.xpath(query, namespaces=NAMESPACES)
