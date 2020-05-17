from ucsmsdk.ucshandle import UcsHandle

def main():
    handle = UcsHandle("192.168.254.200","ucspe","ucspe", secure=False)
    handle.login()
    print(vars(handle))


if __name__ == "__main__":
    main()
