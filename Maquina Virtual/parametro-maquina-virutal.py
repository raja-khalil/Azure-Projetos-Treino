from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import HardwareProfile, StorageProfile, OSProfile, NetworkProfile, VirtualMachine

compute_client = ComputeManagementClient(credential, subscription_id)

vm_name = 'myVM'
vm_parameters = {
    'location': location,
    'hardware_profile': {
        'vm_size': 'Standard_DS1_v2'
    },
    'storage_profile': {
        'image_reference': {
            'publisher': 'Canonical',
            'offer': 'UbuntuServer',
            'sku': '18.04-LTS',
            'version': 'latest'
        }
    },
    'os_profile': {
        'computer_name': vm_name,
        'admin_username': 'azureuser',
        'admin_password': 'P@ssw0rd1234'
    },
    'network_profile': {
        'network_interfaces': [{
            'id': '/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkInterfaces/{nic_name}',
        }]
    }
}

