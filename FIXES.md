FILE NAME:api/.env
LINE: 1-2
WHAT WAS BROKEN: REDIS_PASSWORD was hardcoded in a tracked file, posing a security vunerability.
HOW I FIXED: Added .env to .gitignore, and created a .env.example with placeholder values, and set the app to load values from the environment.
  
FILE NAME:api/main.py
LINE: 19
WHAT WAS BROKEN: Hardcoded Connection: The Redis host was set to localhost, which prevents containers from talking to each other.
HOW I FIX: Replaced localhost with os.getenv("REDIS_HOST", "redis") so the app can find the Redis service in a Docker network.

FILE NAME:api/main.py
LINE: 21
WHAT WAS BROKEN:Security Vulnerability: The Redis connection was missing a password, even though one is required by the production configuration
HOW I FIX:password=os.getenv("REDIS_PASSWORD") to pull the secret key safely from the environment variables.

FILE NAME:api/main.py
LINE: 22
WHAT WAS BROKEN:Data Inconsistency: By default, Redis returns data as "bytes" (e.g., b'queued'), which can cause the app to crash or display weird text.
HOW I FIX:Added decode_responses=True to the Redis client to automatically translate responses into clean, human-readable text.

FILE NAME:api/main.py
LINE: 27
WHAT WAS BROKEN: The code tries to .decode() a response that is already decoded by the Redis client.
HOW I FIXED: Removed the .decode() method from the get_job return statement.

FILE NAME: api/requirements.txt
LINE: 4
WHAT WAS BROKEN: Missing python-dotenv for loading secrets.
HOW I FIX: Added python-dotenv to the requirements list.

FILE NAME: frontend/app.js
LINE: 6
WHAT WAS BROKEN: The API_URL was hardcoded to localhost:8000, which prevents the container from communicating with the API service in a Docker network.
HOW I FIX: Changed API_URL to http://api:8000 to use the Docker service name for internal networking.


FILE NAME: frontend/app.js
LINE: 16,26
WHAT WAS BROKEN: Catch blocks were silent, returning a generic error to the user without logging the actual failure for developer
HOW I FIX: Added console.error(err.message) to both the /submit and /status routes to ensure connection issues are visible in the container logs.

FILE NAME:api/main.py
LINE: 2, 9-15
WHAT WAS BROKEN: Cross-Origin Resource Sharing (CORS) was not configured.
HOW I FIX: Added CORSMiddleware to allow the Frontend to communicate with the API from a different port/origin.

FILE NAME:frontend/package.json
LINE: 11
WHAT WAS BROKEN: Missing dotenv dependency.
HOW I FIX: Added dotenv to the dependencies list to support environment variable management.

FILE NAME: worker/requirements.txt
LINE: 2
WHAT WAS BROKEN: 	Missing python-dotenv dependency.
HOW I FIX: Added python-dotenv to ensure the worker can load the REDIS_PASSWORD from environment variables.

FILE NAME:worker/main.py
LINE:7,9
WHAT WAS BROKEN:Redis host is hardcoded to localhost and is missing a password.
HOW I FIX:Changed host to os.getenv("REDIS_HOST", "redis") and added REDIS_PASSWORD support.

FILE NAME:worker/main.py
LINE:10
WHAT WAS BROKEN:Data returned from Redis is in bytes format.
HOW I FIX:Added decode_responses=True to the Redis client for automatic string conversion.

FILE NAME:worker/main.py
LINE:25
WHAT WAS BROKEN:Manually decoding job_id can lead to errors if the connection settings change.
HOW I FIX:Removed manual .decode() since the client now handles it automatically.

FILE NAME:worker/main.py
LINE: 19
WHAT WAS BROKEN:	Lack of Visibility: The worker started silently, making it impossible to verify if the service was active in container logs.
HOW I FIX:Added a startup print statement to provide immediate feedback when the service is ready to process jobs.

FILE NAME:api/main.py
LINE:
WHAT WAS BROKEN:Missing health check endpoint required for Docker orchestration and monitoring
HOW I FIX:Added a /health GET endpoint to allow the Docker HEALTHCHECK instruction to verify the service status.

FILE NAME:frontend/package.json
LINE: 7
WHAT WAS BROKEN:Missing a lint script, preventing the CI/CD pipeline from running automated code quality checks.
HOW I FIX:Added "lint": "eslint ." to the scripts section and installed eslint to support the linting stage of the pipeline.

