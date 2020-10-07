from ucsmsdk.ucshandle import UcsHandle
import pprint

def main():
    handle = UcsHandle("192.168.254.200","ucspe","ucspe", secure=False)
    handle.login()
    print(" ==== Printing Off Handle ==== ")
    pprint.pprint(vars(handle))
    print(" ==== Printed Off Handle ==== ")
    
    ## Print IP address of UCSM
    print(handle.ip)

    ## Print UCS Name
    print(handle.ucs)

    ## Print Cookie
    print(handle.cookie)

    handle.logout()

if __name__ == "__main__":
    main()
