-------------------

Fine-tuning is a powerful technique to create a new model that's specific to your use case. Before fine-tuning your model, we strongly recommend reading these best practices and [specific guidelines](https://beta.openai.com/docs/guides/fine-tuning/specific-guidelines) for your use case.

After creating our new model after our success message it should generate a message saying try out your model. Insert the fine-tuned model command we copied from the previous page. it should look like the commnad below. Use  `"Codio sign: its tuesday ->"` for your prompt.
**Run it in the terminal:**
```terminal
openai api completions.create -m <FINE_TUNED_MODEL> -p <YOUR_PROMPT>
```
In order to generate output with Python you can try the following using your model in the `openai.Completion.create()` function in the `tester.py` file opened in the upper-left panel:
**python3:**
```python
  model= "curie:ft-personal-.....",
  prompt="Codio sign: its tuesday ->"
```
{Try it!}(python3 tester.py)
After you’ve fine-tuned a model, remember that your prompt has to end with the indicator string ` ->` for the model to start generating completions, rather than continuing with the prompt.

Play around with a couple of prompts. Please note that while playing around the AI can generate different answers every run. Additionally, you can play around with some of these as extra arguments like `temperature` `top_p` `max_tokens`. 

When ready we can go over deleting our model. In case you no longer want to interact with a model you created you can run the following code to remove it.  

**Run it in the terminal:**
```
openai api models.delete -i <FINE_TUNED_MODEL>
```
After your fine-tuned model is deleted you can see something similar in the terminal:

![A picture demonstrating what message would be printed after deleting the model. It shows deleted=true,id =.... and object=model](deleteimg.png)

Or do it in **python3:**
```python
import openai
openai.Model.delete(FINE_TUNED_MODEL)
```
{Try it!}(python3 tester.py 2)

{Check It!|assessment}(fill-in-the-blanks-1528262106)