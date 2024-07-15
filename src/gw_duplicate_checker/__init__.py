import threading
from .config import IP_RANGE
from .main import periodic_scan, duplicate_check


def main():
    threading.Thread(target=periodic_scan, args=(IP_RANGE, 15 * 60)).start()
    threading.Thread(target=duplicate_check, args=(IP_RANGE, 5)).start()


if __name__ == "__main__":
    main()
