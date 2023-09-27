import pickle
import os

import cli.config as config

from llama_index import download_loader, GPTVectorStoreIndex
from llama_hub.github_repo import GithubClient, GithubRepositoryReader

def search(query: str = "Retrieve all API endpoints"):
    download_loader("GithubRepositoryReader")

    current_config = config.load_config()

    # File path and parameters
    file_path = "docs.pkl"
    github_personal_key = os.environ["GITHUB_TOKEN"]
    repository_owner = current_config['repository_owner']
    repository_name = current_config['repository_name']
    directories_to_include = current_config['directories_to_include']
    file_extensions_to_include = current_config['file_extensions_to_include']
    github_branch = current_config['github_branch']

    # Load existing data if file exists
    docs = None
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            docs = pickle.load(f)

    # If data not loaded, fetch from GitHub and save
    if docs is None:
        github_client = GithubClient(github_personal_key)
        loader = GithubRepositoryReader(
            github_client,
            owner=repository_owner,
            repo=repository_name,
            filter_directories=(directories_to_include, GithubRepositoryReader.FilterType.INCLUDE),
            filter_file_extensions=(file_extensions_to_include, GithubRepositoryReader.FilterType.INCLUDE),
            verbose=True,
            concurrent_requests=10,
        )
        docs = loader.load_data(branch=github_branch)

        # Save fetched data for future use
        with open(file_path, "wb") as f:
            pickle.dump(docs, f)


    index = GPTVectorStoreIndex.from_documents(docs)

    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return response