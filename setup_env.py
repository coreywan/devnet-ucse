from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.macpool.MacpoolBlock import MacpoolBlock
from ucsmsdk.mometa.uuidpool.UuidpoolBlock import UuidpoolBlock
from ucsmsdk.mometa.fabric.FabricEthLan import FabricEthLan
from ucsmsdk.mometa.fabric.FabricEthLanEp import FabricEthLanEp
from ucsmsdk.mometa.ls.LsServer import LsServer
from ucsmsdk.mometa.equipment.EquipmentChassis import EquipmentChassis

def main():
    handle = UcsHandle("192.168.254.200","ucspe","ucspe", secure=False)
    handle.login()

    ## Acknolwedge Chassis
    mo = EquipmentChassis(parent_mo_or_dn="sys", admin_state="re-acknowledge", id="5")
    handle.add_mo(mo, True)

    ## Update MAC Pool
    mo = MacpoolBlock(parent_mo_or_dn="org-root/mac-pool-default", r_from="00:25:B5:00:00:00", to="00:25:B5:00:00:C7")
    handle.add_mo(mo)

    ## Update UUID Pools
    handle.query_dn("org-root/uuid-pool-default")
    mo = UuidpoolBlock(parent_mo_or_dn="org-root/uuid-pool-default", r_from="0000-000000000001", to="0000-0000000000C8")
    handle.add_mo(mo)

    ## Setup Fabric Ethernet Uplink A Side
    mo = FabricEthLan(parent_mo_or_dn="fabric/lan", id="A")
    mo_1 = FabricEthLanEp(parent_mo_or_dn=mo, admin_speed="10gbps", admin_state="enabled", auto_negotiate="yes", eth_link_profile_name="default", fec="auto", flow_ctrl_policy="default", name="", port_id="1", slot_id="1", usr_lbl="")
    handle.add_mo(mo, True)

    ## Setup Fabric Ethernet Uplink A Side
    mo = FabricEthLan(parent_mo_or_dn="fabric/lan", id="B")
    mo_1 = FabricEthLanEp(parent_mo_or_dn=mo, admin_speed="10gbps", admin_state="enabled", auto_negotiate="yes", eth_link_profile_name="default", fec="auto", flow_ctrl_policy="default", name="", port_id="1", slot_id="1", usr_lbl="")
    handle.add_mo(mo, True)

    ## Setup Service Profile Template
    mo = LsServer(parent_mo_or_dn="org-root", ident_pool_name="default", name="globotemplate", type="initial-template", uuid="00000000-0000-0000-0000-000000000000")
    handle.add_mo(mo)

    handle.commit()

    handle.logout()

if __name__ == "__main__":
    main()
