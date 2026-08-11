# ==========================================
# 1. 데이터 영역
# ==========================================
# prompts는 프롬프트들을 저장해두는 목록입니다.
# 프로그램이 시작될 때 기본 프롬프트 3개가 들어 있습니다.

import json
import os

FILE_NAME = "prompts.json"


default_prompts = [
    {
        "title": "동영상 생성",
        "category": "Gemini omni로 동영상 생성",
        "content": "첨부한 사진을 일본 애니메이션 스타일의 짧은 영상으로 변환해줘.",
        "favorite": False
    },
    {
        "title": "블로그 글 작성",
        "category": "글쓰기",
        "content": "다음 주제를 바탕으로 독자가 이해하기 쉬운 블로그 글을 작성해줘.",
        "favorite": False
    },
    {
        "title": "코드 설명",
        "category": "프로그래밍",
        "content": "다음 코드를 초보자도 이해할 수 있도록 단계별로 쉽게 설명해줘.",
        "favorite": False
    }
]

def save_prompts():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(prompts, file, ensure_ascii=False, indent=4)


def load_prompts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        return default_prompts


prompts = load_prompts()


# ==========================================
# 2. 메뉴 출력 함수
# ==========================================

def show_menu():
    print("\n===== 프롬프트 관리 프로그램 =====")
    print("1. 새 프롬프트 추가")
    print("2. 전체 프롬프트 보기")
    print("3. 카테고리별 프롬프트 보기")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 추가/해제")
    print("0. 프로그램 종료")


# ==========================================
# 3. 프롬프트 추가 기능
# ==========================================

def add_prompt():
    print("\n===== 프롬프트 추가 =====")

    title = input("제목을 입력하세요: ")
    category = input("카테고리를 입력하세요: ")
    content = input("내용을 입력하세요: ")

    new_prompt = {
        "title": title,
        "category": category,
        "content": content,
        "favorite": False
    }

    prompts.append(new_prompt)
    save_prompts()
    print("프롬프트가 추가되었습니다.")


# ==========================================
# 4. 프롬프트 목록 보기 기능
# ==========================================

def show_list():
    print("\n===== 프롬프트 목록 =====")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        if prompt["favorite"] == True:
            favorite_mark = "★"
        else:
            favorite_mark = " "

        print(f"{index}. {favorite_mark} {prompt['title']} [{prompt['category']}]")


# ==========================================
# 5. 카테고리별 조회 기능
# ==========================================

def search_by_category():
    print("\n===== 카테고리별 조회 =====")

    category = input("조회할 카테고리를 입력하세요: ")

    print(f"\n===== {category} 카테고리 결과 =====")

    found = False

    for index, prompt in enumerate(prompts, start=1):
        if prompt["category"] == category:
            print(f"{index}. {prompt['title']}")
            found = True

    if found == False:
        print("해당 카테고리의 프롬프트가 없습니다.")


# ==========================================
# 6. 검색 기능
# ==========================================

def search_prompt():
    print("\n===== 프롬프트 검색 =====")

    keyword = input("검색할 제목 또는 내용을 입력하세요: ")

    print("\n===== 검색 결과 =====")

    found = False

    for index, prompt in enumerate(prompts, start=1):
        title = prompt["title"]
        category = prompt["category"]
        content = prompt["content"]

        if keyword in title or keyword in category or keyword in content:
            print(f"{index}. {prompt['title']} [{prompt['category']}]")
            found = True

    if found == False:
        print("해당 검색어와 일치하는 프롬프트가 없습니다.")


# ==========================================
# 7. 상세 보기 기능
# ==========================================

def show_detail():
    print("\n===== 상세 보기 =====")

    show_list()

    number = input("상세 보기할 번호를 입력하세요: ")

    if not number.isdigit():
        print("숫자를 입력해야 합니다.")
        return

    number = int(number)

    if number < 1 or number > len(prompts):
        print("존재하지 않는 번호입니다.")
        return

    prompt = prompts[number - 1]

    print("\n===== 상세 정보 =====")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"내용: {prompt['content']}")

    if prompt["favorite"] == True:
        print("즐겨찾기: 예")
    else:
        print("즐겨찾기: 아니오")


# ==========================================
# 8. 즐겨찾기 변경 기능
# ==========================================

def toggle_favorite():
    print("\n===== 즐겨찾기 변경 =====")

    show_list()

    number = input("즐겨찾기 변경할 번호를 입력하세요: ")

    if not number.isdigit():
        print("숫자를 입력해야 합니다.")
        return

    number = int(number)

    if number < 1 or number > len(prompts):
        print("존재하지 않는 번호입니다.")
        return

    prompt = prompts[number - 1]

    prompt["favorite"] = not prompt["favorite"]

    if prompt["favorite"] == True:
        print("즐겨찾기에 추가되었습니다.")
    else:
        print("즐겨찾기가 해제되었습니다.")


# ==========================================
# 9. 프로그램 실행부
# ==========================================

while True:
    show_menu()

    menu = input("메뉴 번호를 입력하세요 (0~6): ")

    if menu == "1":
        add_prompt()

    elif menu == "2":
        show_list()

    elif menu == "3":
        search_by_category()

    elif menu == "4":
        search_prompt()

    elif menu == "5":
        show_detail()

    elif menu == "6":
        toggle_favorite()

    elif menu == "0":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 메뉴입니다. 다시 선택하세요.")

