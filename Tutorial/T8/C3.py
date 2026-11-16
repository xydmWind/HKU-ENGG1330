def sort_jobs(jobs: list) -> None:
    for i in range(1, len(jobs)):
        key = jobs[i]
        j = i - 1
        while j >= 0 and jobs[j][1] > key[1]:
            jobs[j + 1] = jobs[j]
            j -= 1
        jobs[j + 1] = key


n = int(input())
jobs = []
for i in range(n):
    job_id, minutes = input().split()
    jobs.append((job_id, int(minutes)))
observer = jobs
result = sort_jobs(jobs)
print(jobs)
print(observer)
print(result)