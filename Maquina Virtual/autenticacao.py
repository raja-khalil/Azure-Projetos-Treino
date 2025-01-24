from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Credenciais
credential = DefaultAzureCredential()

# ID da assinatura
subscription_id = 'your_subscription_id'

# Cliente de gerenciamento de recursos
resource_client = ResourceManagementClient(credential, subscription_id)
