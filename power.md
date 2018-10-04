temp: $env:Path += ";C:\Program Files\GnuWin32\bin"

$oldpath=(Get-ItemProperty -Path ‘Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment’ -Name PATH).path

$newpath = “$oldpath;c:\path\to\folder”

Set-ItemProperty -Path ‘Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment’ -Name PATH -Value $newPath

($env:path).split(“;”)

https://codingbee.net/category/tutorials/powershell
