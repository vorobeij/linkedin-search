import re
import langid

import config


def containsVisaSupport(description):
    return True


def experienceRequired(description, maxYears):
    pattern = re.compile('[\\d\\+]* years ')
    matches = pattern.findall(description)  # array of matched strings
    for match in matches:
        try:
            if int(match.split(" ")[0].replace("+", "")) > maxYears:
                return False
        except:
            print(match + " can not be converted to int")
    return True



def containsExcludes(text, excludeKeywords):
    excluded = []
    for exclusion in excludeKeywords:
        if exclusion.casefold() in text.casefold():
            excluded.append(exclusion)
    return excluded


def contains(text, keywords):
    for word in keywords:
        if word.casefold() in text.casefold():
            return True
    return False


def english(text):
    lan = langid.classify(text)
    if lan[0] == "en":
        return True
    return False
