## How to Interact with APIs Using Function Calling in Gemini

This repository helps you implements this codelab
https://codelabs.developers.google.com/codelabs/gemini-function-calling

### Setup

Ensure you have at least Python3.8 on your machine.

#### create a virtual environment 
##### Mac/Linux
```
pip install virtualenv
virtualenv <your-env>
source <your-env>/bin/activate

```
##### Windows
```
pip install virtualenv
virtualenv <your-env>
<your-env>\Scripts\activate
```

##### Install the google ai platform library

Mac/Linux
`<your-env>/bin/pip install google-cloud-aiplatform`

Windows
`<your-env>\Scripts\pip.exe install google-cloud-aiplatform`

You can also find installation guide here 

https://github.com/googleapis/python-aiplatform

#### Create a Google Cloud Project

You can follow this guide 

https://cloud.google.com/resource-manager/docs/creating-managing-projects

Save project id as an env variable

`export PROJECT_ID=your-project-id`

Verify the Variable: 

`echo $PROJECT_ID`

#### Verify your setup is okay

 To verify that you setup is working, You can run the code like this 

 `python3 test_generate.py`  
 
 If the setup is okay, you should see gemini response on your terminal.
 Something close to this;
 ```
As of Thursday, October 26, 2023, 1 US Dollar (USD) is equal to approximately 0.98 Euros (EUR). This means that for every 1 USD, you can exchange it for around 0.98 EUR.

It is important to note that exchange rates are constantly fluctuating and can change at any time. This is just a snapshot of the current rate and may not reflect the actual rate at the time you make your transaction. 

Here are some resources where you can find updated exchange rates:

* **Reuters:** https://www.reuters.com/finance/currencies
* **XE Currency:** https://www.xe.com/currencyconverter/
* **Yahoo Finance:** https://finance.yahoo.com/currencies

These resources will also allow you to convert other currencies, not just USD and EUR.
```

####  The code lab

The function calling codelab goes through these steps

- setup (use this guide)
- test gemini text generation. Try the code in `test_generate.py`
- trying a workaround. The code is in `workaround.py`
- testing the currency api. The code is in `api.py`
- Building the function. The code is in `function.py`



