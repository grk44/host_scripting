#1
New-ADUser -Name oprice -GivenName Oliver -Surname Price -SamAccountName oprice -AccountPassword ('Panther$' | ConvertTo-SecureString -AsPlainText -Force) -Enabled $true

#2
Set-ADAccountPassword -Identity oprice -Reset -NewPassword ('Panther$' | ConvertTo-SecureString -AsPlainText -Force)
Get-ADUser -Identity oprice -Properties "PasswordLastSet"

#3
Get-ADDefaultDomainPasswordPolicy
Set-ADDefaultDomainPasswordPolicy -LockoutThreshold 3 -Identity contoso.com
Get-ADDomain | select forest
# runas /noprofile /user:oprice@contoso.com cmd.exe
Get-ADUser -Filter "name -like 'oprice'" -Properties lockedout
Search-ADAccount -LockedOut
Unlock-ADAccount -Identity oprice

#4
Get-ADUser -Filter "surname -like 'H*'"