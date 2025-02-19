1. Make sure no hosts and inventory exists in controller so automation runs smoothly
2. Change `num_hosts` and play the playbook creating_inventory_hosts_and_variables.yml to create inventories, hosts, and populate variables from json file
3. trigger create_host_facts.py to populate ansible facts as ansible_facts api in controller doesn't support PATCH, PUT, POST, so we have to update directly from db
4. Trigger hello_world.yml. First you need to edit the `task_count` to create random tasks in each hosts. This is because we need to trigger more than 1 automation in the host to see performance changes
5. Create metrics-utility report and make sure the # of automations are all there 
6. Monitor AWX DB to see what is happening
