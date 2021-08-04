# AlgorithmicTrading
Algorithmic Trading with Python

Source: Algorithmic Trading Using Python - Full Course
Link: https://www.youtube.com/watch?v=xfzGZB4HhEE&list=WL&index=28&t=10811s

1. Algorithmic Trading Basics
2. API Basics and Course Configuration
3. Project 1: Equal-Weight S&P 500 Screener
4. Project 2: Quantitative Momentum Screener
5. Project 3: Quantitative Value Screener


# Algorithmic Trading Overview 
Means using computers to makie investment decisions. 
There are many differente types of algorithmic trading. The main difference is their speed of execution. 
Here are some of main players in the algorithmic trading landscape (Fundos de investimento): 

Renaissance Technologies 
AQR Capital Management
Citadel Securities

# The Algorithmic Trading Process
The process of running a quantitative investing strategy can be broken down into the following steps.

1. Collect data
2. Develop a hypothesis for a strategy
3. Backtest that strategy


# How this course will be different than algorithmic trading in production
Because this is an introductory course, it will differ from production algorithmic trading in 3 major ways: 
1. We'll be using random data. 
    Sandbox API token (free)
2. We will not be executing trades
    Creation of ordersheets for imaginary tradings
3. We will be saving recommended trades in excel files. 


# API Basics and Course Configuration 
API - Aplication programming interface. 
    Interact and control other software with your own code. 
    In this course, we'll be using the IEX Cloud API to gather stock market data to make investiment decisions. 
    POST - Adds data to the database exposed by the API (create only)
    PUT - Adds and overwrites data in the database exposed by the API (create only)
    Check public APIS in github public apis 


# Momentum Investing Project Overview
Momentum investing means investing in assets that have increased in price the most. 

# Value Investing Project Overview
Value investing means investing in stocks that are trading below their perceived intrinsic value. 
Creating algorithmic value investing strategies relies on a concept called multiples. 

Multiples are calculated by dividing a company's stock price by some measure of the company's worth - like 
earning and assets. 

Here are a few examples of common multiples used in value investing. 
1. Price-to-earnings
2. Price-to-book-value
3. Price-to-free-cash-flow

Each of the individual multiples used by value investors has its pros and cons. 
One way to minimize the impact of any specific multiple is by using a composite. 
We'll use a composite of 5 different valuation strategies in our strategy. 



