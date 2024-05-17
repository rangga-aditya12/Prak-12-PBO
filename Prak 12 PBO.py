import datetime
import pytz

def display_time_decorator(func):
    def wrapper():
        utc_now_before = datetime.datetime.now(pytz.utc)
        jakarta_tz = pytz.timezone('Asia/Jakarta')
        jakarta_now_before = utc_now_before.astimezone(jakarta_tz)

        print("\n=============================\nNama: Rangga Aditya Pradana\nNIM: 064002300026\n=============================")
        print(f"Timezone: {jakarta_tz.zone}")
        print(f"Tanggal: {jakarta_now_before.strftime('%Y-%m-%d')}")
        print(f"Waktu: {jakarta_now_before.strftime('%H:%M:%S.%f')}")

        func()

        utc_now_after = datetime.datetime.now(pytz.utc)
        jakarta_now_after = utc_now_after.astimezone(jakarta_tz)

        print("\nBerubah Menjadi:")
        print(f"Timezone: {jakarta_tz.zone}")
        print(f"Tanggal: {jakarta_now_after.strftime('%Y-%m-%d')}")
        print(f"Waktu: {jakarta_now_after.strftime('%H:%M:%S.%f')}")

    return wrapper

@display_time_decorator
def show_current_time():
    print(datetime.datetime.now(pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S.%f'))

if __name__ == "__main__":
    show_current_time()
