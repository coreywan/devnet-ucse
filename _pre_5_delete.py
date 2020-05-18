from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

import pprint

def main():
    handle = UcsHandle("192.168.254.200","ucspe","ucspe", secure=False)
    handle.login()

    # Query for existing vlan
    vlan_100 = handle.query_dn("fabric/lan/net-vlan100")

    # Setup handle entry to remove vlan
    handle.remove_mo(vlan_100)
    
    # Commit changes back to UCS
    handle.commit()

    handle.logout()

if __name__ == "__main__":
    main()
