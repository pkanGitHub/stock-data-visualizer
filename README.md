# Stock Data Visualizer

This is a python application that will take user input from the terminal, plot it accordingly to get the URL for the API, and render a stock chart in the browser based on Alpha Vantage API.

---

## Instructions to run the code:
<br/>

`cd` into the directory `app.py` is located. <br>
run 
```
python3 app.py
```
---

## The user will be prompted for the following:
**Symbol** - for example (GOOGL, IBM) <br/>
**Chart Type** - Bar or line <br/>
**Time Series:** 
- Intraday, daily, weekly, and monthly <br/>
    - Interaday's interval is set to 60 mins.
    - Intraday's date will overlap in graph if date range is more than 2 days due to the large volume of data<br/> 

**Start/End dates:** 
- *(YYYY-MM-DD)* format <br/>
- start date cannot be the same date or later than current date
- end date cannot be before the start date

(after the chart renders in the browser) <br/>

**Program is closed or reran based on user input**






