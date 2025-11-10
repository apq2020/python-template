import os
import shutil
import sys
from pathlib import Path

def find_project_root(marker="pyproject.toml"):
    """向上查找项目根目录（包含 .git 目录或 pyproject.toml 的地方）。"""
    current_path = Path(__file__).resolve()
    print("current_path: ", current_path)

def find_project_root(marker="pyproject.toml"):
    """向上查找项目根目录（包含 .git 目录或 pyproject.toml 的地方）。"""
    current_path = Path(__file__).resolve()

    for parent in current_path.parents:
        if (parent / marker).exists():
            return parent
    raise FileNotFoundError(f"Project root with '{marker}' not found.")

# --- 配置 ---
# 动态计算项目根目录
PROJECT_ROOT = find_project_root()

print("PROJECT_ROOT: ", PROJECT_ROOT)

# 需要删除的目录名
DIRS_TO_DELETE = ["__pycache__", ".pytest_cache"]

# 需要忽略的目录名，防止误删
DIRS_TO_IGNORE = {".venv", ".git", ".vscode", "build", "dist"}  # 使用集合进行更快的查找

from {{ cookiecutter.project_slug }}.utils import Fore, print_color_text


def main():
    """
    遍历项目目录，删除所有指定的缓存目录。
    """
    print_color_text(f"Starting cache cleanup in: {PROJECT_ROOT}", Fore.YELLOW)
    deleted_count = 0

    for root, dirs, _ in os.walk(PROJECT_ROOT, topdown=True):
        # 关键：从遍历列表中移除要忽略的目录，os.walk 就不会进入这些目录
        dirs[:] = [
            d for d in dirs if d not in DIRS_TO_IGNORE and Path(root, d).is_dir()
        ]

        for dir_name in dirs:
            if dir_name in DIRS_TO_DELETE:
                dir_path = Path(root) / dir_name
                print_color_text(f"Deleting: {dir_path}", Fore.RED)
                shutil.rmtree(dir_path)
                deleted_count += 1

    print_color_text(
        f"\nCleanup complete. Deleted {deleted_count} cache directories.", Fore.GREEN
    )


if __name__ == "__main__":
    main()
