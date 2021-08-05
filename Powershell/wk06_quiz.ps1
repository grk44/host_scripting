Get-Service | ? -Property Status -EQ 'Running'

$ADUsers1=Get-ADUser -filter * -Property Name,Department | Select-Object -Property Name,Department
foreach ($x in $ADUsers1){
    if($x.department -eq $null){
    Write-Host ($x.Name + " Has no Department")
    }
    }
    