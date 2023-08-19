# login: Connect-AzAccount

$GROUP_NAME="fct-rg"
$LOCATION="westeurope"
$STORAGE_NAME="fctsa"
$APP_NAME="fct-app"

"---- create rg ----"
New-AzResourceGroup -Name $GROUP_NAME -Location $LOCATION

"---- create sa ----"
New-AzStorageAccount -ResourceGroupName $GROUP_NAME -Name $STORAGE_NAME -SkuName Standard_LRS -Location $LOCATION

# optional: create premium- ("EP1") or dedicated ("B1") plan
# comment following to create (default) consumption plan
#"---- create plan ----"
#$PLAN_SKU="B1" #"B1"
#$PLAN_NAME="fct-plan"
#New-AzFunctionAppPlan -Name $PLAN_NAME -ResourceGroupName $GROUP_NAME -Location $LOCATION -Sku $PLAN_SKU -WorkerType Linux

#"---- create function app ----"
New-AzFunctionApp -ResourceGroupName $GROUP_NAME -Name $APP_NAME -StorageAccountName $STORAGE_NAME -FunctionsVersion 4 -OSType Linux -RuntimeVersion 3.9 -Runtime python -Location $LOCATION
