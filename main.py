import os
from dotenv import load_dotenv
import yaml

from gitlabmanager import Gitlabmanager


load_dotenv()


def parseReposList():
    with open("repolist.yml", "r") as repolist:
        yaml_data = repolist.read()
        data = yaml.safe_load(yaml_data)

        # repos
        repo_list = [
            [rd["repo_name"], rd["develop_repo"], rd["external_repo"]]
            for repo, rd in data["repos"].items()
        ]

        # configs
        configs = {}
        for p in data["configs"]:
            configs[p] = data["configs"][p]

        configs["gitlab_token"] = os.getenv("GITLAB_TOKEN")

        return repo_list, configs


if __name__ == "__main__":
    repo_list, configs = parseReposList()

    gm = Gitlabmanager(repo_list, configs)

    urls = gm.process_git2git()

    print("MIRRORING PROJECTS CREATED")
    for url in urls:
        print(url)
