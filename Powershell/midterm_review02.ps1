Select-String -Path C:\Users\Greg\Desktop\netstat.txt -AllMatches -Pattern '(\d{1,3}\.?){4}:(443|80)' | Out-File netstat_parse.txt

Select-String -Path C:\Users\Greg\Desktop\netstat.txt -AllMatches -Pattern '(\d{1,3}\.?){4}:(443|80)' | % {$_.Matches}| % {$_.value}
