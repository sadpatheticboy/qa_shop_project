class Base:
    def __init__(self, driver):
        self.driver = driver

    # Method Get Current Url
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current URL is "{get_url}"')

    # Method Assert Word Check
    def assert_word_check(self, word, result):
        value_word = word.text
        assert value_word == result
        print('All Correct')
