from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from values import stuff
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


def get_symbol(element):
	def has_class(elt, name):
		classes = elt.get_attribute('class')
		for class_name in classes.split():
			if class_name == name:
				return True
		return False
	
	if has_class(element, 'css-1kiw93k-svg'):
		print('its x')
		return -1
	elif has_class(element, 'css-hcqxoa-svg'):
		print('its tick')
		return 2
	elif has_class(element, 'css-1h93d4v-svg'):
		print('its flat line')
		return 1
	elif has_class(element, 'css-10xv9lv-svg'):
		print('its circle')
		return 0



file = open('tesla.csv', 'a', newline='', encoding='utf-8')
writer = csv.writer(file)

# header = ['Company', 'Star Rating', 'Current Employee', 'Work Duration', 'Review Title', 'Date Posted', 'Job Title', 'Job Location', 'Recommend', 'CEO Approval', 'Business Outlook', 'Pros', 'Cons', 'Advice to 			Management']
# writer.writerow(header)


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.glassdoor.com/profile/login_input.htm")
driver.maximize_window()


email_input = driver.find_element_by_id('inlineUserEmail')
password_input = driver.find_element_by_id('inlineUserPassword')
sign_in = driver.find_element_by_class_name('evpplnh1')

email_input.send_keys(stuff['username'])
password_input.send_keys(stuff['password'])
sign_in.click()

print('sign in complete')
time.sleep(3)
companies = stuff['companies']
print('companies are -----------------' , companies)

for company, idx in companies:
	print('\n\ncurrent company:', company)
	search_bar = driver.find_element_by_xpath('/html[1]/body[1]/header[1]/nav[1]/div[1]/div[1]/div[1]/div[4]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]')
	search_bar.click()
	search_bar.send_keys(company)

	element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "e1h5k8h92"))
    )
	element.click()
	driver.find_element_by_class_name('universalSearch__UniversalSearchBarStyles__searchButton').click()


	# finding the company from list of companies
	company_tile = WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'company-tile'))
    )
	company_tile[idx].click()
	time.sleep(1)

	# going to job reviews tab
	review_tab = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "reviews"))
    )
	review_tab.click()
	time.sleep(1)


	

	# getting individual items
	
	count = 1
	page_number = 1

	start_at_page = 1

	# while page_number < start_at_page:
	# 	print('Increasing page number:' , page_number)
	# 	time.sleep(3)
	# 	pagination = driver.find_element(by=By.CLASS_NAME, value='gd-ui-pagination')
	# 	next_button = pagination.find_element_by_class_name('nextButton')
	# 	if next_button.is_enabled():
	# 		next_button.click()
	# 		page_number += 1
	# 	else:
	# 		exit()
	
	if start_at_page != 1:
		print('going to page', start_at_page)

		driver.get(f'https://www.glassdoor.com/Reviews/Tesla-Reviews-E43129_P{start_at_page}.htm?filter.iso3Language=eng')
		page_number = start_at_page

	while True:
		time.sleep(5)
		print('current page number:', page_number)
		# getting employee review feed
		feed =  WebDriverWait(driver, 60).until(
        	EC.presence_of_element_located((By.CLASS_NAME, "emp-reviews-feed"))
    	)

		review_boxes = feed.find_elements_by_class_name('empReview')
		for box in review_boxes:
			review_item = {
				'company_name': company, 
				'rating_number': '',
				'review_title': '',
				'current_employee': '',
				'work_duration': '',
				'date_posted': '',
				'position': '',
				'job_location': '',
				'Recommend': '',
				'CEO Approval': '',
				'Business Outlook': '',
				'Pros': '',
				'Cons': '',
				'Advice to Management': ''
			}
 
			# rating number
			rating_number = box.find_element_by_class_name('ratingNumber').text
			review_item['rating_number'] = float(rating_number)
			# print('rating number of employee', count, ':', rating_number)

			# review title
			review_title = box.find_element_by_class_name('reviewLink').text
			review_item['review_title'] = str(review_title)
			# print('review title of employee', count, ':', review_title)


			# current/former employee, years of working
			line = box.find_element_by_class_name('css-1qxtz39').text
			review_item['current_employee'] = ''
			review_item['work_duration'] = '' 
			if len(line) != 0:
				line = line.lower()

				sections = line.split(',')
				current_former = ''
				work_duration = ''
				if len(sections) != 0:
					if len(sections) == 1:
						current_former = sections[0]
						current_former = current_former.strip()
					else:
						current_former = sections[0]
						current_former = current_former.strip()
						current_former = current_former.lower()
						work_duration = sections[1]
						work_duration = work_duration.strip()
						work_duration = work_duration.lower()
						review_item['work_duration'] = work_duration

				
				if len(current_former) != 0:
					if 'former' in current_former:
						current = 0
					elif 'current' in current_former:
						current = 1
					
					review_item['current_employee'] = current
					# print(f'current = ', current)
					
				
				# print('duration: ', work_duration)


			# date posted and job position
			line = box.find_element_by_class_name('authorJobTitle').text
			date_posted, position = line.split('-', 1)
			date_posted = date_posted.strip()
			position = position.strip()

			date_posted = datetime.strptime(date_posted, '%b %d, %Y')

			review_item['date_posted'] = date_posted.date()
			review_item['position'] = position

			
			# job location
			try:
				location = box.find_element_by_class_name('authorLocation')
				job_location = location.text		
			except:
				job_location = ''
			
			review_item['job_location'] = job_location
			

			# review body cell 
			cell = box.find_element_by_class_name('reviewBodyCell')
			cell_items = cell.find_elements_by_class_name('align-items-center')

			for item in cell_items:
				word = item.find_element_by_class_name('common__EiReviewDetailsStyle__newGrey').text
				picture = item.find_element_by_tag_name('svg')
				symbol = get_symbol(picture)
				
				review_item[word] = symbol

			try:
				continue_button = box.find_element_by_class_name('v2__EIReviewDetailsV2__continueReading')
				continue_button.click()
			except:
				# do nothing
				print('nothing')
			
			review_texts = box.find_elements_by_class_name('v2__EIReviewDetailsV2__fullWidth')
			
			for item in review_texts:
				title = item.find_element_by_class_name('mb-0').text
				content = item.find_element_by_class_name('v2__EIReviewDetailsV2__bodyColor').text
				review_item[title] = content



			# pros, cons, advice to management

			print('EMPLOYEE',count)
			print(review_item)

			row = [
				review_item['company_name'], 
				review_item['rating_number'],
				review_item['current_employee'],
				review_item['work_duration'],
				review_item['review_title'], 
				review_item['date_posted'],
				review_item['position'],
				review_item['job_location'],
				review_item['Recommend'],
				review_item['CEO Approval'],
				review_item['Business Outlook'], 
				review_item['Pros'],
				review_item['Cons'],
				review_item['Advice to Management']
			]

			writer.writerow(row)
			print('\n')
			count += 1
	
		# going to the next page
		pagination = driver.find_element(by=By.CLASS_NAME, value='gd-ui-pagination')
		next_button = pagination.find_element_by_class_name('nextButton')
		if next_button.is_enabled():
			next_button.click()
			page_number += 1
		else:
			break

	
print('scraping completed')
driver.close()
file.close()
