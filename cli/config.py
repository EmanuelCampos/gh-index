import yaml

def load_config(filename='config.yaml'):
    with open(filename, 'r') as file:
        config = yaml.safe_load(file)
    return config