import textNLPanalysis

class TestClass:

    def test_function_1(self):
        assert sentiment('Communism.docx') == 'Bias: \n Opinion Polarity: '

    def test_function_2(self):
        assert topic('Stocks 101') == 'Business, Economics'

    def test_function_3(self):
        assert web('East_Coast_Culture.pdf') == 'Relevant information and resources:'

    def test_function_4(self):
        assert translate('Japanese_Doctrine.pdf') == 'Japanese to English:'