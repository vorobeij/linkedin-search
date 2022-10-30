import os
from pathlib import Path

fileOutput = "output/results.md"
fileFiltered = "output/filtered.md"
viewedJobs = 'output/checked.txt'
keywords = "android"
postedDays = 2
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
    "qa"
]
excludedDescriptionKeywords = [
    "React Native",
    "Flutter",
    "ALREADY LIVE IN A EU",
    "AOSP",
    "C++"
]
titleMustContainAnyOf = [
    "android",
    "mobile"
]

Path("output").mkdir(parents=True, exist_ok=True)
