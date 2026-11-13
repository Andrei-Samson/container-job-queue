import time

# def execute_job(duration):
#     print("Job started")
#
#     start_time = time.perf_counter()
#
#     time.sleep(duration)
#
#     end_time = time.perf_counter()
#
#     elapsed_time = end_time - start_time
#
#     print("Job completed")
#     print(f"Execution time: {elapsed_time:.5f} seconds")

# job = {
#     "job_id": 1,
#     "duration": 5,
#     "status": "queued"
# }

# job1 = {
#     "id": 1,
#     "duration": 3,
#     "status": "queued"
# }
#
# job2 = {
#     "id": 2,
#     "duration": 7,
#     "status": "queued"
# }

jobs = [
    {
        "id": 1,
        "duration": 2,
        "status": "queued"
    },
    {
        "id": 2,
        "duration": 3,
        "status": "queued"
    },
    {
        "id": 3,
        "duration": 4,
        "status": "queued"
    }
]

def execute_job(jobs):
    jobs["status"] = "running"

    print("Job", jobs["id"], "started.")
    print("Status:", jobs["status"], "\n")

    start_time = time.perf_counter()
    time.sleep(jobs["duration"])

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    jobs["status"] = "completed"

    print("Job", jobs["id"], "completed")
    print("Status:", jobs["status"])
    print(f"Execution time: {elapsed_time:.2f} seconds \n")


if __name__ == '__main__':
    jobs.append({"id": 4, "duration": 3, "status": "queued"})
    for job in jobs:
        execute_job(job)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
