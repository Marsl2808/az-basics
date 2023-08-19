#!/bin/bash

# make sure to run the script in the fct-project dir
# cd <fct-project>
# ../set-cloud-env.sh

# deploy
func azure functionapp publish fct-app

# view logging in Az-portal
func azure functionapp logstream fct-app --browser