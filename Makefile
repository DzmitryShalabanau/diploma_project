test_chrome_headless:
	pytest --reruns 5 -n 2 --headless=True --count=2 --b=chrome --alluredir allure_results_chrome
test_chrome:
	pytest --reruns 5 -n 2 --headless=False --count=2 --b=chrome --alluredir allure_results_chrome

test_edge_headless:
	pytest --reruns 5 -n 2 --headless=True --count=2 --b=chrome --alluredir allure_results_edge
test_edge:
	pytest --reruns 5 -n 2 --headless=False --count=2 --b=edge --alluredir allure_results_edge

serve_results_chrome:
	allure serve allure_results_chrome
serve_results_edge:
	allure serve allure_results_edge

test_login_for_diploma:
	pytest test_login.py --reruns 5 --headless=False --alluredir allure_results_chrome