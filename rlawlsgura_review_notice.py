def check_review_eligibility(user_name, is_purchased):
    """
    사용자의 구매 여부에 따라 리뷰 작성 안내 메시지를 반환하는 함수
    """
    if is_purchased:
        return f"[{user_name}님] 상품 구매가 확인되었습니다. 리뷰를 작성하시면 500포인트가 적립됩니다!"
    else:
        return f"[{user_name}님] 상품 구매 내역이 없습니다. 리뷰 작성은 구매 확정 후 가능합니다."


# 서로 다른 입력 두 가지의 결과 출력
print("--- 리뷰 작성 안내 서비스 ---")

# 입력 1: 구매 확정 고객
result1 = check_review_eligibility(user_name="김철수", is_purchased=True)
print(f"입력 1 결과: {result1}")

# 입력 2: 미구매 고객
result2 = check_review_eligibility(user_name="이영희", is_purchased=False)
print(f"입력 2 결과: {result2}")