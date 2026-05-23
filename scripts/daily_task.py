import random
import datetime
import os

FRUITS_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "fruits.txt")
LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "daily_log.txt")


def read_fruits():
    with open(FRUITS_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def pick_fruit_of_the_day(fruits):
    return random.choice(fruits)


def append_log(date, fruit):
    entry = f"{date} | 今日水果: {fruit}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)
    return entry


def main():
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
    date_str = now.strftime("%Y-%m-%d %H:%M:%S")

    fruits = read_fruits()
    fruit_of_the_day = pick_fruit_of_the_day(fruits)

    entry = append_log(date_str, fruit_of_the_day)

    print(f"=== 每日水果报告 ===")
    print(f"日期: {date_str}")
    print(f"水果列表: {', '.join(fruits)}")
    print(f"今日水果: {fruit_of_the_day}")
    print(f"已写入日志: {entry.strip()}")


if __name__ == "__main__":
    main()
