#Q1: Create accounts
New-ADUser -Name jjohnny -GivenName Johnny -Surname Test -SamAccountName jjohnny -EmailAddress johnny@contoso.com -AccountPassword ('Panther$' | ConvertTo-SecureString -AsPlainText -Force) -Enabled $true
New-ADUser -Name jbravo -GivenName Johnny -Surname Bravo -SamAccountName jbravo -EmailAddress bravo@contoso.com -AccountPassword ('Panther$' | ConvertTo-SecureString -AsPlainText -Force) -Enabled $true
New-ADUser -Name jquest -GivenName Johnny -Surname Quest -SamAccountName jquest -EmailAddress jquest@contoso.com -AccountPassword ('Panther$' | ConvertTo-SecureString -AsPlainText -Force) -Enabled $true

#Q2: Show Accounts
Get-ADUser -Identity jjohnny
Get-ADUser -Identity jbravo
Get-ADUser -Identity jquest

#Q3: Set Johnny Test account expiration date
Set-ADAccountExpiration -Identity jjohnny -DateTime "01/01/2015"
Get-ADUser -Identity jjohnny -Properties "AccountExpirationDate"

#Q4: Enable jbravo account
Set-ADUser -Identity jbravo -Enabled $true
Get-ADUser -Identity jbravo

#Q5: Reset jbravo password
Set-ADAccountPassword -Identity jbravo -Reset -NewPassword ('Panther$' | ConvertTo-SecureString -AsPlainText -Force)
Get-ADUser -Identity jbravo -Properties "PasswordLastSet"

#Q6: Remove jbravo
Remove-ADUser -Identity jbravo
Get-ADUser -Identity jbravo