import day7_modulefile 

day7_modulefile.errormessage("not warning")



#different method of importing package
from day7_modulefile import errormessage

errormessage("I LOVE YOU", True)

#virtual environment
#python -m venv nameofvnev
#python -m vnev day7
#then ./day7/script/activate.ps1
#if got an error do "Set-ExecutionPolicy RemoteSigned" on ps-admin