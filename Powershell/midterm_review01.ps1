Get-Content -Path C:\Users\Greg\Desktop\firewall-log.txt
$regex = '((.{2}:){5})'
Select-String -Path C:\users\Greg\Desktop\firewall-log.txt -AllMatches -Pattern '((.{2}:){5}.{2})' | % {$_.Matches} |% {$_.Value}