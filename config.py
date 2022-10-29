import os

fileOutput = "output/results.md"
fileFiltered = "output/filtered.md"
postedDays = 1
countries = [
    "Spain",
    "Cyprus",
    "Netherlands",
    "Germany",
    "Georgia",
    "Canada",
    "Chile"
]
maxYears = 6
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
os.mkdir("output")
