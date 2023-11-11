# Practical introduction to Python's subprocess module
# https://www.youtube.com/watch?v=yeH3rw3rgHA

from argparse import ArgumentParser
from pathlib import Path
import subprocess


def project_starter(projectname):
    print(projectname)
    """_summary_
    Args:
        projectname (_type_): _description_
    Create a simple directory with projectname, and then initialise with:
    1. README.md
    2. requirements.txt
    3. Create a virtual environment
    4. Create a .gitignore
    5. Initialize git and make our first commit
    6. [Optional] add a Task on a TaskWarrior
    """
    
    project_dir = Path.cwd().absolute() / projectname       # might be also e.g. / "projects" / projectname
    print(project_dir)
    project_dir.mkdir()
    
    # create a file named README.md and requirements.txt
    (project_dir/"README.md").touch()
    (project_dir/"requirements.txt").touch()
    
    # create .gitignore and venv
    with open((project_dir/".gitignore"), mode="w") as f:
        f.write(
            "\n".join([
                "venv", "__pycache__", ".vscode"
            ])
        )
    
    # create venv and make the first commit
    # subprocess.run(["git", "-C", projectname, "init"])
    # subprocess.run(["git", "-C", projectname, "add", "."])
    # subprocess.run(["git", "-C", projectname, "commit", "-m", "Initial commit"])
    cmds = [
        ["python", "-m", "venv", f"{project_dir}/venv"],
        
        ["git", "-C", projectname, "init"],                             # -C initializes a new Git repository in the specified directory (carautomation).
        ["git", "-C", projectname, "add", "."],
        ["git", "-C", projectname, "commit", "-m", "Initial commit"],
        
        # create a task on our task manager
        # ["task", "add", f"Write documentation for {projectname}"]
    ]
    
    for cmd in cmds:
        try:
            subprocess.run(cmd, check=True, timeout=60)
        except FileNotFoundError as exc:
            print(f"The program that you're trying to launch cannot be found")
        except subprocess.CalledProcessError as exc:
            print(f"Command failed with a non-zero exit status.\n{exc}")
        except subprocess.TimeoutExpired as exc:
            print(f"Command timed out.\n{exc}")
            


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--project_name", '-p', type=str)   # --project_name AND -p have the same functionality (just one is shorter)
    parser.add_argument("--add_task", action="store_true")       
    args = parser.parse_args()
    print(args)
    
    project_starter(args.project_name)