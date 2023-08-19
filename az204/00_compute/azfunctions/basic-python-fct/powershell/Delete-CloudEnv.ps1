$GROUP_NAME='fct-rg'
$PLAN_NAME="fct-plan"

#Remove-AzAppServicePlan -Name $PLAN_NAME -ResourceGroupName $GROUP_NAME

#az group delete --name $GROUP_NAME -y
Remove-AzResourceGroup -Name $GROUP_NAME
