from daikin_notifier.api import is_needed_water
from daikin_notifier.history import already_notified, delete_history, save_history
from daikin_notifier.line import send_message


def main():
    is_needed = is_needed_water
    if not is_needed:
        print("Water need not to be supplied")
        delete_history()
        return

    print("Water should be supplied")
    if already_notified():
        print("Already Notified")
    else:
        # 未通知
        send_message("給水が必要です")
        save_history()
        return


if __name__ == "__main__":
    main()
