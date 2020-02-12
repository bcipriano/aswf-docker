import subprocess
import datetime
from . import constants


def get_current_branch() -> str:
    return subprocess.check_output("git rev-parse --abbrev-ref HEAD", encoding="UTF-8")


def get_current_sha() -> str:
    return subprocess.check_output("git rev-parse --short HEAD", encoding="UTF-8")


def get_current_date() -> str:
    # 2020-01-19T08:04:51Z
    return datetime.datetime.now().isoformat(timespec="seconds") + "Z"


def get_docker_org(repoUri: str, sourceBranch: str) -> str:
    if not sourceBranch and not repoUri:
        return constants.TESTING_DOCKER_ORG
    elif (
        sourceBranch == "refs/heads/master"
        and repoUri == "https://github.com/AcademySoftwareFoundation/aswf-docker"
    ):
        dockerOrg = constants.PUBLISH_DOCKER_ORG
    elif sourceBranch == "refs/heads/testing" or sourceBranch == "":
        dockerOrg = constants.TESTING_DOCKER_ORG
    else:
        dockerOrg = constants.FAKE_DOCKER_ORG
    return dockerOrg
