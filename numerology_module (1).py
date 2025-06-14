
from datetime import datetime

def simplify(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

def birthday_digits_sum(date_str):
    return sum(int(c) for c in date_str if c.isdigit())

def calculate_age(birthdate_str):
    birth = datetime.strptime(birthdate_str, "%Y/%m/%d")
    today = datetime.today()
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    return age

def calculate_flow_year_fixed(date_str):
    y, m, d = date_str.split('/')
    month = int(m)
    day = int(d)
    now_year = datetime.today().year
    year_sum = sum(int(i) for i in str(now_year))
    month_day_sum = sum(int(i) for i in f"{month:02d}{day:02d}")
    flow_year = year_sum + month_day_sum
    while flow_year > 9:
        flow_year = sum(int(d) for d in str(flow_year))
    return flow_year

flow_year_data = {
    1: {"關鍵詞": "開始", "機遇": "勇敢開局、創造機會、邁出第一步", "挑戰": "開局不利、缺乏明確目標"},
    2: {"關鍵詞": "溝通", "機遇": "建立關係、貴人來幫忙", "挑戰": "猶豫不決、被人影響、拖延"},
    3: {"關鍵詞": "行動", "機遇": "抓住機會、快速突破", "挑戰": "衝動做錯、情緒波動大"},
    4: {"關鍵詞": "策劃", "機遇": "專注學習、累積能量", "挑戰": "想太多、擔心過頭、不執行"},
    5: {"關鍵詞": "轉折", "機遇": "蛻變轉型、打開新局", "挑戰": "被困住、阻礙多、拖累他人"},
    6: {"關鍵詞": "財富", "機遇": "財富機會到、收穫金錢", "挑戰": "錯誤投資、浪費、財務混亂"},
    7: {"關鍵詞": "人脈", "機遇": "結識貴人、拓展人際圈", "挑戰": "吸引小人、關係惡化"},
    8: {"關鍵詞": "權力", "機遇": "握有主導權、升官加薪機會", "挑戰": "壓力大、權責不清、被推責"},
    9: {"關鍵詞": "總結", "機遇": "完成階段性目標、圓滿結束", "挑戰": "被迫結束、收尾困難"}
}

def basic_analysis(date_str):
    digits_total = birthday_digits_sum(date_str)
    main_num = simplify(digits_total)
    age = calculate_age(date_str)
    flow_year = calculate_flow_year_fixed(date_str)
    flow_info = flow_year_data.get(flow_year, {})

    # 缺失數字（1~9 中，生日中沒出現的）
    appeared_digits = [int(d) for d in date_str if d.isdigit()]
    missing = sorted(set(range(1, 10)) - set(appeared_digits))
    appeared = sorted(set(appeared_digits) & set(range(1, 10)))

    return {
        "主性格數": main_num,
        "年紀": age,
        "流年": flow_year,
        "流年說明": flow_info,
        "出現數字": appeared,
        "缺失數字": missing
    }

def generate_13_codes(date_str):
    y, m, d = date_str.split('/')
    A = int(d[0])
    B = int(d[1])
    C = int(m[0])
    D = int(m[1])
    E = int(y[0])
    F = int(y[1])
    G = int(y[2])
    H = int(y[3])

    I = simplify(A + B)
    J = simplify(C + D)
    K = simplify(E + F)
    L = simplify(G + H)
    M = simplify(I + J)
    N = simplify(K + L)
    O = simplify(M + N)
    P = simplify(M + O)
    Q = simplify(N + O)
    R = simplify(Q + P)
    X = simplify(I + M)
    W = simplify(J + M)
    S = simplify(X + W)
    V = simplify(K + N)
    U = simplify(L + N)
    T = simplify(V + U)

    g1 = f"{I}{J}{M}"
    g2 = f"{K}{L}{N}"
    g3 = f"{M}{N}{O}"
    g4 = f"{M}{O}{P}"
    g5 = f"{N}{O}{Q}"
    g6 = f"{Q}{P}{R}"
    g7 = f"{I}{M}{X}"
    g8 = f"{J}{M}{W}"
    g9 = f"{X}{W}{S}"
    g10 = f"{K}{N}{V}"
    g11 = f"{L}{N}{U}"
    g12 = f"{V}{U}{T}"
    g3_digits = [int(d) for d in g3]
    g13 = ''.join(str(simplify(d + d)) for d in g3_digits)

    return {
        "g1": g1, "g2": g2, "g3": g3, "g4": g4, "g5": g5,
        "g6": g6, "g7": g7, "g8": g8, "g9": g9, "g10": g10,
        "g11": g11, "g12": g12, "g13": g13
    }

def five_elements_analysis(date_str):
    result = generate_13_codes(date_str)
    # 拿出與五行對應的 I~X 數值
    y, m, d = date_str.split('/')
    A = int(d[0])
    B = int(d[1])
    C = int(m[0])
    D = int(m[1])
    E = int(y[0])
    F = int(y[1])
    G = int(y[2])
    H = int(y[3])
    I = simplify(A + B)
    J = simplify(C + D)
    K = simplify(E + F)
    L = simplify(G + H)
    M = simplify(I + J)
    N = simplify(K + L)
    O = simplify(M + N)
    P = simplify(M + O)
    Q = simplify(N + O)
    R = simplify(Q + P)
    X = simplify(I + M)
    W = simplify(J + M)
    S = simplify(X + W)
    V = simplify(K + N)
    U = simplify(L + N)
    T = simplify(V + U)

    five_elements = {
        '金': [1, 6],
        '水': [2, 7],
        '火': [3, 8],
        '木': [4, 9],
        '土': [5]
    }

    count = {k: 0 for k in five_elements}
    variables = {'I': I, 'J': J, 'K': K, 'L': L, 'M': M, 'N': N,
                 'O': O, 'P': P, 'Q': Q, 'R': R, 'S': S, 'T': T,
                 'U': U, 'V': V, 'W': W, 'X': X}
    for var, value in variables.items():
        for element, nums in five_elements.items():
            if value in nums:
                count[element] += 1
    return count
