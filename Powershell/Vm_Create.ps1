New-VM -Name Marketing -MemoryStartupBytes 512MB -NewVHDPath "C:\VM\Virtual Hard Disks\Marketing01.vhdx" -NewVHDSizeBytes 127GB
Set-VMMemory -VMName Marketing -DynamicMemoryEnabled $true -MaximumBytes 3GB
Set-VMProcessor -VMName Marketing -Count 2
Set-VMDvdDrive -VMName Marketing -Path "C:\Users\student\Downloads\TinyCore-current.iso"

New-VM -name $vm.VMName -MemoryStartupBytes $msb -VHDPath C:\VM\'Virtual Hard Disks'\$vm.VHD -NewVHDSizeBytes $vhdsize