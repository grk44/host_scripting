#Greg Kessel
#3/18/21
#Exercise 2

#set variable to hold csv data
$VMimport=Import-Csv C:\Users\student\Desktop\HyperV.csv 

#perform operations on each line of csv data
foreach ($vm in $VMimport){
    #convert memory, vhd size, and vhdname to string variables
    [string]$msb=Invoke-Expression $vm.Memory
    [string]$vhdsize=Invoke-Expression $vm.VHDSize
    [string]$vhdname=$vm.VHD
    
        #create the new VM using the converted values from last step
    New-VM -name $vm.VMName -MemoryStartupBytes $msb -NewVHDPath C:\VM\VM2\$vhdname -NewVHDSizeBytes $vhdsize
    #check if dynamic memory will be enabled
    switch($vm.DynamicMemory){
        #if yes convert memory maximum to string and bytes to use in setting
        Y{$vmDM=$true
            [string]$vmMM=Invoke-Expression $vm.MemoryMaximum
            Set-VMMemory -VMName $vm.VMName -DynamicMemoryEnabled $vmDM
            Set-VMMemory -VMName $vm.VMName -MaximumBytes $vmMM 
        }
        #if N or other sets variable to false and does nothing
        N{$vmDM=$false}
        Default{$vmDM=$false}
    }
    #setting processor of the vm to the number in the csv data
    Set-VMProcessor -VMName $vm.VMName -Count $vm.Processors

    #setting and checking on vm switch options
        #getting switch names that match the desired name
    $vmSwTest=Get-VMSwitch | Where-Object -Property Name -EQ $vm.SwitchName
    #if csv switch name exists, add VM to it
    if($vmSwTest.Name -eq $vm.SwitchName){       
        Connect-VMNetworkAdapter -SwitchName $vm.SwitchName -VMName $vm.VMName         
    }
    #if switch does not exist, create and add computer to it.
    else{
        New-VMSwitch -Name $vm.SwitchName -SwitchType Internal -NetAdapterName "Ethernet 2"
        Connect-VMNetworkAdapter -SwitchName $vm.SwitchName -VMName $vm.VMName       
    }
    #start VM after Creation
    Start-VM -Name $vm.VMName
}
    #generate Reports
     Get-VM | Where-Object -Property State -EQ Running | Select-Object -Property Name,State,Uptime | ft | out-file $env:USERPROFILE\desktop\VM-report.log

     Get-VMNetworkAdapter -VMName * | Select-Object -Property VMName,SwitchName | ft | out-file $env:USERPROFILE\desktop\VM-Switch.log



function rmVM {
    param ([string]$vmname)
        $vmstate = Get-VM $vmname | Where-Object -Property Name
        Write-Host $vmstate.State
        switch ($vmstate.State) {
            Off { 
                Write-Host "The VM "$vmname "is off, Deleting Now"
                Remove-VM -Name $vmname
             }
             Running{
                 Write-Host "The VM "$vmname "is Running, Turning off and Deleting"
                 Stop-VM -Name $vmname
                 Remove-VM -Name $vmname
             }
            Default {}
        }    
    
}