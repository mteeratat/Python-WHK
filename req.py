import requests

r = requests.get('https://www.uncle-engineer.com/api/hacking/fruit-list.txt?fbclid=IwAR3zW6g5AXQkJR7vufonx361fvxvvsx_Vg_TipirYfLyyH1rl_9smjkE-54')
print(r.text)
# for t in r.content:
#     print(t)

file = open('myfile.txt', 'w')
file.write(r.text)
file.close()