from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

import pprint

def main():
    handle = UcsHandle("192.168.254.200","ucspe","ucspe", secure=False)
    handle.login()
    
    # Get Parrent Object
    lan_cloud = handle.query_classid("FabricLanCloud")

    # Create new VLAN Object for vlan 100
    vlan_mo = FabricVlan(parent_mo_or_dn=lan_cloud[0], name="vlan100", id="100")

    # Add the object to be ready to be committed
    handle.add_mo(vlan_mo)
    
    # Commit changes back to UCS
    handle.commit()

    handle.logout()

if __name__ == "__main__":
    main()
