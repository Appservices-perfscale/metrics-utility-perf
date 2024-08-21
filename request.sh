python delete_bulk.py
python adding_bulk.py

max=10
for i in `seq 2 $max`
do

rm -rf /awx_devel/awx-dev/metrics-utility/shipped_data/billing/reports/*
export METRICS_UTILITY_SHIP_TARGET=controller_db
export METRICS_UTILITY_REPORT_TYPE=RENEWAL_GUIDANCE
export METRICS_UTILITY_SHIP_PATH=/awx_devel/awx-dev/metrics-utility/shipped_data/billing
export METRICS_UTILITY_REPORT_TYPE=RENEWAL_GUIDANCE
export METRICS_UTILITY_SHIP_PATH=/awx_devel/awx-dev/metrics-utility/shipped_data/billing # Builds report covering 365days back by default

metrics-utility build_report --since=12months --ephemeral=1month

done