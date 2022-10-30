from linkedin_api import Linkedin

import config
from search import authConfig, search

if __name__ == '__main__':
    # f = open(config.fileFiltered, "w")
    # f.write("")
    # f.close()
    # f = open(config.fileOutput, "w")
    # f.write("")
    # f.close()

    api = Linkedin(authConfig.get("email").data, authConfig.get("password").data)
    for country in config.countries:
        search(api, country)
