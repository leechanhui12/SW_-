# feture-a branch
def check_spam(text: str) -> tuple:
    text = text.lower().strip()
    
    # 수정된 부분: 빈 문자열일 경우 "undefined"와 0을 반환하도록 변경
    if text == "":
        return "undefined", 0
    
    spam_keywords = [
        "free", "win", "winner", "prize", "click",
        "buy now", "urgent", "cash", "money", "offer", "deal", "bonus" , "limited", "guarantee", "coupang"
    ]

    hit = 0
    for kw in spam_keywords:
        print(kw, text)
        if kw in text:
            hit += 1
            
    return "Spaaam" if hit >= 2 else "Haaam", hit