# make sure to run the script in the fct-project dir
# cd <fct-project>
# ../Set-CloudEnv.ps1

# deploy
func azure functionapp publish fct-app

# view logging in Az-portal
func azure functionapp logstream fct-app --browser