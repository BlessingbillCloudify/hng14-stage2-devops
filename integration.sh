#!/bin/bash
set -e

echo "Starting Integration Test..."

# 1. Submit a job to the Node.js frontend
RESPONSE=$(curl -s -X POST http://localhost:3000/submit)
JOB_ID=$(echo $RESPONSE | jq -r '.job_id')

if [ "$JOB_ID" == "null" ] || [ -z "$JOB_ID" ]; then
  echo "Failed to get Job ID"
  exit 1
fi

echo "Job ID: $JOB_ID submitted successfully."

# 2. Poll for completion
MAX_RETRIES=10
COUNT=0

while [ $COUNT -lt $MAX_RETRIES ]; do
  STATUS=$(curl -s http://localhost:3000/status/$JOB_ID | jq -r '.status')
  echo "Current Status: $STATUS"
  
  if [ "$STATUS" == "completed" ]; then
    echo "Integration Test Passed!"
    exit 0
  fi
  
  sleep 5
  COUNT=$((COUNT+1))
done

echo "Test timed out!"
exit 1
