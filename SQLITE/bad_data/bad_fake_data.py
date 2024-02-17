import random as rd
rd.seed(123)

# Expanded first name and last name lists
first_name_list = ["Alice", "Bob", "Charlie", "David", "Emily", 
                   "Frank", "Grace","Henry", "Isabella", "Jack", 
                   "Kate", "Liam", "Mia", "Noah", "Olivia", "Peter", 
                   "Quinn", "Ryan", "Sophia", "Thomas","Ursula", 
                   "Victor", "Wendy", "Xavier", "Yara", "Zachary", 
                   "Amelia", "Benjamin", "Chloe","Daniel", "Emma", 
                   "Fiona", "George", "Hannah", "Ian", "Julia", 
                   "Kevin", "Lily", "Matthew", "Jo"]

last_name_list = ["Smith", "Johnson", "Brown", "Taylor", "Miller",
                  "Anderson", "Clark", "Davis", "Hall","Lewis","Moore",                   "Parker", "Scott", "Turner", "Walker", "Young",       
                  "Allen", "Baker", "Carter", "Evans","Foster", 
                  "Garcia", "Hill", "James", "King", "Lee", "Martin", 
                  "Nelson", "Owens", "Price","Roberts", "Stewart", 
                  "Thomas", "Ward", "White", "Wilson", "Zimmerman",
                 "B"]

# Generate a list of 80 users
user_list = []
for _ in range(80):
    first_name = rd.choice(first_name_list)
    last_name = rd.choice(last_name_list)
    email_suffix = rd.choice(["@gmail.com",
                              "gmail.com",
                              "@yahoo.com",
                              "yahoo.com",
                              "@hotmail.com",
                             "hotmail.com"])
    email = f"{first_name.lower()}.{last_name.lower()}{email_suffix}"
    location = rd.choice(["London", "New York", "Paris", "Tokyo"])
    user_list.append((first_name, last_name, email, location))
    
# Expanded list of 22 products
product_list = [("laptop", 849.99, 20), 
                ("iphone 10", 620.00, 30), 
                ("samsung s23 phone", 600.00, 40), 
                ("desktop pc", 350.49, 12), 
                ("dyson hover",  299.99, 15), 
                ("apple tablet", 250.55, 22), 
                ("apply watch", 399.99, 27), 
                ("microphone plus", 80.99, 33), 
                ("microphone v10", 45.99, 11), 
                ("flask", 45.00, 90), 
                ("microwave v2", 200.45, 10), 
                ("headphones sony", 60.99, 25),
                ("headphones samsung", 55.50, 24),
                ("headphones apple", 70.75, 28), 
                ("ps5", 550.99, 8), 
                ("xbox 10", 499.99, 8), 
                ("usb 1TB", 50.99, 5), 
                ("usb 500GB", 35.50, 16),
                ("mouse wireless", 15.99, 44), 
                ("mouse wired", 9.99, 3), 
                ("earphones sony", 18.99, 18), 
                ("earphones nokia", 11.95, 19),
               ("apple watch", 0.0, 100),
               ("sony watch", 0.0, 120)]

# Generate a list of 400 orders
order_list = []
for order_id in range(1, 401):
    product_id = rd.randint(1, 22)
    user_id = rd.randint(1, 80)
    quantity = rd.randint(0, 20)
    order_list.append((product_id, user_id, quantity))
