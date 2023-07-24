from datetime import date

today = date.today()

today_or_other = input("Today's date or other date? (Enter 'today' for today's date or a specific date in the format 'YYYY-MM-DD'): ")

if today_or_other == "today":
    end_date = today
elif len(today_or_other) > 1: 
    year, month, day = map(int, today_or_other.split('-'))
    end_date = date(year, month, day)
else:
    end_date = today


delta_date_tff = end_date - date(2023, 6, 8)
delta_date_ftmo = end_date - date.today()
#delta_date_ftmo = end_date - date(2024, 6, 8)
start_balance = 10000


def tff(scale=0.25, scale_time=90):
    if delta_date_tff.days <= scale_time:
        return start_balance
    else:
        return start_balance * (1 + scale) ** (delta_date_tff.days // scale_time)


def ftmo(scale=0.25, scale_time=120):
    if delta_date_ftmo.days <= scale_time:
        return start_balance
    else:
        return start_balance * (1 + scale) ** (delta_date_ftmo.days // scale_time)



  

def scale_balance():
  choice_input = input("Calculate for TFF or FTMO: ")
  if choice_input == "tff":
      tff_balance = tff()
      print(f"TFF Balance on {end_date}: {tff_balance}$")
  elif choice_input == "ftmo":
      ftmo_balance = ftmo()
      print(f"FTMO Balance on {end_date}: {ftmo_balance}$")
  else:
      print("Wrong input")


def save_payout_values(file_name, payout_values):
    with open(file_name, 'w') as file:
        for value in payout_values:
            file.write(str(value) + '\n')

def load_payout_values(file_name):
    payout_values = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                payout_values.append(str(line.strip()))
    except FileNotFoundError:
        pass
    return payout_values

tff_payout_file = "tff_payout.txt"
ftmo_payout_file = "ftmo_payout.txt"

tff_payout = load_payout_values(tff_payout_file)
ftmo_payout = load_payout_values(ftmo_payout_file)

def payout_entry_loop():
    while True:
        cevap = input("TFF or FTMO? (Press enter for exit): ")

        if cevap.lower() == 'tff':
            tff_payout_value = input("Enter TFF payout: ")
            if tff_payout_value:
                tff_payout.append(float(tff_payout_value))  # Convert to float here
        elif cevap.lower() == 'ftmo':
            ftmo_payout_value = input("Enter FTMO payout: ")
            if ftmo_payout_value:
                ftmo_payout.append(float(ftmo_payout_value))  # Convert to float here
        elif cevap.lower() == 'q' or not cevap:
            break
        else:
            print("Invalid choice. Please try again.")

    return tff_payout, ftmo_payout



choice_click = input("Do you want scale balance calculate (enter 'scale') or input the payout (enter 'payout'): ")

if choice_click == "scale":
    scale_balance()
elif choice_click == "payout":
    tff_payout, ftmo_payout = payout_entry_loop()


save_payout_values(tff_payout_file, tff_payout)
save_payout_values(ftmo_payout_file, ftmo_payout)



def total_ftmo():
    total_sum = 0
    with open(ftmo_payout_file, 'r') as file:
        for line in file:
            value = float(line.strip())  
            total_sum += value

    return total_sum

result_ftmo = total_ftmo()


def total_tff():
    total_sum = 0
    with open(tff_payout_file, 'r') as file:
        for line in file:
            value = float(line.strip())  
            total_sum += value

    return total_sum

result_tff = total_tff()


print("Total TFF Payout:", str(result_tff) + "$", "Funded days:", delta_date_tff.days)
print("Total FTMO Payout:", str(result_ftmo) + "$", "Funded days:", delta_date_ftmo.days)




