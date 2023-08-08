import os
import openai
import secret
openai.api_key=secret.api_key

#opens the file and reads the lines
with open("box.txt") as f:
    contents = f.readlines()
#if they dont write anything the get a message to write something
if contents==[] :
  print("Please write a prompt in the box above")
else:
  #contents is a list of lines. we join them then use it as the prompt
  prompts = "".join(contents)
  response = openai.Completion.create(model="text-davinci-002", 
                                      prompt=prompts,
                                      max_tokens=256)
  txt_response=response['choices'][0]['text'].strip()
  #the following adds an extra line then writes the response in the following line 
  f = open("box.txt", "a")
  f.write(("\n"+txt_response))
  f.close()
