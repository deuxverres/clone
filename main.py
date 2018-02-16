from git import Repo
import yaml as YAML

with open("manifest.yaml",'r') as f:
    try:
        manifest = YAML.load(f)
    except YAML.YAMLError as err:
        print(err)
        quit(1)

for dirc, url in manifest["urls"].items():
    Repo.clone_from(url,dirc)