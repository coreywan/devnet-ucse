# DevNet UCS Automation Section

## Sandbox Information

Vapp Template: ucspe-sandbox

### Topology

| Server | OS | IP | user |
| ------ | -- | -- | ---- |
| rhel | rhel 7.8 | 192.168.254.101 | student |
| jump | windows 10 | 192.168.254.103 | admin |
| ucspe | UCSPE Appliance | VIP 192.168.254.200 | |

### NAT'd Ports

* 22 (ssh) -> rhel
* 3389 (rdp) -> jump (windows 10)

## Setup

1. From within vCloud Sandbox. Deploy the `ucspe-sandbox` catalog template.
2. Once deployed start it, and grab your NAT'd IP address, and you should be able to RDP to that windows server from your laptop.
3. Clone this git repo to windows jump box:

```sh
git clone https://github.com/coreywan/devnet-ucse.git
cd ./devnet-ucse
```

## Python Execution

1. Change down into the `python` sub directory of the git repository.
2. Execute the `setup_env.py` script
```
python ./setup_env.py
```
3. I suggest reviewing the following files starting with _pre* in order to get a context for the usmsdk python modules
4. Then look at the make_sp_* files for the Service Profile generation use case. Each one evolves from the previous.


## Powershell execution

1. Change down into the `powershell` sub directory of the git repository.
2. Execute the `setup_env.ps1` script
```
python ./setup_env.py
```
3. Review and execute `make_sp.ps1`

