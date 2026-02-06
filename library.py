"""
Library Management System
작성일: 2026-02-06
설명: 상속과 다형성을 활용한 도서 관리 프로그램. 
__slots__를 통한 메모리 최적화와 타입 힌트를 적용한 객체 지향 구조 실습용.
"""

from typing import List

class Item:
    # 인스턴스별 메모리 사용량을 줄이기 위한 슬롯 설정
    __slot__ = ["_title", "_author"]

    def __init__(self, title: str, author: str):
        """도서관 아이템의 공통 속성(제목, 저자) 초기화"""
        self._title = title
        self._author = author

    def display_info(self):
        """아이템의 기본 정보 출력 (자식 클래스에서 확장해서 사용)"""
        return f"책 제목 : {self._title}, 책 저자 : {self._author}"
    
class Book(Item):
    # 부모 클래스의 슬롯에 ISBN 속성 추가
    __slot__ = ["_isbn"]

    def __init__(self, title: str, author: str, isbn: int):
        """부모 생성자 호출 후 종이책 전용 속성인 ISBN 설정"""
        super().__init__(title, author)
        self._isbn = isbn

    def display_info(self):
        """기본 정보에 도서번호(ISBN)를 추가로 결합"""
        item_msg = super().display_info()
        return f"{item_msg}, 도서번호 : {self._isbn} "

class EBook(Item):
    # 부모 클래스의 슬롯에 파일 크기 속성 추가
    __slot__ = ["_file_size"]

    def __init__(self, title: str, author: str, file_size: int):
        """부모 생성자 호출 후 전자책 전용 속성인 파일 크기 설정"""
        super().__init__(title, author)
        self._file_size = file_size

    def display_info(self):
        """기본 정보에 파일크기 정보를 추가로 결합"""
        item_msg = super().display_info()
        return f"{item_msg}, 파일크기 : {self._file_size} "

class Library:
    def __init__(self):
        """도서 객체들을 저장할 리스트 초기화"""
        self._items: List[Item] = []
    
    def add_item(self, item: Item):
        """
        도서관에 새로운 아이템 추가.
        isinstance를 사용해 Item 클래스나 그 자식 객체인지 검증함.
        """
        if isinstance(item, Item):
            self._list.append(item)
        else:
            print("오류: Item 타입의 객체만 추가할 수 있습니다.")

    def show_all_items(self):
        """리스트에 저장된 모든 도서의 정보를 루프를 돌며 출력"""
        for lib in self._list:
            print(f'{lib.display_info()}')