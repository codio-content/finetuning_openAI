import os
import openai
import secret
openai.api_key=secret.api_key

### CODIO SOLUTION BEGIN
prompts ="what is the sentiment of the following sentences:['i am happy','i am happy to be sad','I am sad']"

response = openai.Completion.create(
  model="text-davinci-002",
  prompt=prompts,
  top_p=0.1,
  max_tokens=50)


print(response['choices'][0]['text'].strip())
## CODIO SOLUTION END