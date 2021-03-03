import newsfeedingester

class TestClass:

    def test_function_1(self):
        assert bookmark('mark') == True

    def test_function_2(self):
        assert unbookmark('unmark') == False

    def test_function_3(self):
        assert organize('topic') == 'Organized by topic'

    def test_function_4(self):
        assert organize('date') == 'Organized by date:'

    def test_function_5(self):
        assert theme('1/1/2020 to 12/1/2020') == 'Content from 1/1/2020 to 12/1/2020'

    def test_function_6(self):
        assert filter('Politics') == 'Politics Content:'

    def test_function_7(self):
        assert filter('2018') == '2018 Content:'