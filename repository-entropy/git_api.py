import requests as req


class GitApi:

    # Need to create some integration tests for this
    __git_api_version = "v3"
    __git_url = None
    __owner = None
    __repo = None

    def __init__(self, git_url, owner, repo):
        self.__git_url = git_url
        self.__owner = owner
        self.__repo = repo

    def __str__(self):
        return "Entry-point : " + self.__form_request([])

    def __form_request(self, api_paths):
        return '/'.join([self.__git_url] + ["repos"] + [self.__owner] + [self.__repo] + api_paths)

    def get_commit_shas(self):
        request_url = self.__form_request(["commits"])
        accept_header = "application/vnd.github." + self.__git_api_version + ".json"
        package = req.get(request_url, accept_header)
        assert(package.status_code == 200)
        return [commit["sha"] for commit in package.json()]  # Hmmm, refine this when doing analysis

    def get_diff(self, commit_sha):
        request_url = self.__form_request(["commits", commit_sha])
        accept_header = "application/vnd.github." + self.__git_api_version + ".diff"
        package = req.get(request_url, headers={"Accept":accept_header})
        assert (package.status_code == 200)
        return package.text
