#Greg Kessel
#3/18/21
#Excerise 3

#Import CSV to Variable
$Newusers=Import-Csv C:\Users\Administrator\Desktop\users.csv 

#Create Characters for password Generation
$chars = "abcdefghijkmnopqrstuvwxyzABCEFGHJKLMNPQRSTUVWXYZ23456789!#%&?".ToCharArray()

#Create new accounts
Foreach ($i in $NewUsers){
    #Generate and output passwords and usernames
        #Yes I found the password generator online and copy paste almost all of it
$newPassword=""
1..12 | ForEach {  $newPassword += $chars | Get-Random }
New-ADUser -Name ($i.UserFirstName + "-" + $i.UserLastName) -SamAccountName ($i.UserFirstName + "-" + $i.UserLastName) -Department $i.GroupOU -GivenName $i.UserFirstName -Surname $i.UserLastName -AccountPassword ($newPassword | ConvertTo-SecureString -AsPlainText -Force) -Enabled $true
($i.UserFirstName + "-" + $i.UserLastName + "---" + $newPassword)| out-file -Append $end:USERPROFILE\Desktop\NewUserPass.txt
}

#get new unique groups
$newGroups=$Newusers
$newGroupsU = $newGroups.GroupOU | Select-Object -Unique
#Create new groups
psdrive
cd AD:\
foreach($g in $newGroupsU){
New-ADOrganizationalUnit -Name $g 
New-ADGroup -Name $g -GroupScope Global -SamAccountName $g 
}

#assign group members
foreach($p in $Newusers){
    Add-ADGroupMember $p.GroupOU ($p.UserFirstName + "-" + $p.UserLastName)
}

#generate User group and name log
foreach($q in $newGroupsU){
$UNG=Get-ADGroupMember $q | Select-Object -Property Name
    foreach($w in $UNG){
    $e=Get-ADUser $w.name | Select-Object -Property GivenName, Surname
    
    ($q + " " +$e.GivenName +" " +$e.Surname + " " + $w.name) | Out-File -Append $env:USERPROFILE\Desktop\user_group_log.txt
    }
}