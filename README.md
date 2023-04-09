# Veezum

_Obscure but simple way for checking the status of your Czech Visa application using **selenium** and **telegram**_

## Disclaimer

**_This bot/scrapper was created for two purposes:_**

- **_Automation of a repetitive mundane task_**

- **_Education_**

**_I have decided to share the code for same reasons. Also fun._**


**_Consequently, there is a limit in the constructor so that it raises a ValueError when it tries to schedule the bot at more 
than two times per day._**


**_I suspect that even that number might be an overkill_**

--------------------

## Usage


**_Unix / macOS:_**

    python3 -m Veezum

**_Windows:_**

    py -m Veezum

--------------------

## Installation


- **Step 1: Setting up the Telegram bot**

    * Download and install Telegram Messenger on your smartphone
  
    * Message _@BotFather_, and make a new bot using:
  
          /newbot
  
    * Make note of the token for the HTTP API

    * You can read more about bots and Telegram API [here](https://core.telegram.org/bots)
  
- **Step 2: Install Veezum**

    * Download and then install the latest release using:
  
            pip install Veezum-<Version Number>.tar.gz
  
    * Build your own using _python -m build_

- **Step 3: Set up the Environment Variables:**

    * Veezum scrapper gets all the attributes required passed through with the Environment Variables
  
        + veezum_ids - List of IDs provided by the Embassy, in format:
      
                ABCD123456879,ABCD123456789
      
        + veezum_times - List of times for the bot to execute at, in format:
      
                08:00,16:00
      
        + veezum_token - Telegram HTTP API Token

--------------------

## Requirements

    schedule
    selenium
    requests
    webdriver_manager

    optional:
    pytest


--------------------

## Planned Changes

- Improve Exception / Error Handling

- Fix occasional socket issue

- Fix unnecessary waits

- Improve and simplify testing

    * Expand test cases
  
    * Refactor code for repetition
  

