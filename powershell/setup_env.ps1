## Import Required Powershell Modules
import-module Cisco.UCSManager

## Create Credential Object
$password = ConvertTo-SecureString "ucspe" -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential ("ucspe", $password)

# Log into UCS 
connect-ucs 192.168.254.200 -Credential $creds

## Acknolwedge Chassis
get-ucschassis | Acknowledge-UcsChassis -Force

## Update MAC Pool
get-ucsmacpool | Add-UcsMacMemberBlock -From "00:25:B5:00:00:00" -To "00:25:B5:00:00:C7"

## Update UUID Pools
Get-UcsUuidSuffixPool | Add-UcsUuidSuffixBlock -From "0000-000000000001" -To "0000-0000000000C8"

## Setup Fabric Ethernet Uplink A and B Side
$lanclouds = get-ucsfilancloud
foreach($lc in $lanclouds){
    $uplink_port = $lc | Add-UcsUplinkPort -ModifyPresent -AdminState "enabled" -Name "" -PortId 1 -SlotId 1 -UsrLbl "" -AdminSpeed "10gbps"
    write-host $uplink_port.DN
}

## Setup Service Profile Template
Add-UcsServiceProfile -Type initial-template -Name globotemplate_powershell -IdentPoolName default

disconnect-ucs
