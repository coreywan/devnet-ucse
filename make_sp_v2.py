
## Converts Nick's script to Cisco SDK

## Downside - It doesn't actually associate the template with a server

from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.ucsmethodfactory import ls_instantiate_n_template
from ucsmsdk.ucsbasetype import DnSet, Dn

NUM_SP = 3

def main():
    handle = UcsHandle("192.168.254.200","ucspe","ucspe", secure=False)
    handle.login()

    # Create XML Object to create template clone
    templates = ls_instantiate_n_template(
        cookie=handle.cookie,
        dn="org-root/ls-globotemplate",
        in_target_org="org-root",
        in_server_name_prefix_or_empty="SP",
        in_number_of=str(NUM_SP),
        in_hierarchical="no"
    )
    # Send XML Object to xml process handler
    mo_list = handle.process_xml_elem(templates)
    
    for mo in mo_list:
        print(mo.dn)

if __name__ == "__main__":
    main()
