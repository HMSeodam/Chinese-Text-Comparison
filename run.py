"""
한문 텍스트 교감기 (Classical Chinese Text Collator)
Windows GUI Launcher - pywebview 기반

사용법:
  pip install pywebview
  python run.py
"""

import os
import sys
import webview


def get_html_path():
    """index.html 경로를 찾는다."""
    if getattr(sys, 'frozen', False):
        # PyInstaller로 빌드된 경우
        base_dir = sys._MEIPASS
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))

    html_path = os.path.join(base_dir, 'index.html')
    if not os.path.exists(html_path):
        print(f"오류: index.html 파일을 찾을 수 없습니다: {html_path}")
        sys.exit(1)
    return html_path


def main():
    html_path = get_html_path()
    file_url = f'file:///{html_path.replace(os.sep, "/")}'

    window = webview.create_window(
        title='漢文 텍스트 교감기',
        url=file_url,
        width=1000,
        height=750,
        resizable=True,
        min_size=(600, 400),
    )

    # Windows에서는 mshtml(IE) 대신 EdgeChromium 사용 시도
    webview.start(gui='edgechromium', debug=False)


if __name__ == '__main__':
    main()
