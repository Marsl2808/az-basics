# script creates a basic Function App and a HTTP-triggered example function in Python
$PojectName='MyFctProject'
$FunctionName='HttpExample'

# create & activate pythone venv
py -m venv .venv
.venv\scripts\activate

Start-Sleep -s 5

# create project
func init $PojectName --python
cd $PojectName

# create function
func new --name $FunctionName --template "HTTP trigger" --authlevel "anonymous"
