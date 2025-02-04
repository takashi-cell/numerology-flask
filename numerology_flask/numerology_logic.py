import re

num_meanings = {
    1: "男性数。独立。\n強い意志と行動力を持ち、目標に向かって進む能力がある。\n組織やグループを率いる役割を果たすことが多い。",
    2: "女性数。サポート・バックアップ。\n協調性があり、人と調和を築くことが得意。\n感受性が豊かで、人の気持ちを理解し、サポートできる。",
    3: "子供数。わくわく楽しく。\n創造的で表現力があり、芸術やコミュニケーションが得意。\n楽しさを追求し、明るい性格で人を惹きつける力を持つ。",
    4: "固定数。コツコツ堅実に裏どりして動く。貯金好き。新しい事はあまりやりたがらない。\n真面目で努力家。物事を継続する力があり、安定した基盤を築く。\n現実的な考え方が得意で、コツコツと成長できる。",
    5: "移動数。いろんな所に行きたい。派手好き。\n好奇心が旺盛で、自由な発想を持ち、変化を楽しむ性格。\n新しい環境に適応する力が強く、多くの経験を積むことで成長できる。",
    6: "家族数。家族仲良く。パートナーシップ、仲間と一緒。\n愛情深く、家庭やコミュニティを大切にする。\n責任感が強く、人を支える役割を果たすことが多い。",
    7: "職人数。一点突破。一つの事を探求する。\n知的で探求心が強く、スピリチュアルな成長を求める。\n直感力が鋭く、深く考えることが好き。",
    8: "八方広がり数。営業職、成功数。完成を意味する。\n成功志向が強く、物質的豊かさやリーダーシップを持つ。\n実業家や組織のリーダーとして活躍できる。",
    9: "ギフト数。完成したものを伝える。教える。\n博愛精神があり、人道的な活動に適している。\n自己犠牲の精神が強く、多くの人に貢献できる。",
    11: "直感力が鋭く、精神的なリーダーやインスピレーションの源となる。\nカリスマ性があり、人を導く力が強い。",
    22: "強い現実化能力を持ち、大きな目標を実現する。\n壮大なビジョンを持ち、社会に大きな影響を与える可能性がある。",
    33: "無条件の愛を持ち、他者の幸福を第一に考える。\n人々を癒し、導く力を持つ。"
}

def reduce_to_single_digit(n):
    while n > 9 and n not in {11, 22, 33}:  # マスター数を考慮
        n = sum(int(digit) for digit in str(n))
    return n

def calculate_life_path_number(birthdate):
    return reduce_to_single_digit(sum(int(d) for d in birthdate if d.isdigit()))

def calculate_birth_day_number(birthdate):
    day = int(birthdate[-2:])  # 日付部分を取得
    return reduce_to_single_digit(day)

def calculate_birth_month_number(birthdate):
    month = int(birthdate[4:6])  # 月部分を取得
    return reduce_to_single_digit(month)

def calculate_birth_year_number(birthdate):
    year = int(birthdate[:4])  # 年部分を取得
    return reduce_to_single_digit(year)

def calculate_numerology(birthdate):
    life_path = calculate_life_path_number(birthdate)
    birth_day = calculate_birth_day_number(birthdate)
    birth_month = calculate_birth_month_number(birthdate)
    birth_year = calculate_birth_year_number(birthdate)
    
    return {
        "life_path": {"number": life_path, "meaning": num_meanings.get(life_path, "意味が見つかりません")},
        "past_number": {"number": birth_day, "meaning": num_meanings.get(birth_day, "意味が見つかりません")},
        "future_number": {"number": birth_month, "meaning": num_meanings.get(birth_month, "意味が見つかりません")},
        "year_number": {"number": birth_year, "meaning": num_meanings.get(birth_year, "意味が見つかりません")}
    }
