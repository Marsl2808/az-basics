Get-AzSubscription
Set-AzContext -Subscription "Azure for Students"

$ResourceGroup = "storage-service-rg"
$SAName = "saazstorage"
$ContainerName = "my-blob-conatiner"
$BlobName = "SampleSource.txt"

$StorageKey = (Get-AzStorageAccountKey -ResourceGroupName $ResourceGroup -Name $SAName)
$Context = (New-AzStorageContext -StorageAccountName $SAName -StorageAccountKey $StorageKey[0].Value)
$Context

# get reference to container object
$Container = Get-AzStorageContainer -Context $Context

# get reference to blob
$Blob = Get-AzStorageBlob -Blob $BlobName -Container $ContainerName -Context $Context
$Blob

# download file
Get-AzStorageBlobContent -Blob $BlobName -Container $ContainerName -Context $Context -Destination .

# Copy to second container
Set-AzStorageBlobContent -File ./SampleSource.txt -Container $ContainerName"2" -Context $Context -Properties @{"ContentType" = "text/plain"}