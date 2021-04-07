"""
How to multithread in python:
Synchronous Approach
The method below calls the yahoo finance library for 5 company symbols. It gets the information for each of the companies sequentially.
The code then prints out the time it took to get the information for the 5 companies:
"""
"""
import time
import yfinance as yf
started=time.time()

def print_company_info(company):
    ticker=yf.Ticker(company)
    info=ticker.get_info()
    print(info)

companies=['ABT','ABBV','ABMD','ATVI','ADBE']
for company in companies:
    print_company_info(company)

elapsed=time.time()

print('Time Taken: ',elapsed-started)
This is standard approach for wait for multithreaded approach
"""

"""
import time
import concurrent.futures
import yfinance as yf

started=time.time()

def print_company_info(company):
    ticker=yf.Ticker(company)
    info=ticker.get_info()
    print(info)

companies=['ABT','ABBV','ABMD','ATVI','ADBE']

size=5
with concurrent.futures.ThreadPoolExecutor(size) as thp:
    thp.map(print_company_info,companies)

elapsed=time.time()
print('Time Taken: ',elapsed-started)
This is one of the ways of multi threaded approach. Refer below for AsyncIO approach
"""
"""
import asyncio
import time
import yfinance as yf

def print_company_info(company):
    ticker = yf.Ticker(company)
    info = ticker.get_info()
    print(info)

companies = ['ABT', 'ABBV', 'ABMD', 'ATVI', 'ADBE']

tasks = []
event_loop = asyncio.get_event_loop()
for company in companies:
    #Not calling the functions here, we are storing an awaitable functions in an array
    tasks.append((print_company_info(company)))
started = time.time()
event_loop.run_until_complete(asyncio.wait(tasks))
elapsed = time.time()
print('Elapsed time : ',elapsed-started)
"""