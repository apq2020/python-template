# Windows Python 学习型模板用法

这个模板旨在帮助你快速启动新的 Python 学习项目，通过 `cookiecutter` 一条命令完成安装，并提供了一些便捷的配置。

## 安装步骤

<<<<<<< HEAD
1.  **安装 `cookiecutter`**

    首先，你需要安装 `cookiecutter`。打开命令提示符或 PowerShell，运行以下命令：

    ```bash
    pip install cookiecutter
    ```

2.  **使用模板创建项目**

    在想要创建项目的目录下，运行以下命令：

    ```bash
    # 使用 gh: 前缀的简写形式
    cookiecutter gh:apq2020/python-template

    # 或者使用完整的 HTTPS URL
    cookiecutter https://github.com/apq2020/python-template.git
    ```

    根据提示，输入项目名称、描述等信息。

## VS Code 使用

1.  **选择 Python 解释器**

    -   按下 `Ctrl + Shift + P` 打开命令面板。
    -   输入 `Python: Select Interpreter` 并选择。
    -   选择项目中的 `.venv\Scripts\python.exe` 作为解释器。

2.  **删除项目虚拟环境时切换解释器**
    -   删除虚拟环境前，需要将 VS Code 的解释器切换为系统解释器。
    -   删除完毕，再切换回项目解释器。

3.  **一键运行当前 `python` 文件**
    -   按下 `Ctrl + Shift + P` 打开命令面板。
    -   选择 `Run current file` 选项
  
4.  **一键清除缓存文件**
    -   按下 `Ctrl + Shift + P` 打开命令面板。
    -   选择 `Clean Cache` 选项

享受你的 Python 学习之旅吧！

# Windows Python Learning Template Usage

This template is designed to help you quickly start new Python learning projects. It can be installed with a single `cookiecutter` command and includes several convenient configurations.

## Installation Steps

=======
>>>>>>> a964ed9 (feat: Add MIT License)
1.  **Install `cookiecutter`**

    First, you need to install `cookiecutter`. Open Command Prompt or PowerShell and run the following command:

    ```bash
    pip install cookiecutter
    ```

2.  **Create a project using the template**

    In the directory where you want to create your project, run the following command:

    ```bash
    # Using the shorthand gh: prefix
    cookiecutter gh:apq2020/python-template

    # Or using the full HTTPS URL
    cookiecutter https://github.com/apq2020/python-template.git
    ```

    Follow the prompts to enter your project name, description, and other information.

## VS Code Usage

1.  **选择 Python 解释器 (Select Python Interpreter)**

    -   Press `Ctrl + Shift + P` to open the command palette.
    -   Type `Python: Select Interpreter` and select it.
    -   Choose `.venv\Scripts\python.exe` in your project as the interpreter.

2.  **删除虚拟环境时切换解释器 (Switch interpreter when deleting venv)**
    -   Before deleting the virtual environment, you need to switch VS Code's interpreter to the system interpreter.
    -   After deletion, switch back to the project interpreter.

<<<<<<< HEAD
3.  **Run current `python` file with one click**
    -   Press `Ctrl + Shift + P` to open the command palette.
    -   Select the `Run current file` option

4.  **Clear cache files with one click**
    -   Press `Ctrl + Shift + P` to open the command palette.
    -   Select the `Clean Cache` option

=======
>>>>>>> a964ed9 (feat: Add MIT License)
Enjoy your Python learning journey!
