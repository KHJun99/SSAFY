"""
이미 생성된 PDF 파일에 OCR을 적용하는 스크립트
기존 PDF를 검색 가능하게 만듭니다!
"""

import subprocess
import os
import sys


def add_ocr_to_pdf(input_pdf, output_pdf, language='kor+eng'):
    """
    기존 PDF에 OCR 레이어 추가
    
    Args:
        input_pdf: 입력 PDF 파일
        output_pdf: 출력 PDF 파일 (OCR 적용됨)
        language: OCR 언어 (기본: 한글+영어)
    """
    
    print("=" * 70)
    print("📄 PDF에 OCR 적용하기")
    print("=" * 70)
    print()
    print(f"입력 파일: {input_pdf}")
    print(f"출력 파일: {output_pdf}")
    print(f"OCR 언어: {language}")
    print()
    
    # 파일 존재 확인
    if not os.path.exists(input_pdf):
        print(f"❌ 파일을 찾을 수 없습니다: {input_pdf}")
        return False
    
    # ocrmypdf 설치 확인
    print("🔍 ocrmypdf 확인 중...")
    try:
        result = subprocess.run(['ocrmypdf', '--version'], 
                              capture_output=True, text=True)
        print(f"✅ ocrmypdf 설치됨: {result.stdout.strip()}")
        print()
    except FileNotFoundError:
        print("❌ ocrmypdf가 설치되어 있지 않습니다!")
        print()
        print("📦 설치 방법:")
        print()
        print("   [Ubuntu/Debian]")
        print("   sudo apt-get update")
        print("   sudo apt-get install ocrmypdf tesseract-ocr-kor")
        print()
        print("   [Mac]")
        print("   brew install ocrmypdf")
        print()
        print("   [Windows]")
        print("   WSL(Windows Subsystem for Linux)에서:")
        print("   sudo apt-get install ocrmypdf tesseract-ocr-kor")
        print()
        return False
    
    # Tesseract 한글 팩 확인
    print("🔍 Tesseract 한글 팩 확인 중...")
    try:
        result = subprocess.run(['tesseract', '--list-langs'], 
                              capture_output=True, text=True)
        if 'kor' in result.stdout:
            print("✅ 한글 언어 팩 설치됨")
        else:
            print("⚠️  한글 언어 팩이 없습니다!")
            print("   설치: sudo apt-get install tesseract-ocr-kor")
            print("   계속 진행하지만 한글 인식이 안 될 수 있습니다.")
    except:
        pass
    print()
    
    # OCR 적용
    print("🔤 OCR 적용 중...")
    print("⏳ 시간이 걸릴 수 있습니다. 기다려주세요...")
    print()
    
    cmd = [
        'ocrmypdf',
        '--language', language,
        '--output-type', 'pdf',
        '--skip-text',  # 기존 텍스트는 건너뛰기
        '--deskew',  # 기울기 보정
        '--rotate-pages',  # 회전 보정
        '--clean',  # 이미지 정리
        '--optimize', '1',  # 최적화
        '--jobs', '4',  # 병렬 처리 (4개 동시)
        '--progress-bar',  # 진행률 표시
        input_pdf,
        output_pdf
    ]
    
    try:
        # 실행
        result = subprocess.run(
            cmd,
            timeout=7200  # 최대 2시간
        )
        
        if result.returncode == 0:
            print()
            print("=" * 70)
            print("✅ 완료!")
            print("=" * 70)
            print()
            print(f"📁 검색 가능한 PDF: {output_pdf}")
            print()
            print("✨ 테스트:")
            print("   1. PDF 열기")
            print("   2. Ctrl+F 누르기")
            print("   3. 한글 검색 시도!")
            print()
            return True
        else:
            print()
            print("❌ OCR 적용 실패")
            print(f"   오류 코드: {result.returncode}")
            return False
            
    except subprocess.TimeoutExpired:
        print()
        print("❌ 시간 초과 (2시간)")
        return False
    except KeyboardInterrupt:
        print()
        print("❌ 사용자가 취소했습니다")
        return False
    except Exception as e:
        print()
        print(f"❌ 오류 발생: {e}")
        return False


def main():
    print()
    print("🎓 PDF OCR 추가 도구")
    print()
    
    # 입력 파일
    if len(sys.argv) > 1:
        input_pdf = sys.argv[1]
    else:
        input_pdf = input("입력 PDF 파일명: ").strip()
    
    # 출력 파일
    if len(sys.argv) > 2:
        output_pdf = sys.argv[2]
    else:
        # 기본 출력 파일명 생성
        name, ext = os.path.splitext(input_pdf)
        output_pdf = f"{name}_OCR적용{ext}"
        print(f"출력 파일명 (기본값: {output_pdf}): ", end='')
        user_output = input().strip()
        if user_output:
            output_pdf = user_output
    
    print()
    
    # OCR 적용
    success = add_ocr_to_pdf(input_pdf, output_pdf)
    
    if not success:
        print()
        print("💡 도움말:")
        print("   - ocrmypdf가 설치되어 있는지 확인하세요")
        print("   - Tesseract 한글 팩이 설치되어 있는지 확인하세요")
        print("   - 파일 경로가 정확한지 확인하세요")
        print()


if __name__ == "__main__":
    main()
