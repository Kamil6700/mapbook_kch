
users:list=[
    {'username':'kamil', 'location': 'łódź','posts':1,'usermessage': ['życzenia1', 'kocham legie', 'sprzedam opla', 'kiwi']},
    {'username':'wiktoria', 'location': 'ostróda','posts':2,'usermessage': ['życzenia2', 'kocham legie1', 'sprzedam opla1']},
    {'username':'paweł', 'location': 'radom','posts':3,'usermessage': ['życzenia3', 'kocham legie2']},
    {'username':'filip', 'location': 'dęblin','posts':4,'usermessage': ['życzenia4', 'kocham legie3', 'sprzedam opla3', 'kiwi3']}
]

for user in users[1:]:
    print(f'twoj znajomy {user['username']} z miejscowości {user["location"]} opublikował {user['posts']} wiadomości. Ostatnia wiadomość {user['usermessage'][-1]}')


#   twój znajomy filip z miejscowości dęblin opublikował 1 post o treści: życzenia