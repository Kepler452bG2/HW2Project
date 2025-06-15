import requests
from backend.tasks.celery_app import celery_app

@celery_app.task
def fetch_and_save():
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=10)
        response.raise_for_status()
        data = response.json()
        fact = data.get("fact", "No fact found.")

        with open("/tmp/output.txt", "a") as f:
            f.write(fact + "\n")

        print("Fact saved:", fact)

    except Exception as e:
        print("Error fetching fact:", str(e))
