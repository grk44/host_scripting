
[int]$VMcount = 0
$VMcount=Read-Host 'How Many VMs are you Creating Today?'

$i=0
while ($i -lt $VMcount) {
    New-VM -Name HR_$i -MemoryStartupBytes 256MB -NewVHDPath "C:\VM\Virtual Hard Disks\HR_$i.vhdx" -NewVHDSizeBytes 10GB -SwitchName Production
    Set-VMMemory -VMName HR_$i -DynamicMemoryEnabled $true -MaximumBytes 2GB    
    Write-Host 'Virtual Machine HR_'$i' Created'
    $i++
}

$i1=0
while ($i1 -lt $VMcount) {
    Start-VM -Name HR_$i1
    Write-Host 'Virtual Machine HR_'$i' Started'
    $i1++
}
