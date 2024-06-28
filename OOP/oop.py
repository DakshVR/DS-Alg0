# class StarCookie:
#     milk= 1
#     def __init__(self, weight, color):
#         self.weight = weight
#         self.color = color

# star_cookie1 = StarCookie(12, 'red')
# star_cookie1.weight = 14
# star_cookie1.color = 'Red'

# print(star_cookie1.weight)
# print(star_cookie1.color)
# print(star_cookie1.milk)

# star_cookie2 = StarCookie(22, 'blue')
# print(star_cookie2.milk)
# print(star_cookie2.weight)
# print(star_cookie2.color)

# print(star_cookie1.__dict__)
# print(star_cookie2.__dict__)
# print(StarCookie.__dict__)

class Youtube:
    def __init__(self, username, subscribers=0, subscription=0) -> None:
        self.username = username
        self.subscribers = subscribers
        self.subscription = subscription

    def subscribe(self, user):
        user.subscribers +=1
        self.subscription +=1


user1= Youtube("daksh")
user2= Youtube('Gurav')

print(user1.subscribers)
print(user1.subscription)

print(user2.subscribers)
print(user2.subscription)

user1.subscribe(user2)

print("After-------------------------------------")
print(user1.subscribers)
print(user1.subscription)

print(user2.subscribers)
print(user2.subscription)
