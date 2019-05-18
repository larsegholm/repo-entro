from git_requests import GitRequester


def main():
    git_requester = GitRequester("https://api.github.com", "larsegholm", "EntropyTest")
    print(git_requester)
    git_requester.get_commits()

    return


if __name__ == main():
    main()
