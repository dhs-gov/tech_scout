"""
Before you can use the Google API, you must do the following:

Follow instructions at:
    https://programmablesearchengine.google.com/controlpanel/all?optin=true

Select Add.

On next page:
•	Name your engine
•	Search entire web
•	I’m not a robot
•	Create

On next page (Your new search engine has been created), select “Go to legacy Control Panel” at the top.
Next, select Continue.

On next page:
    Select your search engine
    Copy your search engine ID
    Copy your public URL

Next, go to https://developers.google.com/custom-search/v1/introduction and 
select ‘Get a Key’. In the ‘Enable Custom Search API’, enter a new project 
name. Next, select ‘Show Key’ and copy your API key: 

Next, fill in your API_KEY and SEARCH_ENGINE_ID below.
"""

import requests

# get the API KEY here: https://developers.google.com/custom-search/v1/overview
API_KEY = "<your API key here>"

# get your Search Engine ID on your CSE control panel
SEARCH_ENGINE_ID = "Your search engine ID here>"

# the search query you want
query = "sean warnick byu"
# using the first page
page = 1
# constructing the URL
# doc: https://developers.google.com/custom-search/v1/using_rest
# calculating start, (page=2) => (start=11), (page=3) => (start=21)
start = (page - 1) * 10 + 1
url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"

# make the API request
data = requests.get(url, verify=False).json()

# get the result items
search_items = data.get("items")

# iterate over 10 results found
for i, search_item in enumerate(search_items, start=1):
    print('-----------')
    # Use the following to see other available keys
    #print(f'{search_item}, type: {type(search_item)}')
    print(f'Title: {search_item["title"]}')
    print(f'Link: {search_item["link"]}')
    print(f'Snippet: {search_item["snippet"]}')
    print(f'Pagemap: {search_item["pagemap"]}')

    #for k, v in search_item.items():
    #    print(k, v)
    """
    THE FOLLOWING IS NOT WORKING
    try:
        long_description = search_item["pagemap"]["metatags"][0]["og:description"]
    except KeyError:
        long_description = "N/A"
    # get the page title
    title = search_item.get("title")
    # page snippet
    snippet = search_item.get("snippet")
    # alternatively, you can get the HTML snippet (bolded keywords)
    html_snippet = search_item.get("htmlSnippet")
    # extract the page url
    link = search_item.get("link")
    # print the results
    print("="*10, f"Result #{i+start-1}", "="*10)
"""