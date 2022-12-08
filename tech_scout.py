# Test of simple scraper and entity extractor.
import requests

# NSF awards API is found at: 
# https://www.research.gov/common/webapi/awardapisearch-v1.htm
nsf_awards_json_api = 'http://api.nsf.gov/services/v1/awards.json'
keywords = 'keyword=ai'

# Make the URL request
res = requests.get(nsf_awards_json_api + '?' + keywords)

# Get the awards data
json_response = res.json()["response"]
print(f'type(awards): {type(json_response)}')
print(json_response)
awards = json_response["award"]

# Show each award in the list of awards
for award in awards:
    print('----')
    # Print the award info for each awardee
    print(f'agency: {award["agency"]}')
    print(f'awardeeCity: {award["awardeeCity"]}')
    print(f'awardeeName: {award["awardeeName"]}')
    print(f'awardeeStateCode: {award["awardeeStateCode"]}')
    print(f'fundsObligatedAmt: {award["fundsObligatedAmt"]}')
    print(f'id: {award["id"]}')
    print(f'piFirstName: {award["piFirstName"]}')
    print(f'piLastName: {award["piLastName"]}')
    print(f'publicAccessMandate: {award["publicAccessMandate"]}')
    print(f'date: {award["date"]}')
    print(f'title: {award["title"]}')
    # abstractText is not a valid key even though it is listed on NSF site.
    #print(f'abstractText: {award["abstractText"]}')



