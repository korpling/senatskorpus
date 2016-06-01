PEPPER_DIR="../tools/pepper/"
WORKFLOW_FILE=$(echo $PWD)/"convert.pepper"


cd "$PEPPER_DIR"
./pepperStart.sh "$WORKFLOW_FILE"

