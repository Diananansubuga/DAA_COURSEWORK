from collections import deque

class socialNetwork:
    def __init__(self):
        self.graph={}
        
    def add_edge(self, user1,user2):
        if user1 not in self.graph:
            self.graph[user1]=[]
        if user2 not in self.graph:
            self.graph[user2]=[]
            
        self.graph[user1].append(user2)
        self.graph[user2].append(user1)
        
    def mutual_friends(self,user1,user2):
        visited=set()
        queue=deque([user1,user2])
        
        while queue:
            current_user, path=queue.popleft() if queue else(None,[])
            
            if current_user==user2:
                return path
            visited.add(current_user)
            
            for friend in self.graph.get(current_user,[]):
                if friend not in visited:
                    queue.append((friend,path+[friend]))
                    
        return []

social_network=socialNetwork()
social_network.add_edge("Alice","Bob")
social_network.add_edge("Alice","charlie")
social_network.add_edge("Bob","David")
social_network.add_edge("Charlie","Eve")
social_network.add_edge("Eve","Frank")

user1="Alice"
user2="Frank"

mutual_friends_list=social_network.mutual_friends(user1,user2)

if mutual_friends_list:
    print(f"mutual friends between {user1} and {user2}: {mutual_friends_list}")
    
else:
    print(f"{user1}and {user2} have no mutual friends")
            