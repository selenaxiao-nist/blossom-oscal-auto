import sys
from lxml import etree
from constants import NAMESPACES, ACL_FILE, SSP_FILE

def check_file_path(file_path: str) -> bool:
    if len(file_path) == 0:
        print("Ensure SSP_FILE and ACL_FILE are defined in constants.py")
        return False
    return True

def get_elementtree_root(file: str):
    if not check_file_path(file):
        sys.exit(1)
    
    tree = etree.parse(file) # type: ignore (uses default parameter)
    root = tree.getroot()
    return root

def run_acl_query(query: str, node=None):
    if node is None:
        node = get_elementtree_root(ACL_FILE)
    return node.xpath(query, namespaces=NAMESPACES)

def run_ssp_query(query: str, node=None):
    if node is None:
        node = get_elementtree_root(SSP_FILE)
    return node.xpath(query, namespaces=NAMESPACES)
