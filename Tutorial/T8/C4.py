def rank_jobs(jobs: list, minimum: int) -> list:
    tmp_jobs = []
    for i in range(len(jobs)):
        if jobs[i][2] >= minimum:
            tmp_jobs.append(jobs[i])
    return sorted(tmp_jobs, key = lambda job: (job[1], job[2]))


n = int(input())
jobs = []
for i in range(n):
    job_id, priority, minutes = input().split()
    jobs.append((job_id, int(priority), int(minutes)))
minimum = int(input())
print(rank_jobs(jobs, minimum))
print(jobs)