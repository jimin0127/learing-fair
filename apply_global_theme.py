BACKGROUND_COLOR = "#FFF8E4"  # 아주 연한 민트
PRIMARY_COLOR = "#85B788"     # 포인트 (버튼 등)
TEXT_COLOR = "#1F2B2E"        # 딥 그레이
HOVER_COLOR = "#255E4D"
CARD_BG_COLOR = "#ffffff"     # 카드용
BORDER_COLOR = "#CCE3D3"      # 구분선

def apply_global_theme(app):
    app.setStyleSheet(f"""
        QWidget {{
            background-color: {BACKGROUND_COLOR};
            color: {TEXT_COLOR};
            font-family: 'Pretendard', 'Noto Sans KR', sans-serif;
            font-size: 14px;
        }}

        QLabel {{
            font-size: 14px;
        }}

        QPushButton {{
            background-color: {PRIMARY_COLOR};
            color: white;
            padding: 8px 12px;
            border-radius: 6px;
            font-weight: bold;
        }}

        QPushButton:hover {{
            background-color: {HOVER_COLOR};
        }}

        QLineEdit, QComboBox, QSpinBox {{
            background-color: white;
            border: 1px solid {BORDER_COLOR};
            border-radius: 4px;
            padding: 4px;
        }}

        QListWidget {{
            background-color: white;
            border: 1px solid {BORDER_COLOR};
        }}
        
        QLabel#headerLabel {{
            font-size: 15px;
            font-weight: bold;
        }}
        
        QLabel#nameLabel {{
            font-size: 18px;
            font-weight: bold;
            margin: 4px 0px;
        }}
        QLabel#brandLabel {{
            font-size: 13px;
            color: #555;
            margin: 4px 0px;
        }}
    """)
