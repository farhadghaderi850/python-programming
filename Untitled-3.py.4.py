def sec_to_HMS(seconds):
    hours = seconds // 3600
    seconds_left = seconds % 3600
    minutes = seconds_left % 60
    seconds_left = seconds_left % 60
    return hours, minutes, seconds_left
def main():
    input_seconds = int(input("Enter seconds : "))
    hours, minutes, seconds = sec_to_HMS(input_seconds)
    print(f"{input_seconds} seconds is equal to {hours} hours, {minutes} minutes and {seconds} seconds. ")
main()