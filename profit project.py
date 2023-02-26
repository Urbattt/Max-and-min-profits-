from tkinter import* 

root= Tk()
root.geometry("600x400")
root.title("greatest profit")

month = ("January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits=(20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)

min1_profit = Label(root)
max1_profit = Label(root)
month_label = Label(root, text= "January, Febuary, March, April, May, June, July, August, September, October, November, December")
profits_label = Label(root, text = "20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000")


max_profit=max(profits)
max_profit_index= profits.index(max_profit)
print(max_profit_index)



max_profit_month = month[max_profit_index]
print("The maximum profit of " + str(max_profit)+ " was recorded in the month of " + str(max_profit_month))

min_profit = min(profits)
min_profit_index= profits.index(min_profit)
print(min_profit_index)

min_profit=min(profits)
min_profit_index = profits.index(min_profit)
print(min_profit_index)

min_profit_month=month[min_profit_index]
print("The minimum profit of " + str(min_profit)+" was recorded in the month of "
      +str(min_profit_month))

def maximum():
    max1_profit["text"]="The maximum profit of " + str(max_profit)+ " was recorded in the month of " + str(max_profit_month)

def minimum():
    min1_profit["text"]="The minimum profit of " + str(min_profit)+" was recorded in the month of " +str(min_profit_month)


btn = Button(root, text = "Maximum Profit", command= maximum)
btn.place(relx = 0.5, rely = 0.7, anchor= CENTER)

max1_profit.place(relx=0.5, rely=0.6, anchor = CENTER)

btn1 = Button(root, text = "Minimum Profit", command= minimum)
btn1.place(relx = 0.5, rely = 0.5, anchor= CENTER)

min1_profit.place(relx=0.5, rely=0.4, anchor = CENTER)

month_label.place(relx=0.5, rely=0.9, anchor =CENTER)
profits_label.place(relx=0.5, rely=0.8, anchor =CENTER)


root.mainloop()