from git_api import GitApi
from git_diff import GitDiff


def main():
    git_api = GitApi("https://api.github.com", "larsegholm", "EntropyTest")
    shas = git_api.get_commit_shas()
    diffs = iter(GitDiff(git_api.get_diff(sha)) for sha in shas)
    for diff in diffs:
        print(diff)

    return


if __name__ == main():
    main()
