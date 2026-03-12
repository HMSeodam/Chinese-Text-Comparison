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
    """HTML 파일 경로를 찾는다. index.html 또는 실행.html을 시도한다."""
    if getattr(sys, 'frozen', False):
        # PyInstaller로 빌드된 경우
        base_dir = sys._MEIPASS
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))

    # 여러 가능한 파일명 시도
    possible_names = ['index.html', '실행.html', 'run.html']
    for name in possible_names:
        html_path = os.path.join(base_dir, name)
        if os.path.exists(html_path):
            return html_path
    
    # 파일을 찾지 못한 경우
    print(f"오류: HTML 파일을 찾을 수 없습니다.")
    print(f"다음 위치에서 찾았습니다: {base_dir}")
    print(f"다음 파일명을 시도했습니다: {', '.join(possible_names)}")
    sys.exit(1)


def main():
    try:
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
        # 실패 시 자동으로 다른 GUI 백엔드 시도
        try:
            webview.start(gui='edgechromium', debug=False)
        except Exception as e:
            print(f"EdgeChromium 로드 실패, 기본 GUI로 시도합니다: {e}")
            webview.start(debug=False)
    except Exception as e:
        print(f"프로그램 실행 중 오류가 발생했습니다: {e}")
        input("엔터를 눌러 종료하세요...")
        sys.exit(1)


if __name__ == '__main__':
    main()
