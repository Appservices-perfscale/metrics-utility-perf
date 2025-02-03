1. Play the playbook creating_inventory_hosts_and_variables.yml to create inventories, hosts, and populate variables from json file
2. trigger creating_host_facts.py to populate ansible facts as ansible_facts api in controller doesn't support PATCH, PUT, POST, so we have to update directly from db
