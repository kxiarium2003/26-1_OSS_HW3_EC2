# OSS HW3 - EC2 배포 실습

본 프로젝트는 오픈소스소프트웨어실습 과제로, Streamlit 애플리케이션을 AWS EC2 환경에 배포하고 외부 접속을 확인하는 실습입니다.

## 1. 과제 내용
- AWS Learner Lab EC2 환경 구축
- Streamlit 애플리케이션 배포 및 외부 접속 확인
- 배포 결과 데모 영상 제작

## 2. 프로젝트 구성 
사용자 인터페이스 및 데이터 처리를 위해 다음과 같은 파일들로 구성되어 있습니다.

- `app.py`: Streamlit 메인 실행 파일
- `logic.py`: 앱의 주요 비즈니스 로직 처리
- `data_loader.py`: 데이터 로딩 및 전처리
- `quiz_data.json`: 앱에서 사용하는 퀴즈 데이터
- `requirements.txt`: 필요한 라이브러리 목록 (Streamlit 등)

## 3. 실행 방법 
### 포트 및 네트워크 설정
- **기본 포트**: 본 애플리케이션은 Streamlit의 기본 포트인 `8501`을 사용합니다.
- **AWS 보안 설정**: EC2 인스턴스의 보안 그룹(Security Group) 내 인바운드 규칙에서 `TCP 8501` 포트를 모든 소스(`0.0.0.0/0`)에 대해 개방하여 외부 접속이 가능하도록 설정하였습니다.

### 패키지 설치
- EC2 인스턴스에 접속한 후, 아래 명령어를 통해 필요한 라이브러리를 설치합니다.  
- Ubuntu 24.04 이상의 환경에서 시스템 패키지 충돌을 방지하기 위해 아래 명령어를 사용합니다.
```bash
pip3 install -r requirements.txt --break-system-packages
```
### 앱 실행
```bash
python3 -m streamlit run app.py
```
## 4. 실시간 로그 모니터링
본 앱은 주요 상호작용 시 EC2 터미널에 실시간 로그를 출력하도록 설계되었습니다.
- 로그인 시: [LOG] Login Success: User '...'
- 퀴즈 제출 시: [LOG] Quiz Completed - Score: X/5

## 5. 배포 결과 확인 
- 데모 영상 링크: [26-1 OSS HW3 EC2 배포](https://www.youtube.com/watch?v=FwBdA4Wjcqc&list=PLY__K2b2YO5XVoNmlWsxbeYwUJRxm8-JH&index=2)