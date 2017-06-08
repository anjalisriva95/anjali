from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('James Bond', 'Mr.', 24, 4.7)

friend_one = Spy('Aditi Bhardaj', 'Miss.', 22, 4.9)
friend_two = Spy('Simran Raj', 'Miss.', 21, 4.56)
friend_three = Spy('Akhil Bharti', 'Dr.', 22, 4.76)
friend_four = Spy('Akash Singh' , 'Mr' , 21, 5.0)


friends = [friend_one, friend_two, friend_three, friend_four]