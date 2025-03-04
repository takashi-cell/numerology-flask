import re

num_meanings = {
    1: "男性数。独立。\n強い意志と行動力を持ち、目標に向かって進む能力がある。",
    2: "女性数。サポート・バックアップ。\n協調性があり、人と調和を築くことが得意。",
    3: "子供数。わくわく楽しく。\n創造的で表現力があり、芸術やコミュニケーションが得意。",
    4: "固定数。コツコツ堅実に動く。貯金好き。\n真面目で努力家。物事を継続する力がある。",
    5: "移動数。いろんな所に行きたい。派手好き。\n好奇心が旺盛で、変化を楽しむ。",
    6: "家族数。家族仲良く。パートナーシップ。\n愛情深く、責任感が強い。",
    7: "職人数。一点突破。\n知的で探求心が強く、スピリチュアルな成長を求める。",
    8: "八方広がり数。成功数。\nリーダーシップがあり、実業家向き。",
    9: "ギフト数。完成したものを伝える。\n人道的な活動に適している。",
    11: "直感力が鋭く、精神的リーダー。\n人を導く力が強い。",
    22: "現実化能力を持ち、大きな目標を実現する。\n社会に大きな影響を与える。",
    33: "無条件の愛を持ち、他者の幸福を第一に考える。\n人々を癒し、導く力を持つ。"
}

def reduce_to_single_digit(n):
    """1桁になるまで足し続ける。ただし11, 22, 33は保持する"""
    while n > 9 and n not in {11, 22, 33}:
        n = sum(int(d) for d in str(n))  
    return n

def calculate_life_path_number(birthdate):
    return reduce_to_single_digit(sum(int(d) for d in birthdate if d.isdigit()))

def calculate_birth_day_number(birthdate):
    day = int(birthdate[-2:])
    return day if day in {11, 22} else reduce_to_single_digit(day)

def calculate_future_number(birthdate):
    """未来数を計算する（誕生月と誕生日の数字を1桁ずつに分解して合計し、1桁にする）"""
    try:
        # ハイフンを除去
        clean_birthdate = birthdate.replace("-", "")

        # 誕生月・誕生日の部分を取得（例: "20241222" → "12" と "22"）
        month_digits = [int(d) for d in clean_birthdate[4:6]]  # 誕生月を各桁に分解
        day_digits = [int(d) for d in clean_birthdate[6:8]]    # 誕生日を各桁に分解
        total = sum(month_digits + day_digits)  # すべての桁を合計

        # 🔴 デバッグ出力
        print(f"DEBUG: 修正後の誕生日 {clean_birthdate}, 誕生月の桁 {month_digits}, 誕生日の桁 {day_digits}, 合計 {total}")

        return reduce_to_single_digit(total)
    except (ValueError, IndexError):
        print("ERROR: 誕生日の取得に失敗しました")
        print(f"DEBUG: 受け取った誕生日 {birthdate}")
        return None  # エラー防止

def calculate_birth_year_number(birthdate):
    year = int(birthdate[:4])
    return reduce_to_single_digit(year)

def calculate_numerology(birthdate):
    life_path = calculate_life_path_number(birthdate)
    birth_day = calculate_birth_day_number(birthdate)
    birth_month = calculate_future_number(birthdate)  # 修正
    birth_year = calculate_birth_year_number(birthdate)

    # デバッグ出力
    print("DEBUG: 誕生日 =", birthdate)
    print("DEBUG: 過去数 =", birth_day)
    print("DEBUG: 未来数 =", birth_month)
    print("DEBUG: 誕生年数 =", birth_year)

    # 過去数が 11 の場合、2 の特性も含める
    if birth_day == 11:
        past_number_meaning = f"{num_meanings[11]}\n\n※11 は 2 の特性も併せ持ちます。\n\n{num_meanings[2]}"
    # 過去数が 22 の場合、4 の特性も含める
    elif birth_day == 22:
        past_number_meaning = f"{num_meanings[22]}\n\n※22 は 4 の特性も併せ持ちます。\n\n{num_meanings[4]}"
    else:
        past_number_meaning = num_meanings.get(birth_day, "意味が見つかりません")

    return {
        "life_path": {"number": life_path, "meaning": num_meanings.get(life_path, "意味が見つかりません")},
        "past_number": {"number": birth_day, "meaning": past_number_meaning},
        "future_number": {"number": birth_month, "meaning": num_meanings.get(birth_month, "意味が見つかりません")},
        "year_number": {"number": birth_year, "meaning": num_meanings.get(birth_year, "意味が見つかりません")}
    }