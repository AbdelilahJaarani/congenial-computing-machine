class User:

    #Attributen von einer Klasse
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1



user1 = User("01","AJ")
user2 = User("02","HJ")

user1.follow(user2)

print(user1.follower)
print(user1.following)
print(user2.follower)
print(user2.following)
