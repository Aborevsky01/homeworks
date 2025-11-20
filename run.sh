set -e

echo "Starting bioinfo-joins container"
echo "================================"
echo ""

if ! command -v docker &> /dev/null; then
    echo "Docker is not installed"
    exit 1
fi

echo "Docker: OK"

if [ ! -f "input/sample_metadata.csv" ] || [ ! -f "input/mass_spec_results.csv" ] || [ ! -f "input/quality_data.csv" ]; then
    echo "Input files not found in input/ directory"
    exit 1
fi

echo "Input files: OK"

if [ ! -d "output" ]; then
    mkdir -p output
    chmod 777 output
fi

echo "Output directory: OK"
echo ""

echo "Building Docker image..."
docker build -t bioinfo-joins . || {
    echo "Build failed"
    exit 1
}

echo "Build: OK"
echo ""

echo "Running container..."
echo "================================"
docker run --rm \
  -v "$(pwd)/input:/data/input:ro" \
  -v "$(pwd)/output:/data/output" \
  bioinfo-joins

echo ""
echo "================================"
echo "Completed"
echo ""
echo "Results in output/:"
ls -lh output/*.csv 2>/dev/null || echo "No output files found"
