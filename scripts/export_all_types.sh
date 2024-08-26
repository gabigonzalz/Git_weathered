
# Define the city
COUNTRY="Sydney"

# Define the export types
EXPORT_TYPE=("txt" "json" "csv")

# Iterate over each export type and execute the Python script
for TYPE in "${EXPORT_TYPE[@]}"; do
    echo "Ejecutando el script con exportación $TYPE"
    python3 ../git_weathered.py -c "$COUNTRY" -e "$TYPE"
done
