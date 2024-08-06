LOCUST="locust"
LOCUS_OPTS="-f /locust-tasks/locustfile.py"
LOCUS_HOST="-H https://cloud.stage.redhat.com"
LOGIN_LOCUST="galaxy:Galaxy2023"
LOCUST_MODE=${LOCUST_MODE:-standalone}

if [[ "$LOCUST_MODE" = "master" ]]; then
    LOCUS_OPTS="$LOCUS_OPTS --web-auth $LOGIN_LOCUST --master --master-port=5557"

elif [[ "$LOCUST_MODE" = "worker" ]]; then
    LOCUS_OPTS="$LOCUS_OPTS --worker --master-port=5557 --master-host=$LOCUST_MASTER_URL"
fi

echo "$LOCUST $LOCUS_OPTS $LOCUS_HOST"

$LOCUST $LOCUS_OPTS $LOCUS_HOST
