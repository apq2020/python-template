import sys
from colorama import Fore, Style, init

# 初始化 colorama（延迟到首次调用时）
_colorama_initialized = False


def _ensure_colorama_init():
    global _colorama_initialized
    if not _colorama_initialized:
        init(autoreset=True, strip=False)
        _colorama_initialized = True


def print_color_text(text, color=Fore.WHITE, file=sys.stdout, end='\n'):
    """
    高效的彩色文本打印函数
    
    Args:
        text: 要打印的文本
        color: 颜色代码，默认白色 (Fore.RED, Fore.GREEN, Fore.BLUE 等)
        file: 输出流，默认 stdout
        end: 结尾字符，默认换行
    
    示例:
        print_color_text("错误信息", Fore.RED, sys.stderr)
        print_color_text("成功", Fore.GREEN)
    """
    _ensure_colorama_init()
    print(f"{color}{text}{Style.RESET_ALL}", file=file, end=end)