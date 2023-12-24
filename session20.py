import streamlit as st
import requests



def fetch_data(data):

	copyright = 'NOT MENTIONED'
	date = 'NOT MENTIONED'
	explanation = 'NOT MENTIONED'
	title = 'NOT MENTIONED'
	url = 'NOT MENTIONED'

	if('copyright' in data):
		copyright = data['copyright']
	if('date' in data):
		date = data['date']
	if('explanation' in data):
		explanation = data['explanation']
	if('title' in data):
		title = data['title']
	if('url' in data):
		url = data['url']

	return copyright, date, explanation, title, url

def print_data(copyright, date, explanation, title, url):
	st.write('Copyright : ', copyright)
	st.write('Date : ', date)
	st.write('Explanation : ', explanation)
	st.write('Title : ', title)
	st.write('Url : ', url)


def save_image(url, name):

	response = requests.get(url)

	with open(name+".jpg", 'wb') as file:
		for chunk in response.iter_content(chunk_size=128):
			file.write(chunk)




st.title('NASA APOD Application')

st.write('Astonomy picture -')


API_KEY = 'aYhbW971GME0K137ALnBwg4QBelH5tc2cr6EAsOf'

API_ENDPOINT = 'https://api.nasa.gov/planetary/apod'

params = {
	'api_key' : API_KEY
}


option = st.selectbox('Select', ['Latest', 'Specific Date'])


if(option == 'Latest'):

	result = requests.get(API_ENDPOINT, params=params)
	data = result.json()
	copyright, date, explanation, title, url = fetch_data(data)
	print_data(copyright, date, explanation, title, url)
	save_image(url, date)

elif(option == 'Specific Date'):
	date = st.date_input('Select Date -')
	params['date']=date
	result = requests.get(API_ENDPOINT, params=params)
	data = result.json()
	copyright, date, explanation, title, url = fetch_data(data)
	print_data(copyright, date, explanation, title, url)
	save_image(url, date)




st.image(date+'.jpg')
st.caption(title)