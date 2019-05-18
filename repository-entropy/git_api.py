import requests as req


class GitApi:

    git_api_version = "v3"
    git_url = ""
    owner = ""
    repo = ""

    def __init__(self, git_url, owner, repo):
        self.git_url = git_url
        self.owner = owner
        self.repo = repo

    def __str__(self):
        return "Entry-point : " + self.form_request([])

    def form_request(self, api_paths):
        return '/'.join([self.git_url]+["repos"]+[self.owner]+[self.repo]+api_paths)

    def get_commit_shas(self):
        request_url = self.form_request(["commits"])
        accept_header = "application/vnd.github." + self.git_api_version + ".json"
        package = req.get(request_url, accept_header)
        assert(package.status_code == 200)
        return [commit["sha"] for commit in package.json()] # Hmmm, refine this when doing analysis

    def get_diff(self, commit_sha):
        request_url = self.form_request(["commits", commit_sha])
        accept_header = "application/vnd.github."+self.git_api_version+".diff"
        package = req.get(request_url, headers={"Accept":accept_header})
        assert (package.status_code == 200)
        return package.text
