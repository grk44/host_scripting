#Greg Kessel
#Lab Pipelining

$sites=@('www.google.com', 'unixs.cis.pitt.edu', 'www.pitt.edu', 'www.upb.pitt.edu','www.pittbradford.org', 'zonnon.univ.pitt.edu')

$sites |ForEach-Object -Process {$_} | Test-NetConnection -CommonTCPPort HTTP | Sort-Object -Property pingsucceeded | ConvertTo-Html | Out-File 'G:\UPB Docs\CIST 1342 Host scripting\nettest.htm'

