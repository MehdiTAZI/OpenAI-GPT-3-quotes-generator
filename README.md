# GPT-3-quotes-generator
Use an AWS Lambda to exposes a webservice that returns a simple quote of prophetes and explain it using OpenAI GPT-3


## Usage : 

### Local : 

you should intall openAI for example using pip :  pip install openai

then you can call the function

  api_result = lambda_handler(None,None)
  result_body = json.loads(api_result['body'])
  print(result_body['answer'])
 

### On AWS Infrastructure : 
  Create a new AWS Lambda function
  Use the API Gateway to expose the Lambda function
  call the webservice using a HTTP Client
