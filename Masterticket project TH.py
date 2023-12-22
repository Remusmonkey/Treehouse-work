TICKET_PRICE = 10

tickets_remaining = 100


while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("May I have your name please?  ")
    num_tick_req = input("How many tickets would you like {}?  ".format(name))
    try:
        num_tick_req = int(num_tick_req)
        if num_tick_req > tickets_remaining:
            raise ValueError ("There are only {} tickets remaining".format(tickets_remaining))
        #raise a ValueError if the request is for more ticketsthan are available
    except ValueError as err:
        print("We ran into an issue. {}. Please try again".format(err))
#        if num_tick_req > tickets_remaining:
#           print("I'm sorry there are not enough tickets to process your order {}, please try again".format(name))
#        
        
    else:
        total_cost = num_tick_req * TICKET_PRICE
        print("{}, this is your total for {} tickets: ${}".format(name, num_tick_req, total_cost))
        confirm = input("Would you like to proceed {}. Y/N? ".format(name)) 
    # TODO: Gather credit card info and process it
        if confirm.lower() == "y":
            print("Sold! Thank you for your purchase {}.".format(name))
            tickets_remaining -= num_tick_req
        else:
            print("Thank you for you time {}.".format(name))

print("I'm sorry all tickets are sold out")

# My original code
# while tickets_remaining >= 1:
#     print("There are {} tickets remaining.".format(tickets_remaining))
#     name = input("May I have your name please?  ")
#     num_tick_req = int(input("How many tickets would you like {}?  ".format(name)))
#     if num_tick_req != int():
#         print("Please input a whole number.")
#     if num_tick_req > tickets_remaining:
#         print("I'm sorry there are not enough tickets to process your order {}".format(name))
#     else:
#         total_cost = num_tick_req * TICKET_PRICE
#         print("{}, this is your total for {} tickets: ${}".format(name, num_tick_req, total_cost))
#         confirm = input("Would you like to proceed {}. Y/N? ".format(name)) 
#             # TODO: Gather credit card info and process it
#         if confirm.lower() == "y":
#             print("Sold! Thank you for your purchase {}.".format(name))
#             tickets_remaining -= num_tick_req
#         else:
#             print("Thank you for you time {}.".format(name))
# 
# print("I'm sorry all tickets are sold out"