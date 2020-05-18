from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

import pprint

def main():
    handle = UcsHandle("192.168.254.200","ucspe","ucspe", secure=False)
    handle.login()

    # Query for existing vlan
    vlan_100 = handle.query_dn("fabric/lan/net-vlan100")
    print(vlan_100.dn, vlan_100.sharing)

    # Update sharing type to primary
    vlan_100.sharing = "primary"

    # Add the object to be ready to be committed
    handle.set_mo(vlan_100)
    
    # Commit changes back to UCS
    handle.commit()

    # Get Updated vlan
    vlan_100 = handle.query_dn("fabric/lan/net-vlan100")
    print(vlan_100.dn, vlan_100.sharing)

    handle.logout()

if __name__ == "__main__":
    main()
