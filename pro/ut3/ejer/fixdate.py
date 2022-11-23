date = "12/31/20"
date_list = date.split("/")
date_list = [date_list[1], date_list[0], "20" + date_list[2]]
date = "-".join(date_list)
print(date)
