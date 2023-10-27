test_chrome:
	pytest --reruns 5 -n 2 --headless=no --count=2 --b=chrome --alluredir my_allure_results
test_chrome_headless:
	pytest --reruns 5 -n 2 --headless=yes --count=2 --b=chrome --alluredir my_allure_results
test_firefox:
	pytest --reruns 5 -n 2 --headless=no --count=2 --b=firefox --alluredir my_allure_results
test_firefox_headless:
	pytest --reruns 5 -n 2 --headless=yes --count=2 --b=firefox --alluredir my_allure_results
test_edge:
	pytest --reruns 5 -n 2 --headless=False --count=2 --b=edge --alluredir my_allure_results
test_edge_headless:
	pytest --reruns 5 -n 2 --headless=True --count=2 --b=edge --alluredir my_allure_results
serve_results:
	allure serve my_allure_results

