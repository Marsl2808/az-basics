import os

from dotenv import load_dotenv

from azure.identity import DefaultAzureCredential
from azure.keyvault.keys import KeyClient, KeyRotationLifetimeAction, KeyRotationPolicyAction, KeyRotationPolicy
from azure.keyvault.keys.crypto import CryptographyClient, EncryptionAlgorithm


load_dotenv()
keyVaultName = os.getenv("KEY_VAULT_NAME")
KVUri = f"https://{keyVaultName}.vault.azure.net"

credential = DefaultAzureCredential()
client = KeyClient(vault_url=KVUri, credential=credential)


# Create an RSA key
key_1 = "my-rsa-key"
rsa_key = client.create_rsa_key(key_1, size=2048)
print(rsa_key.name)
print(rsa_key.key_type)

# Create an elliptic curve key
key_2 = "my-ec-key"
ec_key = client.create_ec_key(key_2, curve="P-256")
print(ec_key.name)
print(ec_key.key_type)

######################
# Read
######################
# single
key = client.get_key(key_1)
print(key.name)

# all
keys = client.list_properties_of_keys()
for key in keys:
    print(key.name)

######################
# Update
######################
# disable key for further use
updated_key = client.update_key_properties(key_2, enabled=False)

print(updated_key.name)
print(updated_key.properties.enabled)

######################
# Delete
######################
deleted_key = client.begin_delete_key(key_2).result()

print(deleted_key.name)
print(deleted_key.deleted_date)

######################
# Set auto rotation
######################
# Set the key's automated rotation policy to rotate the key 30 days before the key expires
actions = [KeyRotationLifetimeAction(KeyRotationPolicyAction.rotate, time_before_expiry="P30D")]
# You may also specify the duration after which the newly rotated key will expire
# In this example, any new key versions will expire after 90 days
policy = KeyRotationPolicy()
updated_policy = client.update_key_rotation_policy(key_1, policy=policy, expires_in="P90D", lifetime_actions=actions)

# You can get the current rotation policy for a key with get_key_rotation_policy
current_policy = client.get_key_rotation_policy(key_1)

# Finally, you can rotate a key on-demand by creating a new version of the key
rotated_key = client.rotate_key(key_1)

######################
# Cryptographic operations
######################
# CryptographyClient enables cryptographic operations (encrypt/decrypt, wrap/unwrap, sign/verify) using a particular key.

key = client.get_key(key_1)
crypto_client = CryptographyClient(key, credential=credential)
plaintext = b"plaintext"

result = crypto_client.encrypt(EncryptionAlgorithm.rsa_oaep, plaintext)
decrypted = crypto_client.decrypt(result.algorithm, result.ciphertext)
