import os
import subprocess
import sys


def run_command(command, message):
    """Runs a command and prints a message."""
    print(f"🚀 {message}...")
    try:
        # Using shell=True for Windows compatibility with commands like 'git'
        subprocess.run(command, check=True, shell=True, capture_output=True, text=True)
        print("✅ Done.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e.stderr}")
        sys.exit(1)


def main():
    """
    This script runs after the project is generated.
    It initializes a git repository and creates a virtual environment.
    """

    # --- Initialize Git Repository ---
    if "{{ cookiecutter.create_git_repo }}" == "yes":
        run_command("git init", "Initializing Git repository")
        run_command("git add .", "Staging all files")
        run_command(
            'git commit -m "Initial commit from cookiecutter template"',
            "Creating initial commit",
        )

    # --- Create Virtual Environment and Install Dependencies ---
    if "{{ cookiecutter.create_venv_and_install }}" == "yes":
        # Find the python executable to create the venv
        python_executable = sys.executable or "python"

        run_command(
            f'"{python_executable}" -m venv .venv',
            "Creating virtual environment (.venv)",
        )

        # Determine the correct pip path based on OS
        if sys.platform == "win32":
            pip_executable = os.path.join(".venv", "Scripts", "pip")
        else:
            pip_executable = os.path.join(".venv", "bin", "pip")

        run_command(
            f'"{pip_executable}" install -r requirements.txt',
            "Installing dependencies from requirements.txt",
        )

    print("\n🎉 Project '{{ cookiecutter.project_name }}' is ready! 🎉")


if __name__ == "__main__":
    main()