from plumbum import cli
from pyfiglet import Figlet
from plumbum.cmd import ls, git
from questionary import prompt

def print_banner(text):
    print(Figlet(font='slant').renderText(text))

def get_files():
    ls_output = ls().strip()
    files = ls_output.split("\n")
    return files

def generate_question(files):
    return [{
        'type': 'checkbox',
        'name': 'files',
        'message': 'What would would like to add?',
        'choices': [{'name': file.strip()} for file in files if not(file.startswith("__"))],
    }]

class FancyGitAdd(cli.Application):
    VERSION = "1.3"
    commit = cli.Flag(['c', 'commit'], help="Commits the added files as well")
    push = cli.Flag(['p', 'push'], help="Also push")

    def main(self):
        print_banner("Git Fancy Add")
        files = get_files()

        question = generate_question(files)
        answer = prompt(question)
        git('add', answer['files'])
        if self.commit:
            git('commit', '-m', 'updates')
        if self.push:
            git('push')


if __name__ == "__main__":
    FancyGitAdd()

def test_get_files():
    files = get_files()
    assert len(files) == 7, "There should be enough files"


def test_generate_question():
    files = ["one.text", "two.md", "three.docx", "__temp__"]
    question = generate_question(files)

    assert len(question) == 1, "has to be one question"
    assert question[0]['type'] == 'checkbox'
    assert len(question[0]['choices']) == len(files) - 1, "same number of files as what exists"