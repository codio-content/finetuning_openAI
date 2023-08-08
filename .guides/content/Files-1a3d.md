Files are used to upload documents that can be used with features like Fine-tuning. Let's go over some basic commands to work with files with the OpenAI API.
Before that we need to identify what file can be uploaded. Each line in the file should be a JSON dictionary with two keys: "prompt" and "completion". The "prompt" key should contain the input text to be used for fine-tuning, and the "completion" key should contain the expected output text.
```json-hide-clipboard
{"prompt": "What is the capital of France?", "completion": "The capital of France is Paris."}

```
### Uploading a file

To upload a file to the OpenAI API, use the `create` command with the `file` and `purpose` arguments. To insert the following, click on the `file.py` tab on the left panel. Then copy and paste the following. 

```python
with open("my_document.txt", "rb") as f:
    response=openai.File.create(
        file=f,
        purpose="fine-tune"
    )
print(response)
```
{Try it!}(python3 file.py 1)

The `file` argument specifies the name of the file as it will be stored in the API. The `purpose` argument specifies the intended use of the file, such as fine-tuning or search. 

This code will read `"my_document.txt"` from your local machine and upload it to OpenAI for the purpose of fine-tuning. The response object will contain the server's response, which should include the ID of the newly created file which we need for the next part.



### List 
----
To list the files that belong to the current user, use the `list`command:

```
files = openai.File.list()
print(files)
```

{Try it!}(python3 file.py 3)
This will return a list of `File` objects that correspond to the files that belong to the user. Each `File` object has a `filename` and a `purpose` attribute, as well as other metadata like the file size and upload date.
One of the key pieces of data you will interact the most with is the file ids. Copy and paste the following just to print out the ids of your files. 
```python
# Retrieve list of files
files = openai.File.list()

# Print all file IDs
for file in files.data:
    print(file.id)
```
{Try it!}(python3 file.py 8)

### Delete
To delete a file from the OpenAI API, use the delete method of the File object:

Now that you have your list id you can copy and paste the following to delete an file. Make sure to replace `"file-oUBzcM42OuWO4wDnnIR9uzSN"` with the actual ID of the file you want to delete.
```python

# Delete the file by ID
file_id = "file-oUBzcM42OuWO4wDnnIR9uzSN"
openai.File.delete(file_id)

```
{Try it!}(python3 file.py 5)


### Downloading
To download the contents of a file from the OpenAI API, use the following method of the File object:
```python3 
# Step 1: Upload a file
with open("my_document.txt", "rb") as f:  # Replace with your actual file
    response = openai.File.create(
        file=f,
        purpose="fine-tune"
    )

# The file ID is in the response from the API
file_id = response.id
print(f"Uploaded file ID: {file_id}")

# Step 2: Download the file using its ID
download_url = f"https://api.openai.com/v1/files/{file_id}/content"

headers = {
    "Authorization": f"Bearer {openai.api_key}"
}

response = requests.get(download_url, headers=headers)

with open("my_doc2.txt", "wb") as f:  # The file will be saved with this name
    f.write(response.content)

print("Downloaded file saved as my_doc2.txt")
```
{Try it!}(python3 file.py 4)
This will download the contents of the file `"my_document.txt"` from the API and save them to a local file with the same name. Please note if using a free account, there might be an error generated with the text in the downloaded file saying that downloading of fine-tuned files is disabled
![image showing error with message that downloading is disabled on free accounts in order to mitigate abuse.](freeAccount.png)



{Check It!|assessment}(multiple-choice-1648796114)