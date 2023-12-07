# Language Learning Chatbot
A guide to create an application with AWS Lambda, Streamlit, Docker, and the OpenAI Chat Completions API as a language learning tool. The online web app serves as a personal Gujarati language teacher.

### Demo Video: `https://www.youtube.com/watch?v=9JC8xxIKom8`

This project contains source code and supporting files for a serverless application deployed with SAM CLI. It includes the following files and folders:

* /base
  `function.py - Code for the application's Lambda function.`
  `app.py - Streamlit front-end.`
* events - Invocation events that you can use to invoke the function.
* tests - Unit tests for the application code. 
* template.yaml - A template that defines the application's AWS resources.

## Setup and Tools
To use the application, you need the following tools.

* AWS Account - IAM > User > Permissions
* Pycharm - AWS Toolkit Plugin
* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* OpenAI - Create Account and Generate API Key
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)
* Streamlit - Front-end Interface

## Guide for Project Setup

### Prerequisites:
Create an OpenAI account and generate an API key at `https://platform.openai.com/api-keys`. Then install the OpenAI library locally for the Lambda function layer. 
```console
pip install --upgrade openai
```
Before moving forward with SAM CLI in Pycharm, install both AWS CLI and Docker. Then download the setup file at `aws.amazon.com/serverless/sam`, and follow the same installation process like you did above for the CLI.

Finally, in Pycharm install the AWS Toolkit by going to `Pycharm > Settings > Plugins`, and then search `AWS Toolkit` and install.

Log into AWS account and go to `IAM`, create user and install the needed permissions for application. Then create an access key and secret access key. Open up terminal and type `aws configure`, and once prompted, add all credentials.

### Create Application
Open up Pycharm IDE and create new project. Choose `AWS Serverless Application`:
* Project Type: Zip
* Runtime: Python3.11
* SAM Template: AWS SAM Hello World

When you are finished with your application code, go to AWS account and navigate the Lambda console:
* Create Lambda function and configure environment variables.
* Then create an HTTP API in API Gateway, and attach it as a `Trigger` to your Lambda function.
* Make sure to add all of these updates to your `template.yaml` file.

Create OpenAI Chat Completions API, and then configure and run the OpenAI API locally:
* Go to `Run` > `Edit Configurations`.
* Click on `SAM CLI` and check the `Build function inside container` box.
* Then go back to `Configuration` and add the Event Template (JSON):
```console
{
  "queryStringParameters": {
    "prompt": "Your test prompt here"
  }
}
```
* Finally, click the option `Run`.

### Streamlit Setup

Use the terminal command to view web application:
```console
streamlit run ./base/app.py
```

## Deploy Application

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build --use-container
sam deploy --guided
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

You can find your API Gateway Endpoint URL in the output values displayed after deployment.

## Use the SAM CLI to build and test locally

Build your application with the `sam build --use-container` command.

```bash
Language-Learning$ sam build --use-container
```

The SAM CLI installs dependencies defined in `requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

The SAM CLI reads the application template to determine the API's routes and the functions that they invoke. The `Events` property on each function's definition includes the route and method for each path.

```yaml
      Events:
        lambdaFunctionAPI:
          Type: Api
          Properties:
            Path: /base
            Method: ANY
            Auth:
              Authorizor: NONE
```
