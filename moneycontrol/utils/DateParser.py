from datetime import datetime
# from time import strptime


def parse_date(datetime_string):
    return datetime.strptime(datetime_string, "%B %d, %Y/ %I:%M %p %Z").__str__()


if __name__ == "__main__":
    out = parse_date("APRIL 02, 2021 / 04:39 PM IST")
    print(out)
