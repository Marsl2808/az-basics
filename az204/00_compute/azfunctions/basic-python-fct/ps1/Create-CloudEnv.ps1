# login: Connect-AzAccount

$GROUP_NAME="fct-rg"
$LOCATION="westeurope"
$STORAGE_NAME="fctsa"
$APP_NAME="fct-app"

"---- create rg ----"
New-AzResourceGroup -Name $GROUP_NAME -Location $LOCATION

"---- create sa ----"
New-AzStorageAccount -ResourceGroupName $GROUP_NAME -Name $STORAGE_NAME -SkuName Standard_LRS -Location $LOCATION

"---- create function app ----"
New-AzFunctionApp -ResourceGroupName $GROUP_NAME -Name $APP_NAME -StorageAccountName $STORAGE_NAME -FunctionsVersion 4 -OSType linux -RuntimeVersion 3.9 -Runtime python -Location $LOCATION
