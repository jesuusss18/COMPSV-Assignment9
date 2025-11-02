class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []
    def add_friend (self, friend):
        if friend not in self.friends :
            self.friends.append(friend)

 
class SocialNetwork:
    def __init__(self):
        self.person = {}
    def add_person(self, name):
        if name not in self.person:
            self.person[name] = Person(name)
        else:
            print("Name already exist on the network")
    def add_friendship(self,person1_name, person2_name):
        if person1_name in self.person and person2_name in self.person:

            person1 = self.person[person1_name]
            person2 = self.person[person2_name]

            person1.add_friend(person2)
            person2.add_friend(person1)

        else:
            print("One of the persons does not exist!")

    def print_network(self):
        for name, person in self.person.items():
            friends = [f.name for f in person.friends]
            print(name, ":", friends)

# Test your code here
social_network = SocialNetwork()

# Add 6 people
print('New Test')
social_network.add_person("Carlos")
social_network.add_person("Lucía")
social_network.add_person("Miguel")
social_network.add_person("Sofía")
social_network.add_person("Diego")
social_network.add_person("Elena")

# Try adding a duplicate
print('New Test')
social_network.add_person("Lucía")

# Create friendships
print('New Test') 
social_network.add_friendship("Carlos", "Lucía")
social_network.add_friendship("Carlos", "Miguel")
social_network.add_friendship("Lucía", "Sofía")
social_network.add_friendship("Miguel", "Diego")
social_network.add_friendship("Sofía", "Elena")
social_network.add_friendship("Diego", "Carlos")
social_network.add_friendship("Lucía", "Elena")
social_network.add_friendship("Miguel", "Sofía")

# Edge case: non-existent person
print('New Test')
social_network.add_friendship("Carlos", "Pedro")

# Print social network
print("Social Network")
social_network.print_network()

'''
Why is a graph the right structure to represent a social network?

A graph is the best way to represent a social network because it shows how people are
connected to each other. In a graph, each person is a node, and every friendship is 
an edge that connects two people. This makes it easy to show that people can have many
friends, and friends can also be connected with one another. The graph structure fits
how real social networks work.

Why wouldn’t a list or tree work as well for this?

A list or a tree would not work as well. A list only keeps things in order,but it doesn’t show
any connections between them. A tree also doesn’t fit because it has one main “root” and branches 
that go in one direction. In a social network, there is no single root person, and friendships go
both ways. 

What performance or structural trade-offs did you notice when adding friends or printing the network?

When adding people or friendships, the program runs quickly because it just adds new items to the 
dictionary or friend lists. However, printing the whole network can take longer when there are many 
people and friends, since it must go through each person and their friends. Still, using a dictionary
to store people and their friend lists is a simple and efficient way to build this small social network.

'''