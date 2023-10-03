from math import ceil

def calc_account(m):
    # 実装は入れていません、自分で入れてください
    if m <= 0:
        return None
    elif m <= 1700:
        return 610
    else:
        additional_distance = m - 1700
        additional_fare = (additional_distance + 314) // 315 * 80  
        return 610 + additional_fare


if __name__ == "__main__":
    from argparse import ArgumentParser
    import sys

    parser = ArgumentParser(description="引数に金額を渡すとタクシー料金を計算します")
    parser.add_argument("distance", help="走行距離(メートル)", type=int)

    args = parser.parse_args()
    d = args.distance
    a = calc_account(d)
    if a == None:
        print("不正な数値です、1以上の整数値を渡してください", file=sys.stderr)
        sys.exit(1)
    print(f"走行距離 {args.distance}m => 金額は {calc_account(args.distance)}円です。")


