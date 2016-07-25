import os
os.system ('cls')
import prettytable 
cc_t= float(input("Enter Credit Card Amount: $"))
c_f= float(input("Enter Total Cash Amount: $"))
c_s= float(input("Enter Start Cash: $"))
c_m= c_f-c_s
print ("Cash Collected: $",c_m)
def credit():
	num21= float(input("Number of Tickets for $4.50: "))
	num22= float(input("Number of Tickets for $6.50: "))
	num23= float(input("Number of Tickets for $6.75: "))
	num24= float(input("Number of Tickets for $8.50: "))
	num25= float(input("Number of Tickets for $10.00: "))
	num26= float(input("Number of Tickets for $11.50: "))
	num27= float(input("Number of Tickets for $13.00: "))
	num28= float(input("Number of Tickets for $0.50: "))
	num29= float(input("Number of Tickets for $1.50: "))
	num30= float(input("Number of Tickets for $2.50: "))
	num31= float(input("Number of Tickets for $3.50: "))
	num32= float(input("COD amount: "))
	tct=int((num21+num22+num23+num24+num25+num26+num27+num28+num29+num30+num31))
	a_1=4.5*num21
	b_1=6.5*num22
	c_1=6.75*num23
	d_1=8.5*num24
	e_1=10.0*num25
	f_1=11.5*num26
	g_1=13.0*num27
	h_1=0.5*num28 + 1.5*num29 + 2.5*num30 + 3.5*num31
	k_1=int(num28+num29+num30+num31)
	tcp=a_1+b_1+c_1+d_1+e_1+f_1+g_1+h_1
	tp_cc=tcp+num32
	if tp_cc != cc_t:
		print ("\nCredit Card Ammount not matching. Count Tickets again\n")
		return credit()
	else:
		print("----------------------------------------------------------------------------------")
		from prettytable import PrettyTable
		t1 = PrettyTable(['No.', 'Amount', 'Total'])
		t1.add_row([int(num21),"$4.50",a_1])
		t1.add_row([int(num22),"$6.50",b_1])
		t1.add_row([int(num23),"$6.75",c_1])
		t1.add_row([int(num24),"$8.50",d_1])
		t1.add_row([int(num25),"$10.00",e_1])
		t1.add_row([int(num26),"$11.50",f_1])
		t1.add_row([int(num27),"$13.00",g_1])
		print (t1)
		from prettytable import PrettyTable
		w1 = PrettyTable(['No.', '$0.50', '$1.50', '$2.50', '$3.50', '$ Total'])
		w1.add_row([k_1,int(num28),int(num29),int(num30),int(num31),h_1])
		print (w1)
		from prettytable import PrettyTable
		x1 = PrettyTable(['Term', 'Value'])
		x1.add_row(["TOTAL TICKETS",tct])
		x1.add_row(["SUB TOTAL",tcp])
		x1.add_row(["COD",num32])
		x1.add_row(["TOTAL",tp_cc])
		print (x1)
		print ("Credit Card Finished.\nDo Cash Sheet")
def cash():
	num1= float(input("\nNumber of Tickets for $4.50: "))
	num2= float(input("Number of Tickets for $6.50: "))
	num3= float(input("Number of Tickets for $6.75: "))
	num4= float(input("Number of Tickets for $8.50: "))
	num5= float(input("Number of Tickets for $10.00: "))
	num6= float(input("Number of Tickets for $11.50: "))
	num7= float(input("Number of Tickets for $13.00: "))
	num8= float(input("Number of Tickets for $0.50: "))
	num9= float(input("Number of Tickets for $1.50: "))
	num10= float(input("Number of Tickets for $2.50: "))
	num11= float(input("Number of Tickets for $3.50: "))
	num12= float(input("Number of Tickets for White Coupons: "))
	num13= float(input("Number of Tickets for Blue Coupons: "))
	num14= float(input("Number of Tickets for IDOC: "))
	num15= float(input("Number of Tickets for IDNW: "))
	num16= float(input("Number of Tickets for PTE: "))
	num17= float(input("Number of Tickets for GRACE: "))
	num18= float(input("COD amount: "))
	tt=int(num1+num2+num3+num4+num5+num6+num7+num8+num9+num10+num11+num12+num3+num14+num15+num16+num17)
	a=4.5*num1
	b=6.5*num2
	c=6.75*num3
	d=8.5*num4
	e=10.0*num5
	f=11.5*num6
	g=13.0*num7
	h=0.5*num8 + 1.5*num9 + 2.5*num10 + 3.5*num11
	i=int(num12+num13)
	j=int(num14+num15+num16+num17)
	k=int(num8 + num9 + num10 + num11)
	tp=a+b+c+d+e+f+g+h
	tp_1=tp+num18
	if tp_1 != c_m:
		print ("\nCash Ammount not matching. Count Tickets again\n")
		return cash()
	else:
		print("----------------------------------------------------------------------------------")
		from prettytable import PrettyTable
		t = PrettyTable(['No.', 'Amount', 'Total'])
		t.add_row([int(num1),"$4.50",a])
		t.add_row([int(num2),"$6.50",b])
		t.add_row([int(num3),"$6.75",c])
		t.add_row([int(num4),"$8.50",d])
		t.add_row([int(num5),"$10.00",e])
		t.add_row([int(num6),"$11.50",f])
		t.add_row([int(num7),"$13.00",g])
		print (t)
		from prettytable import PrettyTable
		u = PrettyTable(['No.', 'IDOC', 'IDNW', 'PTE', 'GRACE'])
		u.add_row([j,int(num14),int(num15),int(num16),int(num17)])
		print (u)
		from prettytable import PrettyTable
		v = PrettyTable(['No.', 'WHITE', 'BLUE'])
		v.add_row([i,int(num12),int(num13)])
		print (v)
		from prettytable import PrettyTable
		w = PrettyTable(['No.', '$0.50', '$1.50', '$2.50', '$3.50', '$ Total'])
		w.add_row([k,int(num8),int(num9),int(num10),int(num11),h])
		print (w)
		from prettytable import PrettyTable
		x = PrettyTable(['Term', 'Value'])
		x.add_row(["TOTAL TICKETS",tt])
		x.add_row(["SUB TOTAL",tp])
		x.add_row(["COD",num18])
		x.add_row(["TOTAL",tp_1])
		print (x)
def main():
	yes = set(['yes','y'])
	no = set(['no','n'])
	choice = input("Is this a credit card sheet:").lower()
	if choice in yes:
		credit()
		cash()
	elif choice in no:
		print ("Do Credit Card sheet first")
		return main()
		return False
	else:
		print ("Invalid Input. Enter Yes or No ")
		return main()
if __name__ == "__main__":
	main()