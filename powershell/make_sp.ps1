## Import Required Powershell Modules
import-module Cisco.UCSManager

$num_sp = 3
$blade_model = 'UCSB-B200-M4'

## Create Credential Object
$password = ConvertTo-SecureString "ucspe" -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential ("ucspe", $password)

# Log into UCS 
connect-ucs 192.168.254.200 -Credential $creds

# Query for unassociated blades of the type $blade_model
$blades = get-ucsblade | where-object {$_.model -eq $blade_model -and $_.operstate -eq 'unassociated'}
write-host $blades.count available blades were found

# Error Check for available blades
if ($blades.count -lt $num_sp){
    $errormsg = "There are only $($blades.count) blades left to associate, and you asked for $num_sp Servers to be generated"
    throw $errormsg
}

$spTemplate = get-ucsserviceprofile -Name globotemplate_powershell

$spCreated = $spTemplate  | Add-UcsServiceProfileFromTemplate -Prefix SP -Count $num_sp 

$counter = 0
foreach ($sp in $spCreated){
    $blade = $blades[$counter] 
    write-host Associating Blade $blade.Dn with $sp.Dn
    associate-ucsServiceProfile -ServiceProfile $sp -Blade $blade -Force | out-null
    ++$counter
}

disconnect-ucs
