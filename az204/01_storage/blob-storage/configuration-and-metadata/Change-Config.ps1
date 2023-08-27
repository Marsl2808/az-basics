Get-AzSubscription
Set-AzContext -Subscription "Azure for Students"

$ResourceGroup = "storage-service-rg"
$SAName = "saazstorage"
$ContainerName = "my-blob-conatiner"
$BlobName = "SampleSource.txt"

$StorageKey = (Get-AzStorageAccountKey -ResourceGroupName $ResourceGroup -Name $SAName)
$Context = (New-AzStorageContext -StorageAccountName $SAName -StorageAccountKey $StorageKey[0].Value)

# get reference to container object
$Container = Get-AzStorageContainer -Context $Context

# get reference to blob
$Blob = Get-AzStorageBlob -Blob $BlobName -Container $ContainerName -Context $Context
# get information of blob
$Blob.BlobClient.GetProperties().value

# add key-value pair as custom Metadata to Blob
$Metadata = New-Object System.Collections.Generic.Dictionary"[String, String]"
$Metadata.Add("customKey", "customValue")
$Metadata.Add("customKey2", "customValue2")
$Blob.BlobClient.SetMetadata($Metadata, $null)
# test
$Blob.BlobClient.GetProperties().value.Metadata
