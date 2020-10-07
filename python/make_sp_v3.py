
## Same as v2, but uses a named Template, instead of auto generating... This is more idempotent

from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.ucsmethodfactory import ls_instantiate_n_named_template
from ucsmsdk.ucsmethodfactory import ls_instantiate_n_template
from ucsmsdk.ucsbasetype import DnSet, Dn

NUM_SP = 3

def main():
    handle = UcsHandle("192.168.254.200","ucspe","ucspe", secure=False)
    handle.login()

    # Setup Variable for SP Templates to be deployed
    dn_set = DnSet()
    for i in range(1, NUM_SP+1):
        dn = Dn()
        sp_name = "SP{}".format(str(i))
        dn.attr_set("value", sp_name)
        dn_set.child_add(dn)

    # Build XML Object to submit to the API
    templates = ls_instantiate_n_named_template(
        cookie=handle.cookie,
        dn="org-root/ls-globotemplate",
        in_target_org="org-root",
        in_error_on_existing="false",
        in_name_set=dn_set
        )

    # Send XML Object to xml process handler
    mo_list = handle.process_xml_elem(templates)
    
    for mo in mo_list:
        print(mo.dn)

if __name__ == "__main__":
    main()
