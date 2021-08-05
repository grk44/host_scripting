

Export-VM -Name Marketing -Path c:\export

Import-VM -Path 'C:\export\Marketing\Virtual Machines\741E76E6-03E5-4933-A437-A0A359DF85CC.vmcx' -Copy -GenerateNewId -VirtualMachinePath 'C:\VM\Markting2' -VhdDestinationPath 'C:\VM\VM2'

