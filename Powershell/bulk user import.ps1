Import-Csv C:\Users\Administrator\Desktop\ADuserlist.csv |
 % {New-ADUser -Name ($_.fname + "." + $_.lname) -SamAccountName 
 ($_.fname + "." + $_.lname) -GivenName $_.fname -Surname $_.lname 
 -EmailAddress $_.email -Department $_.department
  -AccountPassword ('Panther$' | ConvertTo-SecureString -AsPlainText -Force) 
  -Enabled $true}