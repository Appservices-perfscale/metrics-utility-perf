1. Make sure no hosts and inventory exists in controller so automation runs smoothly

2. Change `num_hosts` and play the playbook creating_inventory_hosts_and_variables.yml to create inventories, hosts, and populate variables from json file
3. trigger create_host_facts.py to populate ansible facts as ansible_facts api in controller doesn't support PATCH, PUT, POST, so we have to update directly from db

4. Run the `running_template.yml` file will run the automations.yml playbook in controller. Change the `repeat_count` to run a template in controller multiple times. 

---------
Monitoring: 

5. Create metrics-utility report and make sure the # of automations are all there 

6. Monitor AWX DB to see what is happening and also execute the following
```

```
