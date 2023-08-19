#!/bin/bash

# script creates a basic Function App and a HTTP-triggered example Function in Python
PROJECT_NAME='MyFctProject'
FUNCTION_NAME='HttpExample'

# create & activate pythone venv
py -m venv .venv
.venv\scripts\activate

Start-Sleep -s 5

# create project
func init $PROJECT_NAME --python
cd $PROJECT_NAME

# create function
func new --name $FUNCTION_NAME --template "HTTP trigger" --authlevel "anonymous"
