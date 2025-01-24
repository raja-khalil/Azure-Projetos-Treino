resource_group_name = 'myResourceGroup'
location = 'eastus'

resource_client.resource_groups.create_or_update(
    resource_group_name,
    {
        'location': location
    }
)
