# DevNet UCS Automation Section

## Sandbox Information

### Topology

| Server | OS | IP |
| ------ | -- | -- |
| rhel | rhel 7.8 | 192.168.254.101 |
| windows | windows server 2016 | 192.168.254.100 |
| ucspe | UCSPE Appliance | VIP 192.168.254.200 |

### NAT'd Ports

22 (ssh) -> rhel
3389 (rdp) -> windows

## Setup

1. From within vCloud Sandbox. Deploy the ucspe-sandbox catalog template.
2. Once deployed start it, and grab your NAT'd IP address, and you should be able to RDP to that windows server from your laptop.
3. Once you are in, open up powershell and install some required python packages
    ```
    pip install requests
    pip install xml2dict
    ```
