import urllib, urllib.request
from aslite.arxiv import get_response, parse_response

search_query = 'cat:cs.CV'
start_index = 0
resp = get_response(search_query=search_query, start_index=0, batch=3)
print(resp.decode('utf-8'))

papers = parse_response(resp)
print(papers)
