# GH-Index CLI Tool

gh-index is a command-line tool for interacting with your GitHub repositories and executing specific queries. It allows users to update configurations and search using the configurations set.

## Installation
First, ensure you have Python installed. This tool was developed using Python 3.9.

Clone the repository:

```bash
git clone https://github.com/EmanuelCampos/gh-index
cd gh-index
```

Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Install the tool in editable mode:

```bash
pip install -e .
```

## Configuration
### Environment Variables
You need to set the following environment variables:


```bash
EXPORT GITHUB_TOKEN=<YOUR GITHUB_PERSONAL_TOKEN HERE>
EXPORT OPENAI_API_KEY<YOUR OPENAI_API_KEY HERE>
```

## Using the Tool
To update the configuration:

```bash
gh-index update-config --repository-owner [OWNER] --repository-name [NAME] --directories-to-include [DIR1] --directories-to-include [DIR2] --file-extensions-to-include [.EXT1] --file-extensions-to-include [.EXT2] --github-branch [BRANCH_NAME]
```

Replace [OWNER], [NAME], [DIR1], [DIR2], [.EXT1], [.EXT2], and [BRANCH_NAME] with your desired values.

For example:

```bash
gh-index update-config --repository-owner run-llama --repository-name sec-insights --directories-to-include backend --directories-to-include frontend --file-extensions-to-include .py --github-branch main
```

## Usage
Once the configuration is set, you can use other commands like query commands that will be based on the configurations you've set.

### Query the data

To query specifics pieces of your data, you can run: 
```bash
gpt-index query "List for me all fastapi routes and paramters on conversations.py file"
```

output:
```bash
Using the following configuration:
{'directories_to_include': ['backend', 'frontend'], 'file_extensions_to_include': ['.py'], 'github_branch': 'main', 'repository_name': 'sec-insights', 'repository_owner': 'run-llama'}
Running the query: List for me all fastapi routes and paramters on conversations.py file ...
There are four FastAPI routes in the `conversation.py` file:

1. POST `/`: This route is used to create a new conversation. It expects a payload of type `schema.ConversationCreate` and returns a response of type `schema.Conversation`.

2. GET `/{conversation_id}`: This route is used to get a conversation by its ID along with its messages and message subprocesses. It expects a path parameter `conversation_id` of type `UUID` and returns a response of type `schema.Conversation`.

3. DELETE `/{conversation_id}`: This route is used to delete a conversation by its ID. It expects a path parameter `conversation_id` of type `UUID` and does not return any response.

4. GET `/{conversation_id}/message`: This route is used to send a message from a user to a conversation and receive a SSE (Server-Sent Events) stream of the assistant's response. It expects path parameter `conversation_id` of type `UUID` and query parameter `user_message` of type `str`. It returns a response of type `EventSourceResponse`.
```

## Contributon
- Adding soon