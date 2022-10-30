import os
from pathlib import Path

fileOutput = "output/results.md"
fileFiltered = "output/filtered.md"
viewedJobs = 'output/checked.txt'
keywords = "android"
postedDays = 2
limit = -1
countries = [
    "Spain",
    "Cyprus",
    "Netherlands",
    "Germany",
    "Georgia",
    "Canada",
    "Chile"
]
myExperienceIsLessThan = 6
excludedTitleKeywords = [
    "React Native",
    "Flutter",
    "Data Engineer",
    "Python",
    "Security",
    "test",
    "Designer",
    "backend",
    "qa"
]
excludedDescriptionKeywords = [
    "React Native",
    "Flutter",
    "ALREADY LIVE IN A EU",
    "AOSP",
    "C++",
    "not sponsor"
]
titleMustContainAnyOf = [
    "android",
    "mobile"
]

Path("output").mkdir(parents=True, exist_ok=True)
