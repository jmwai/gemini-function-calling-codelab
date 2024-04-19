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

The function calling codelab goes through these steps

- setup (use this guide)
- test gemini text generation. Try the code in `test_generate.py`
- trying a workaround `workaround.py`
- testing the currency api `api.py`
- Building the function `function.py`



