OU#1 import csv of groups
Import-Csv C:\Users\Administrator\Desktop\departments-1.csv | % {New-ADOrganizationalUnit -Name $_.department}
#2 change to users directory in AD
Get-PSDrive
cd "AD:\cn=users,dc=contoso,dc=com"

#making group and user array
New-ADGroup -Name Marketing -GroupScope Global -Path "OU=Marketing,DC=contoso,DC=com" -Server dc1
$mktUsers= @('Robin.Horton','Jan.Shelton','Stewart.Graves','Carrie.Rivera','Pamela.Sanchez')

#3 add users to maketing group
foreach($u in $mktUsers){
    Add-ADGroupMember Marketing $u
}

#4 move users to maketing ou
foreach ($u in $mktUsers){
    move .\cn=$u ..\OU=Marketing 
}

#5 set department to marketing
foreach($u in $mktUsers){
    Set-ADUser -Identity $u -Department Marketing
}

#6 move to marketing container and list 
cd "AD:\OU=Marketing,DC=contoso,DC=com"
Get-ADUser -Filter * -Properties Name,Department,Memberof |Select-Object -Property Name,Department,Memberof 