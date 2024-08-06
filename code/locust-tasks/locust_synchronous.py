import subprocess
import time
import os
import uuid
import random
import re
import string
from pathlib import Path
from requests.auth import HTTPBasicAuth

from locust import HttpUser, between, TaskSet, task, events


# This class will be executed when you fire up locust
class AnalyticsUser(HttpUser):
    wait_time = between(0, 0)

    # self.client = GalaxyClient()

    def on_start(self):
        self.client.verify = False
        self.client.trust_env = True
        self.client.proxies = {'https': 'http://squid.corp.redhat.com:3128',
                               'http': "http://squid.corp.redhat.com:3128"}
        self.client.headers = {'Accept': 'application/json'}


    @task
    def execute_job_explorer_options(self):


        self.client.get("/api/tower-analytics/v1/job_explorer_options/",
                        auth=('aa-qe-perf', 'redhatqe'), name="job_explorer_options")

    @task
    def execute_job_explorer2(self):
        post_vars = {
            "attributes": [
                "id",
                "status",
                "job_type",
                "started",
                "finished",
                "elapsed",
                "created",
                "cluster_name",
                "org_name",
                "most_failed_tasks",
                "host_count",
                "host_task_count",
                "failed_host_count",
                "unreachable_host_count",
                "changed_host_count",
                "ok_host_count",
                "skipped_host_count",
            ],
            "status": ["successful", "failed"],
            "quick_date_range": "last_30_days",
            "job_type": ["workflowjob", "job"],
            "org_id": [],
            "cluster_id": [],
            "template_id": [],
            "inventory_id": [],
            "sort_options": "created",
            "sort_order": "desc",
            "only_root_workflows_and_standalone_jobs": False,
            "limit": "5",
            "offset": "0"
        }

        self.client.post("/api/tower-analytics/v1/job_explorer/?limit=25&offset=0&sort_by=created%3Adesc", json=post_vars,
                        auth=('aa-qe-perf', 'redhatqe'), name="First")

    @task
    def execute_event_explorer2(self):

        post_vars = {
            "cluster_id": [],
            "org_id": [],
            "template_id": [],
            "quick_date_range": "last_30_days",
            "group_by": "module",
            "sort_options": "host_task_count",
            "sort_oder": "desc",
            "limit": 10
        }

        self.client.post("/api/tower-analytics/v1/event_explorer/?limit=25", json=post_vars,
                        auth=('aa-qe-perf', 'redhatqe'), name="Second")

    @task
    def execute_job_event_explorer3(self):
        post_vars = {
            "cluster_id": [],
            "org_id": [],
            "template_id": [],
            "quick_date_range": "last_30_days",
            "group_by": "template",
            "limit": 10,
            "job_type": ["job"],
            "group_by_time": False,
            "status": ["successful", "failed"]
        }

        self.client.post("/api/tower-analytics/v1/event_explorer/?limit=25", json=post_vars,
                        auth=('aa-qe-perf', 'redhatqe'), name="Third")

    @task
    def execute_adoption_rate4(self):
        post_vars = {
            "cluster_id": [],
            "org_id": [],
            "template_id": [],
            "quick_date_range": "last_30_days",
            "group_by": "template",
            "limit": 10,
            "job_type": ["workflowjob"],
            "group_by_time": False,
            "status": ["successful", "failed"]
        }

        self.client.post(
            "/api/tower-analytics/v1/event_explorer/?limit=25", json=post_vars,
            auth=('aa-qe-perf', 'redhatqe'), name="Fourth")

    @task
    def execute_job_explorer5(self):
        post_vars = {
            "limit": 6,
            "offset": 0,
            "attributes": [
                "total_count",
                "successful_count",
                "failed_count",
                "average_host_task_count_per_host",
                "average_host_task_ok_count_per_host",
                "average_host_task_failed_count_per_host",
                "average_host_task_unreachable_count_per_host",
                "average_host_task_skipped_count_per_host",
                "successful_count",
                "failed_count",
                "error_count",
                "started",
                "finished",
                "elapsed",
                "created",
                "total_cluster_count",
                "total_org_count",
                "most_failed_tasks",
                "host_count",
                "host_task_count",
                "host_task_changed_count",
                "host_task_failed_count",
                "host_task_ok_count",
                "host_task_skipped_count",
                "host_task_unreachable_count",
                "failed_host_count",
                "unreachable_host_count",
                "changed_host_count",
                "ok_host_count",
                "skipped_host_count",
                "total_count"
            ],
            "group_by": "template",
            "group_by_time": False,
            "granularity": "monthly",
            "quick_date_range": "last_6_months",
            "sort_options": "total_count",
            "sort_order": "desc",
            "cluster_id": [],
            "inventory_id": [],
            "job_type": [],
            "org_id": [],
            "status": [],
            "template_id": []
        }

        self.client.post(
            "/api/tower-analytics/v1/job_explorer/?limit=25&offset=0&sort_by=total_count%3Adesc",
            json=post_vars,
            auth=('aa-qe-perf', 'redhatqe'), name="Fifth")
    #

    @task
    def execute_adoption_rate(self):
        post_vars = {
            "limit": 6,
            "offset": 0,
            "cluster_id": [],
            "org_id": [],
            "inventory_id": [],
            "template_id": [],
            "status": [],
            "sort_options": "total_templates_per_org",
            "sort_order": "desc",
            "adoption_rate_type": "elapsed_of_templates_by_org",
            "percentile": "above_0",
            "granularity": "monthly",
            "quick_date_range": "last_3_months",
            "chart_type": "scatter"
        }

        self.client.post("/api/tower-analytics/v1/adoption_rate/?limit=25&offset=0&sort_by=total_templates_per_org%3Adesc",
                         json=post_vars,
                        auth=('aa-qe-perf', 'redhatqe'),  name="six")

    @task
    def execute_probe_template(self):
        post_vars = {
            "limit": 6,
            "offset": 0,
            "attributes": [
                "average_duration_per_task",
                "host_count",
                "slow_hosts_count"
            ],
            "group_by": "template",
            "cluster_id": [],
            "org_id": [],
            "inventory_id": [],
            "template_id": [],
            "status": [],
            "host_status": [],
            "sort_options": "average_duration_per_task",
            "sort_order": "desc",
            "quick_date_range": "slow_hosts_last_month",
            "slow_host_view": "templates_with_slow_hosts",
            "chart_type": "bar"
        }

        self.client.post("/api/tower-analytics/v1/probe_templates/?limit=25&offset=0&sort_by=average_duration_per_task%3Adesc",
                         json=post_vars, auth=('aa-qe-perf', 'redhatqe'),  name="seven")
    #
    @task
    def execute_event_explorer4(self):
        post_vars = {
            "limit": 6,
            "offset": 0,
            "attributes": [
                "host_task_count",
                "total_org_count",
                "total_template_count",
                "total_count",
                "host_task_changed_count",
                "host_task_failed_count",
                "host_task_ok_count",
                "host_task_skipped_count",
                "host_task_unreachable_count"
            ],
            "group_by": "module",
            "group_by_time": True,
            "granularity": "monthly",
            "quick_date_range": "last_6_months",
            "sort_options": "host_task_count",
            "sort_order": "desc",
            "cluster_id": [],
            "inventory_id": [],
            "job_type": [],
            "org_id": [],
            "status": [],
            "task_action_id": [],
            "template_id": []
        }


        self.client.post("/api/tower-analytics/v1/event_explorer/?limit=25&offset=0&sort_by=host_task_count%3Adesc",
                         json=post_vars, auth=('aa-qe-perf', 'redhatqe'),  name="eight")

    @task
    def execute_event_explorer_task(self):
        post_vars = {
            "limit": 6,
            "offset": 0,
            "attributes": [
                "host_task_count",
                "host_task_changed_count",
                "host_task_ok_count",
                "host_task_failed_count",
                "host_task_unreachable_count",
                "total_count"
            ],
            "group_by": "task",
            "group_by_time": True,
            "granularity": "monthly",
            "quick_date_range": "last_6_months",
            "sort_options": "host_task_count",
            "sort_order": "desc",
            "cluster_id": [],
            "inventory_id": [],
            "job_type": [],
            "org_id": [],
            "status": [],
            "task_action_id": [],
            "template_id": []
        }

        self.client.post("/api/tower-analytics/v1/event_explorer/?limit=25&offset=0&sort_by=host_task_count%3Adesc",
                         json=post_vars, auth=('aa-qe-perf', 'redhatqe'),  name="Nine")

    @task
    def execute_event_org(self):
        post_vars = {
            "limit": 6,
            "offset": 0,
            "attributes": [
                "host_task_count",
                "host_task_changed_count",
                "host_task_ok_count",
                "host_task_failed_count",
                "host_task_unreachable_count",
                "total_count"
            ],
            "group_by": "org",
            "group_by_time": True,
            "granularity": "monthly",
            "quick_date_range": "last_6_months",
            "sort_options": "host_task_count",
            "sort_order": "desc",
            "cluster_id": [],
            "inventory_id": [],
            "job_type": [],
            "org_id": [],
            "status": [],
            "task_action_id": [],
            "template_id": []
        }

        self.client.post("/api/tower-analytics/v1/event_explorer/?limit=25&offset=0&sort_by=host_task_count%3Adesc",
                         json=post_vars, auth=('aa-qe-perf', 'redhatqe'),  name="Ten")
    #
    @task
    def execute_event_template(self):
        post_vars = {
            "limit": 6,
            "offset": 0,
            "attributes": [
                "host_task_count",
                "host_task_changed_count",
                "host_task_ok_count",
                "host_task_failed_count",
                "host_task_unreachable_count",
                "total_count"
            ],
            "group_by": "template",
            "group_by_time": True,
            "granularity": "monthly",
            "quick_date_range": "last_6_months",
            "sort_options": "host_task_count",
            "sort_order": "desc",
            "cluster_id": [],
            "inventory_id": [],
            "job_type": [],
            "org_id": [],
            "status": [],
            "task_action_id": [],
            "template_id": []
        }

        self.client.post("/api/tower-analytics/v1/event_explorer/?limit=25&offset=0&sort_by=host_task_count%3Adesc",
                         json=post_vars, auth=('aa-qe-perf', 'redhatqe'), name="Eleven")



    @task
    def execute_job_explorer3(self):
        post_vars = {
            "limit": 6,
            "offset": 0,
            "granularity": "daily",
            "quick_date_range": "last_30_days",
            "status": [],
            "org_id": [],
            "job_type": [],
            "cluster_id": [],
            "template_id": [],
            "inventory_id": [],
            "attributes": [
                "total_count",
                "host_task_count"
            ],
            "group_by": "org",
            "group_by_time": True,
            "sort_options": "total_count",
            "sort_order": "desc"
        }

        self.client.post("/api/tower-analytics/v1/job_explorer/?limit=6&offset=0&sort_by=total_count%3Adesc",
                         json=post_vars,
                        auth=('aa-qe-perf', 'redhatqe'), name="twelve")

    @task
    def execute_job_explorer4(self):
        post_vars = {
            "limit": 6,
            "offset": 0,
            "attributes": [
                "failed_count",
                "successful_count",
                "total_count"
            ],
            "group_by": "template",
            "group_by_time": True,
            "granularity": "monthly",
            "quick_date_range": "last_6_months",
            "sort_options": "total_count",
            "sort_order": "desc",
            "cluster_id": [],
            "inventory_id": [],
            "job_type": [],
            "org_id": [],
            "status": [],
            "template_id": []
        }

        self.client.post("/api/tower-analytics/v1/job_explorer/?limit=25&offset=0&sort_by=total_count%3Adesc",
                         json=post_vars,
                         auth=('aa-qe-perf', 'redhatqe'), name="Thirteen")
    #
    @task
    def execute_host_explorer2(self):
        post_vars = {
            "limit": 6,
            "offset": 0,
            "attributes": [
                "total_unique_host_count",
                "total_unique_host_changed_count"
            ],
            "group_by": "template",
            "group_by_time": True,
            "granularity": "monthly",
            "quick_date_range": "last_6_months",
            "sort_options": "total_unique_host_count",
            "sort_order": "desc",
            "cluster_id": [],
            "inventory_id": [],
            "job_type": [],
            "org_id": [],
            "status": [],
            "template_id": []
        }

        self.client.post("/api/tower-analytics/v1/host_explorer/?limit=25&offset=0&sort_by=total_unique_host_count%3Adesc",
                         json=post_vars, auth=('aa-qe-perf', 'redhatqe'), name="Fourteen")

    @task
    def execute_host_explorer(self):
        post_vars = {
            "limit": 6,
            "offset": 0,
            "granularity": "daily",
            "quick_date_range": "last_30_days",
            "status": [],
            "org_id": [],
            "job_type": [],
            "cluster_id": [],
            "template_id": [],
            "inventory_id": [],
            "attributes": [
                "total_unique_host_count",
                "total_unique_host_changed_count"
            ],
            "group_by": "org",
            "group_by_time": True,
            "sort_options": "total_unique_host_count",
            "sort_order": "desc"
        }

        self.client.post("/api/tower-analytics/v1/host_explorer/?limit=25&offset=0&sort_by=total_unique_host_count%3Adesc",
                         json=post_vars,
                        auth=('aa-qe-perf', 'redhatqe'), name="Fiveteen")

    @task
    def execute_probe_template2(self):
        post_vars = {
            "limit": 6,
            "offset": 0,
            "attributes": [
                "average_duration_per_task",
                "host_count",
                "slow_hosts_count"
            ],
            "group_by": "template",
            "cluster_id": [],
            "org_id": [],
            "inventory_id": [],
            "template_id": [],
            "status": [],
            "host_status": [],
            "sort_options": "average_duration_per_task",
            "sort_order": "desc",
            "quick_date_range": "slow_hosts_last_month",
            "slow_host_view": "templates_with_slow_hosts",
            "chart_type": "bar"
        }

        self.client.post("/api/tower-analytics/v1/probe_templates/?limit=25&offset=0&sort_by=average_duration_per_task%3Adesc",
                         json=post_vars,
                         auth=('aa-qe-perf', 'redhatqe'), name="Sixteen")


    @task
    def execute_job_explorer6(self):
        post_vars = {
            "limit": 6,
            "offset": 0,
            "attributes": [
                "host_count",
                "changed_host_count",
                "host_task_count",
                "host_task_changed_count"
            ],
            "group_by": "template",
            "group_by_time": True,
            "granularity": "monthly",
            "quick_date_range": "last_6_months",
            "sort_options": "changed_host_count",
            "sort_order": "desc",
            "cluster_id": [],
            "inventory_id": [],
            "job_type": [],
            "org_id": [],
            "status": [],
            "template_id": []
        }

        self.client.post("/api/tower-analytics/v1/job_explorer/?limit=25&offset=0&sort_by=changed_host_count%3Adesc",
                         json=post_vars,
                        auth=('aa-qe-perf', 'redhatqe'), name="Seventeen")

    #
    @task
    def execute_roi_template(self):
        post_vars = {
            "status": [
                "successful"
            ],
            "org_id": [],
            "cluster_id": [],
            "template_id": [],
            "inventory_id": [],
            "quick_date_range": "roi_last_year",
            "job_type": [
                "job"
            ],
            "sort_options": "successful_hosts_savings",
            "sort_order": "desc",
            "limit": "6",
            "offset": "0",
            "only_root_workflows_and_standalone_jobs": True,
            "attributes": [
                "elapsed",
                "host_count",
                "total_count",
                "total_org_count",
                "total_cluster_count",
                "successful_hosts_total",
                "successful_elapsed_total"
            ],
            "group_by": "template",
            "group_by_time": False
        }

        self.client.post(
            "/api/tower-analytics/v1/roi_templates/?limit=25&offset=0&sort_by=successful_hosts_savings%3Adesc",
            json=post_vars,  auth=('aa-qe-perf', 'redhatqe'), name="Eighteen")
    # # #
    @task
    def execute_event_explorer7(self):

        post_vars = {
            "limit": 6,
            "offset": 0,
            "attributes": [
                "host_task_count"
            ],
            "group_by": "template",
            "group_by_time": True,
            "granularity": "monthly",
            "quick_date_range": "last_6_months",
            "sort_options": "host_task_count",
            "sort_order": "desc",
            "cluster_id": [],
            "inventory_id": [],
            "job_type": [],
            "org_id": [],
            "status": [],
            "task_id": [],
            "task_action_name": [
                "apt",
                "apt_key",
                "apt_repository",
                "assemble",
                "blockinfile",
                "copy",
                "cron",
                "csvfile",
                "debconf",
                "dnf",
                "dpkg_selections",
                "env",
                "fetch",
                "file",
                "fileglob",
                "find",
                "first_found",
                "gather_facts",
                "get_url",
                "getent",
                "git",
                "hostname",
                "include_vars",
                "ini",
                "iptables",
                "junit",
                "known_hosts",
                "lineinfile",
                "local",
                "package",
                "password",
                "pip",
                "replace",
                "rpm_key",
                "script",
                "service",
                "service_facts",
                "setup",
                "slurp",
                "stat",
                "subversion",
                "systemd",
                "sysvinit",
                "tempfile",
                "template",
                "tree",
                "unarchive",
                "unvault",
                "user",
                "yum",
                "yum_repository"
            ],
            "task_action_id": [],
            "template_id": []
        }

        self.client.post(
            "/api/tower-analytics/v1/event_explorer/?limit=25&offset=0&sort_by=host_task_count%3Adesc",
            json=post_vars,
            auth=('aa-qe-perf', 'redhatqe'), name="Nineteen")







