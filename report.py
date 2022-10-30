import config

import webbrowser


def saveJob(jobId, title, description):
    f = open(config.fileOutput, "a")
    f.write("# " + title + "\n\n")
    link = "https://www.linkedin.com/jobs/search/?currentJobId=" + jobId
    f.write("[linkedin](" + link + ")\n\n")
    f.write(description + "\n\n")
    f.write("\n\n==================\n\n")
    f.close()
    webbrowser.open(link, new=2)


def saveJobExcludes(jobId, title, description, reason):
    f = open(config.fileFiltered, "a")
    f.write("# " + title + "\n\n")
    f.write(reason + "\n\n")
    f.write("[linkedin](https://www.linkedin.com/jobs/search/?currentJobId=" + jobId + ")\n\n")
    f.write(description + "\n\n")
    f.write("\n\n==================\n\n")
    f.close()
