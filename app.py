from flask import Flask, request, render_template
import urllib.request, json, os
from dotenv import load_dotenv


load_dotenv()
config = {
	"google_key": os.getenv('GOOGLE_KEY'),
	"api_key": os.getenv('API_KEY')
}

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def ip():
	if request.method == 'POST':
		ip = request.form['ip']
		url = f'https://ipinfo.io/{ip}/?token={config["api_key"]}'
	else:
		url = f'https://ipinfo.io/?token={config["api_key"]}'

	source = urllib.request.urlopen(url)
	response = json.load(source)

	split = response['org'].split()
	org = " ".join(split[1:])

	data = {
		"city": str(response['city']),
		"hostname": str(response['hostname']),
		"ip": str(response['ip']),
		"loc": str(response['loc']),
		"postal": str(response['postal']),
		"region": str(response['region']),
		"timezone": str(response['timezone']),
		"country": str(response['country']),
		"org": str(org)
		# "org": str(response['org']),

	}

	return render_template('index.html', data=data, request=request, config=config)


if __name__ == '__main__':
	app.run(debug=True)