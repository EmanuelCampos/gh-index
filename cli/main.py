import click
import yaml
import cli.index as index
import cli.config as settings

@click.group()
def cli():
    pass

@cli.command()
@click.argument('query_string')
def query(query_string: str):
    """Execute a query."""

    current_config = settings.load_config()
    
    print(f"Using the following configuration:")
    print(current_config)

    print(f"Running the query: {query_string} ...")
    response = index.search(query_string)

    print(response)

@cli.command()
@click.option('--repository-owner', required=False, help='Name of the repository owner.')
@click.option('--repository-name', required=False, help='Name of the repository.')
@click.option('--directories-to-include', required=False, multiple=True, help='List of directories to include.')
@click.option('--file-extensions-to-include', required=False, multiple=True, help='List of file extensions to include.')
@click.option('--github-branch', required=False, help='GitHub branch name.')
def update_config(repository_owner, repository_name, directories_to_include, file_extensions_to_include, github_branch):
    """Update the configuration based on provided parameters."""

    current_config = settings.load_config()
    
    config = {
        'repository_owner': repository_owner if repository_owner else current_config['repository_owner'],
        'repository_name': repository_name if repository_name else current_config['repository_name'],
        'directories_to_include': list(directories_to_include) if directories_to_include else current_config['directories_to_include'],
        'file_extensions_to_include': list(file_extensions_to_include) if file_extensions_to_include else current_config['file_extensions_to_include'],
        'github_branch': github_branch if github_branch else current_config['github_branch'],
    }
    
    with open('config.yaml', 'w') as file:
        yaml.safe_dump(config, file)

    click.echo("Configuration updated successfully!")


if __name__ == "__main__":
    cli()
