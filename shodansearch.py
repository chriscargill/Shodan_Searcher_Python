import shodan

# Enter your shodan Api Key here or use a separate config file
SHODAN_API_KEY = ""

# Enter what you are searching for in this variable
desired_search = ""

api = shodan.Shodan(SHODAN_API_KEY)

try:	#Search Shodan
	results = api.search(desired_search)
	#Show the resultz
	print 'Results found: %s' % results['total']
	for result in results['matches']:
	    print 'IP: %s' % result['ip_str'] # Print the ip address
	    print result['data']
        print 'END'
except shodan.APIError, e:
	print 'There was an error while searching Shodan: %s' % e
