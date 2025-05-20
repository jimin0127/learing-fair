import sys
import os

def get_resource_path(relative_path: str) -> str:
    """
    PyInstaller 실행파일이든, 개발 중이든 리소스 경로를 안전하게 반환
    """
    if hasattr(sys, '_MEIPASS'):  # PyInstaller로 패킹된 경우
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)