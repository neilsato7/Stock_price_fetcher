Get Stock Data

This code gets all current stocks listed on the NASDAQ website for the following US exchanges:
- NYSE
- AMEX
- NASDAQ

The files it uses are in this github: https://github.com/rreichel3/US-Stock-Symbols
Note this code is getting the ticker list from files run at 12am each day.

The code in this repo pulls the stock tickers from those lists and then allows you to chose a timeframe to retreive data about those stocks.
Stats currently included:
- Open
- High
- Low
- Close
- Volume

It writes all this to a csv file.
There is one flaw though, if there are 6000+ stocks, it makes a 5 columns of data per stock.
So right now the data isnt in the most usable form and needs to be arranged better.
