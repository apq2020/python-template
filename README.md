# Python Cookiecutter Template for VS Code on Windows

这个模板旨在帮助你快速启动新的 Python 学习项目，通过 `cookiecutter` 一条命令完成安装，并提供了一些便捷的配置。

This template is designed to help you quickly start new Python learning projects. It can be installed with a single `cookiecutter` command and includes several convenient configurations optimized for Windows and VS Code.

## 安装步骤

1.  **安装 `cookiecutter`**

    打开命令提示符或 PowerShell，运行以下命令：
    (Open Command Prompt or PowerShell and run the following command:)

    ```bash
    pip install cookiecutter
    ```

2.  **使用模板创建项目 (Create a project using the template)**

    在想要创建项目的目录下，运行以下命令：
    (In the directory where you want to create your project, run the following command:)

    ```bash
    # 使用 gh: 前缀的简写形式
    cookiecutter gh:apq2020/python-template
    ```

    根据提示，输入项目名称、描述等信息。 (Follow the prompts to enter your project name, description, and other information.)

## VS Code 使用 (VS Code Usage)

1.  **选择 Python 解释器 (Select Python Interpreter)**

    -   按下 `Ctrl + Shift + P` 打开命令面板。
    -   输入 `Python: Select Interpreter` 并选择。
    -   选择项目中的 `.venv\Scripts\python.exe` 作为解释器。

2.  **使用内置任务 (Use Built-in Tasks)**

    -   按下 `Ctrl + Shift + P` 打开命令面板。
    -   输入 `Tasks: Run Task` 并选择。
    -   你可以找到 `Run current file`, `Clean Cache`, `Format & Lint Project` 等许多有用的任务。

享受你的 Python 学习之旅吧！
(Enjoy your Python learning journey!)
