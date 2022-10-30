# Linkedin job postings scraper

- Looks for all job postings through the countries you are interested in
- Filters out postings with irrelevant description and titles (see `ignoreIfTitleContains`
  and `ignoreIfDescriptionContains`)
- Opens in browser all relevant job postings
- Does not show viewed postings

## Setup

1. Create file `auth.properties`

```properties
email=myemail@gmail.com
password=MYStrongPasswordFromLinkedInAccount
```

2. Setup `config.py` for your search preferences
3. Launch `main.py`
4. To get clean result, remove cache at `./output/*`