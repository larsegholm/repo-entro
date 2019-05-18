from unittest import TestCase
from git_diff import GitDiff


class TestGitDiff(TestCase):
    __test_text = "diff --git a/testText b/testText\n" \
                  "index 1fe64f2..4f66e28 100644\n" \
                    "--- a/testText\n" \
                    "+++ b/testText\n" \
                    "@@ -1,3 +1,3 @@\n" \
                    " aaaaaaa\n" \
                    "-bbbbb\n" \
                    " ejgwpegjweopgjewpo\n" \
                    "+asdasdadsada\n" \
                    "\\ No newline at end of file\n"

    def test_additions(self):
        git_diff = GitDiff(self.__test_text)
        adds = git_diff.additions()

        self.assertEqual(len(adds), 1)
        self.assertEqual(adds[0], "asdasdadsada")

    def test_removals(self):
        git_diff = GitDiff(self.__test_text)
        rems = git_diff.removals()

        self.assertEqual(len(rems), 1)
        self.assertEqual(rems[0], "bbbbb")

    def test_all(self):
        git_diff = GitDiff(self.__test_text)
        all = git_diff.all()

        self.assertEqual(len(all), 2)
        self.assertIn("asdasdadsada", all)
        self.assertIn("bbbbb", all)
