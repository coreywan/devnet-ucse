## This script associates the SP to a Server

from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.ucsmethodfactory import ls_instantiate_n_named_template
from ucsmsdk.ucsmethodfactory import ls_instantiate_n_template
from ucsmsdk.ucsbasetype import DnSet, Dn
from ucsmsdk.mometa.ls.LsBinding import LsBinding

NUM_SP = 3
BLADE_MODEL = 'UCSB-EX-M4-1'
def main():
    handle = UcsHandle("192.168.254.200","ucspe","ucspe", secure=False)
    handle.login()

    # Query Blades that are unassociated
    print("\n\n=== Query Based on Class Name with Filter equal to")
    filter = "(oper_state,'unassociated',type='eq')".format(BLADE_MODEL)
    blades = handle.query_classid("computeBlade",filter_str=filter)
    print("***Found {} Blades".format(len(blades)))

    # Error Check for available blades
    if len(blades) < NUM_SP:
        error = "There are only {} blades left to associate, and you asked for {} Servers to be generated".format(len(blades),NUM_SP)
        raise NameError(error)
        
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
    sp_list = handle.process_xml_elem(templates)

    # Loop through each created sp, and associate them to blades
    i = 0
    while i < len(sp_list):
        sp = sp_list[i]
        blade = blades[i]

        # Print SP and Blade Combination
        print(sp.dn,blade.dn)

        # Get Binding Object
        mo = LsBinding(
            parent_mo_or_dn=sp.dn,
            pn_dn=blade.dn,
            restrict_migration="no"
            )
        
        # Add MO Binding Object to handler
        handle.add_mo(mo,modify_present=True)
        i=i+1

    # Bundle the SP Associates
    handle.commit()

if __name__ == "__main__":
    main()
