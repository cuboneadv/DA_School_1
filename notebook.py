#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 노트 설계

class Note():
    def __init__(self, write = None): # 맨 처음 초기화해야 하므로 write = None
        self.write = write

    def write_function(self, write): # 쓰기 기능 추가
        self.write = write
    
    def remove_all(self): # (모두) 지우는 기능 추가
        self.write = ""
    
    def __str__(self): # 작성한 내용을 볼 수 있게 return 값 작성
        return self.write


# In[2]:


# 노트북 설계
# 1) 노트북의 제목
# 2) 페이지 수 
# 3) 노트를 저장

class NoteBook():

    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes = {} # 딕셔너리 형으로 선언, Note Page Number를 Key로 설정해서 쉽게 찾기 위함

    # 새로운 노트를 노트북에 추가하는 함수
    # 지금은 기본 기능만 추가했지만 실제 기능 구현 시 많은 것을 고려해야 함
    # 7페이지면 8페이지에 추가되는 형태로ㅜ 구현
    def add_note(self, note, page = 0):
        if self.page_number < 300:
            if page == 0:
                self.note[self.page_number] = note
                self.page_number += 1
            else:
                self.notes = {page : note}
                self.page_number += 1
        else:
            print("300페이지를 초과하여 추가할 수 없습니다")

    # 특정 페이지 번호에 있는 노트를 제거하는 함수
    # 딕셔너리의 Key가 있는지 확인함, 있다면 삭제하고, 없으면 사용해서 경고 문장을 출력하기
    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("삭제된 노트입니다.")
  
    # 현재 노트 페이지 출력
    def get_number_of_page(self):
        return len(self.notes.keys())

########## 실습 종료 ##########

