async_vm_creation = compute_client.virtual_machines.begin_create_or_update(
    resource_group_name,
    vm_name,
    vm_parameters
)
vm = async_vm_creation.result()
print(f'VM {vm.name} criada com sucesso')
