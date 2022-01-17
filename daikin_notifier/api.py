import os
from urllib import parse, request

ENDPOINT = os.getenv("DAIKIN_CLEANER_ENDPOINT")


def is_needed_water():
    url = parse.urljoin(ENDPOINT, "cleaner/get_unit_info")
    # http = urllib3.PoolManager()
    req = request.Request(url)
    with request.urlopen(req) as res:
        body = res.read()
    data = parse.unquote(str(body))

    for field in data.split(","):
        kv = field.split("=")
        if kv[0] == "water_supply":
            return kv[1] == "1"
    return None


if __name__ == "__main__":
    ret = is_needed_water()
    print(ret)
