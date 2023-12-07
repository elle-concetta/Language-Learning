# Language Learning Chatbot
A guide to create a lambda function that utilizes OpenAI API Text Generation as a language learning tool.

This project contains source code and supporting files for a serverless application deployed with SAM CLI. It includes the following files and folders:

* base
*      function.py - Code for the application's Lambda function.
*       app.py - Code for Streamlit front-end.
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

#### Prerequisites:
Create an OpenAI account and generate an API key at `https://platform.openai.com/api-keys`. Then install the OpenAI library locally for the Lambda function layer. 
```console
pip install --upgrade openai
```
Before moving forward with SAM CLI in Pycharm, install both AWS CLI and Docker. Then download the setup file at `aws.amazon.com/serverless/sam`, and follow the same installation process like you did above for the CLI.

Finally, in Pycharm install the AWS Toolkit by going to `Pycharm > Settings > Plugins`, and then search `AWS Toolkit` and install.

Log into AWS account and go to `IAM`, create user and install the needed permissions for application. Then create an access key and secret access key. Open up terminal and type `aws configure`, and once prompted, add all credentials.

#### Create Application
Open up Pycharm IDE and create new project. Choose `AWS Serverless Application`:
* Project Type: Zip
* Runtime: Python3.11
* SAM Template: AWS SAM Hello World

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

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
Language-Learning$ sam local invoke HelloWorldFunction --event events/event.json
```

The SAM CLI can also emulate your application's API. Use the `sam local start-api` to run the API locally on port 3000.

```bash
Language-Learning$ sam local start-api
Language-Learning$ curl http://localhost:3000/
```

The SAM CLI reads the application template to determine the API's routes and the functions that they invoke. The `Events` property on each function's definition includes the route and method for each path.

```yaml
      Events:
        LanguageFunctionAPI:
          Type: Api
          Properties:
            Path: /base
            Method: GET
            Auth:
              Authorizor: NONE
```

## Add a resource to your application
The application template uses AWS Serverless Application Model (AWS SAM) to define application resources. AWS SAM is an extension of AWS CloudFormation with a simpler syntax for configuring common serverless application resources such as functions, triggers, and APIs. For resources not included in [the SAM specification](https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md), you can use standard [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) resource types.

## Fetch, tail, and filter Lambda function logs

To simplify troubleshooting, SAM CLI has a command called `sam logs`. `sam logs` lets you fetch logs generated by your deployed Lambda function from the command line. In addition to printing the logs on the terminal, this command has several nifty features to help you quickly find the bug.

`NOTE`: This command works for all AWS Lambda functions; not just the ones you deploy using SAM.

```bash
Language-Learning$ sam logs -n HelloWorldFunction --stack-name "language-learning" --tail
```

You can find more information and examples about filtering Lambda function logs in the [SAM CLI Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html).

## Tests

Tests are defined in the `tests` folder in this project. Use PIP to install the test dependencies and run tests.

```bash
Language-Learning$ pip install -r tests/requirements.txt --user
# unit test
Language-Learning$ python -m pytest tests/unit -v
# integration test, requiring deploying the stack first.
# Create the env variable AWS_SAM_STACK_NAME with the name of the stack we are testing
Language-Learning$ AWS_SAM_STACK_NAME="language-learning" python -m pytest tests/integration -v
```

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
sam delete --stack-name "language-learning"
```
