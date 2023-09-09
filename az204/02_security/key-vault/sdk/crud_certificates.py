import os

from dotenv import load_dotenv

from azure.identity import DefaultAzureCredential
from azure.keyvault.certificates import CertificateClient, CertificatePolicy

load_dotenv()
keyVaultName = os.getenv("KEY_VAULT_NAME")
KVUri = f"https://{keyVaultName}.vault.azure.net"

credential = DefaultAzureCredential()
certificate_client = CertificateClient(vault_url=KVUri, credential=credential)


# CREATE
create_certificate_poller = certificate_client.begin_create_certificate(
    certificate_name="cert-name", policy=CertificatePolicy.get_default()
)
print(create_certificate_poller.result())


# READ
certificate = certificate_client.get_certificate("cert-name")

print(certificate.name)
print(certificate.properties.version)
print(certificate.policy.issuer_name)

certificate = certificate_client.get_certificate_version(certificate_name="cert-name", version="cert-version")

print(certificate.name)
print(certificate.properties.version)

# list Properties
certificates = certificate_client.list_properties_of_certificates()

for certificate in certificates:
    print(certificate.name)


# UPDATE
# we will now disable the certificate for further use
updated_certificate= certificate_client.update_certificate_properties(
    certificate_name="cert-name", enabled=False
)

print(updated_certificate.name)
print(updated_certificate.properties.enabled)


# DELETE
deleted_certificate_poller = certificate_client.begin_delete_certificate("cert-name")

deleted_certificate = deleted_certificate_poller.result()
print(deleted_certificate.name)
print(deleted_certificate.deleted_on)

