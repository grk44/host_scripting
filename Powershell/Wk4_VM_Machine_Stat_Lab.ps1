Start-VM -Name Marketing
Save-VM -Name Marketing
Stop-VM -Name Marketing

function checkVM {
    param ([string]$vmname)
        $vmstate = Get-VM $vmname | Where-Object -Property Name
        Write-Host $vmstate.State
        switch ($vmstate.State) {
            Off { 
                Write-Host "The VM "$vmname "is off, starting now"
                Start-VM $vmname
             }
             Running{
                 Write-Host "The VM "$vmname "is Running"
             }
            Default {}
        }    
    
}