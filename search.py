from jproperties import Properties

import config
import validation
from report import saveJobExcludes, saveJob

authConfig = Properties()
with open('auth.properties', 'rb') as config_file:
    authConfig.load(config_file)


def search(api, country):
    print("search " + country + "\n")
    jobs = api.search_jobs(
        keywords=config.keywords,
        # experience="4",
        # job_type="F",
        location_name=country,
        listed_at=config.postedDays * 86400,
        limit=100
    )

    print(jobs)
    for job in jobs:
        jobId = job["dashEntityUrn"].replace("urn:li:fsd_jobPosting:", "")
        title = job["title"]

        excludes = validation.containsExcludes(title, config.excludedTitleKeywords)
        if len(excludes) > 0:
            saveJobExcludes(jobId, title, "", "Title contains excludes: " + " ".join(excludes))
            continue
        if not validation.contains(title, config.titleMustContainAnyOf):
            saveJobExcludes(jobId, title, "", "Title does not contain keywords: ")
            continue

        print(jobId + " " + title)

        jobDescription = api.get_job(jobId)
        text = jobDescription["description"]["text"]

        if not validation.english(text):
            saveJobExcludes(jobId, title, text, "Not english")
            continue
        if not validation.containsVisaSupport(text):
            saveJobExcludes(jobId, title, text, "No visa support")
            continue
        if not validation.experienceRequired(text, config.myExperienceIsLessThan):
            saveJobExcludes(jobId, title, text, "Min experience")
            continue
        excludes = validation.containsExcludes(text, config.excludedDescriptionKeywords)
        if len(excludes) > 0:
            saveJobExcludes(jobId, title, text, "Contains excluded keywords " + " ".join(excludes))
            continue

        saveJob(jobId, title, text)
