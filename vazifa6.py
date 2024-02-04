# 1
# class WeekDays:
#     days = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
#     count = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.count < len(self.days):
#             result = self.days[self.count]
#             self.count += 1
#             return result
#         else:
#             raise StopIteration

# week_days = WeekDays()

# for day in week_days:
#     print(day)


# 2
# class Months:
#     moon = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul","Avgust","Sentabr","Oktabr","Noyabr","Dekabr"]
#     count = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.count < len(self.moon):
#             result = self.moon[self.count]
#             self.count += 1
#             return result
#         else:
#             raise StopIteration

# months = Months()

# for moon in months:
#     print(moon)



# 3
# class User:
#     users = []

#     def __init__(self, f_name, l_name, email):
#         self.f_name = f_name
#         self.l_name = l_name
#         self.email = email
#         User.users.append(self)

#     def __iter__(self):
#         self.index = 0
#         return self

#     def __next__(self):
#         if self.index < len(User.users):
#             result = User.users[self.index]
#             self.index += 1
#             return result
#         raise StopIteration

# user1 = User("Azizxon", "Abdulvahobov", "azizxon@gmail.com")
# user2 = User("Azizbek","Turdiqulov","azizbekturdialiyevich@gmail.com")

# for user in user1:
#     print(f"First Name: {user.f_name}, Last Name: {user.l_name}, Email: {user.email}")

