Fine-Tuning lets you get more out of the models available through the API by providing:

1) Higher quality results than prompt design
2) Ability to train on more examples than can fit in a prompt
3) Token savings due to shorter prompts
4) Lower latency requests

Fine-tuning is all about changing the model so it can generate the responses you want every time. The capabilities and knowledge of the model will be fully focused on the dataset used for fine-tuning. 

Fine-tuning improves on few-shot learning by training on many more examples than can fit in the prompt, letting you achieve better results on a wide number of tasks. Once a model has been fine-tuned, you won't need to provide examples in the prompt anymore. For example, this is how the dataset **json** file would look like.


```json-hide-clipboard
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
```
JSONL, stands for JSON Lines. It is a format that represents structured data as a sequence of JSON objects, each on a separate line. Instead of a single JSON object enclosed within curly braces, each line in a JSONL file represents a separate, self-contained JSON object. This makes JSONL a format suitable for streaming large amounts of data or processing data line by line.

Before we get started, it is recommended to install the OpenAI command-line interface. To do this we are going to run the following command in the terminal (left panel). 
```
pip install --upgrade openai
```

# 
<details>
  <summary><b>If you get numpy version error</b></summary>
You can run the following in the terminal and try again:

<code>pip install numpy --upgrade</code>
</details>

<br>


Run the following in the terminal but this time switching `API KEY` with your API key.
```
export OPENAI_API_KEY="<OPENAI_API_KEY>"
```
Hint: Your OpenAI key can be found by clicking in the menu Codio -> Preferences -> Environment Variables.
{Check It!|assessment}(multiple-choice-3646828368)
