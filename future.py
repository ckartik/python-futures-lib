import requests
import concurrent.futures as cf
from functools import lru_cache
import time

def future(func, paramList):
    return cf.ProcessPoolExecutor(max_workers=len(paramList)).map(func, paramList)

@lru_cache(maxsize=4)
def query(url):
    req = requests.get(url)
    return req

def query_non_cahced(url):
    req = requests.get(url)
    return req

urls = ['http://www.ckartik.com', 'http://ckartik.com/posts/os-concepts-common/', 'http://ckartik.com/about/', 'http://ckartik.com/posts/exception-handling/']
start = time.time()
posts = [post for post in future(query, urls)]
end = time.time()

print("The time to query the URLs in concurrent fashion took: {}".format(end-start))

start = time.time()
posts = [query_non_cahced(post) for post in urls]
end = time.time()

print("The time to query the URLs in regular fashion took: {}".format(end-start))