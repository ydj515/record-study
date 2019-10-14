from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://pythonclock.org')


a = r.html.search('Python 2.7 will retire in...{}Enable Guido Mode')[0]
print(a)


periods = [element.text for element in r.html.find('.countdown-period')]
print(periods)
amounts = [element.text for element in r.html.find('.countdown-amount')]
countdown_data = dict(zip(periods, amounts))
print(countdown_data)

# run without javascript rendering
tmp = r.html.search('Python 2.7 will retire in...{}Enable Guido Mode')[0]
print("run without javascript rendering ",tmp)
print("")

#Run With Javascript Rendering
r.html.render()
tmp = r.html.search('Python 2.7 will retire in...{}Enable Guido Mode')[0]
print("run with javascript rendering ",tmp)
print(type(tmp))