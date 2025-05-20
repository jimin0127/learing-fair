# 헌옷줄게 새옷다오

**지구를 위한 착한 쇼핑!**  
헌 옷을 반환하면 새 옷을 할인된 가격으로 구매할 수 있는 친환경 GUI 애플리케이션입니다.  
`PySide6` 기반으로 제작되었으며, 직관적인 UI로 누구나 쉽게 사용할 수 있어요.

---

## ✅ 주요 기능

- 카테고리별 상품 조회
- 이전에 구매한 옷 반납 시 자동 할인 적용
- 주문서 작성
- 주문 완료 화면 및 주문 내역 검색 기능 제공

---

## 📁 프로젝트 구조

```
📦your_project/
 ┣ 📂assets/               # 이미지 리소스
 ┣ 📂service/              # 데이터 처리 로직
 ┣ 📂userInterface/        # 화면 구성 UI 모듈
 ┣ 📂util/                 # 유틸리티 함수 (포맷 등)
 ┣ 📜ProductData.csv       # 상품 정보 CSV
 ┣ 📜BoughtProductData.csv # 주문 내역 CSV
 ┣ 📜main.py               # 앱 실행 메인
 ┗ 📜README.md             # 실행 가이드
```

---

## 🚀 실행 방법

### 1. 패키지 설치 방법
1. **Python 3.9+ 환경 준비**
2. **필수 패키지 설치**

```
pip install PySide6
```

3. **앱 실행**

```
python main.py
```

### 2. exe 다운 실행 방법
- [Github source 코드 action 주소](https://github.com/jimin0127/learing-fair/actions)로 이동
- 가장 최근 Workflow Action 의 exe 다운로드
- 압축 해제 후 실행

---

## 🧪 개발자용 팁

- `ProductData.csv`: ID, 이름, 브랜드, 가격, 이미지 경로 등 기본 상품 정보
- `BoughtProductData.csv`: 반납 가능한 헌옷 정보 (할인 계산에 사용됨)
- UI 커스터마이징은 `userInterface` 하위 모듈에서 가능
