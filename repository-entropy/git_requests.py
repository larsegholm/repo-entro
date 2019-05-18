import requests as req


class GitRequester:

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

    def get_commits(self):
        request_url = self.form_request(["commits"])
        print(request_url)
        package = req.get(request_url)
        package_json = package.json()
        for js in package_json :
            print(js)

