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

How to make it run using local dev environment with containers and gateway:

1) creating_inventory_hosts_and_variables.yml    needs another variable named 'path_prefix' that should be set to: controller

Example:
ansible-playbook creating_inventory_hosts_and_variables.yml   --extra-vars "controller_url=https://localhost:8030 controller_username=admin controller_password=admin organization_id=1 credential_id=1 path_prefix=controller"


it is because, localhost:8030 points to the gateway and the gateway uses prefix controller, thus /api/v2 that controller uses must be /api/controller/v2 for gateway urls

2) running create_host_facts.py

This one needs to gather information about DB connection.

docker ps

you will see the result for db container:

669953676e5a   quay.io/sclorg/postgresql-15-c9s              "container-entrypoin…"   22 hours ago   Up 4 hours   0.0.0.0:5441->5432/tcp, [::]:5441->5432/tcp                                                                                                                                                                                                                 tools_postgres_1

it is mapping from port 5432 (standard postgres port visible inside container) to 5441 - this port is visible outside of container

you then need to obtain db password:
docker exec -it tools_postgres_1 printenv

search for:
POSTGRESQL_PASSWORD

finally you can run command:
python3 create_host_facts.py --user=awx --password={pswd from printenv} --host="localhost" --port=5441

3) Running the job templates

- Create a project from source in this repo
- Create job template from this project and select automation.yml file, select whatever inventory you want
- select Prompt on Launch for Inventory - because the standard inventory you set for the job template must be overriden

4) Run the playbook:

ansible-playbook running_template.yml --extra-vars 'controller_url=https://localhost:8043 controller_username=admin controller_password={pswd from printenv just as before}'

you can also validate the url of controller using:

docker ps and search for tools_awx_1



