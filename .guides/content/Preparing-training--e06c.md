
Now that we have installed the necessary tools in the back end we can start training our data. Training data is how you teach GPT-3 what you'd like it to say. 

GPT-3 expects your fine-tune dataset to be in a specific JSONL file format:
```python-hide-clipboard
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
```
The tool accepts different formats, with the only requirement that they contain a prompt and a completion column/key. Then simply run it through the OpenAI command-line tool to validate it.
You can pass a CSV, TSV, XLSX, JSON or JSONL file, and it will save the output into a JSONL file ready for fine-tuning. JSON Lines(.jsonl) is like JSON, but each line is a valid JSON object. This means that each line is a separate, independent data entry, which can be read, parsed, and processed independently of the others. It will bring up suggesting changes as you proceed. 

A sample data,`SampleData.csv`, has been provided for this exercise. It has about 50 examples. When going about it on your own please note it usually recommends a few hundred examples. The sample data is a csv which we can see on the top left. Run the following code, replace `<LOCAL_FILE>` with `SampleData.csv`.
```
openai tools fine_tunes.prepare_data -f <LOCAL_FILE>
```
When you are done, we can run the following line of code on your terminal so we can peek at our newly generated JSONL file.
```
head -5 SampleData_prepared_valid.jsonl
```
The following assumes you have already prepared training data.The training file goes in the  `< >` and the second one is for the BASE_MODEL that is the name of the base model you're starting from (ada, babbage, curie, or davinci). 

Train a new fine-tuned model, replace train file  `<TRAIN_FILE_ID_OR_PATH>` with `SampleData_prepared.jsonl` and `<BASE_MODEL>` with `curie`:
```
openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL>
```
This often takes a few minutes but can take longer depending on the data and the model. 

Running the above command does several things:

1. Uploads the file using the files API 
2. Creates a fine-tune job
3. Streams events until the job is done 

If by any chance, the work is interrupted, you can run the following command to get it back on track. 
`openai api fine_tunes.follow -i <YOUR_FINE_TUNE_JOB_ID>`
The command you need can be copied from the terminal if the stream is interrupted.

When your command is done running you should see the following message.

![.guides/img/success](.guides/img/success.png)

Please make sure you copy the model name in the response.  In our case should be `curie: ft`
Hint: after the line saying `Try out your fine-tuned model`: the command you need can be copied in the terminal 
{Check It!|assessment}(fill-in-the-blanks-455380182)
