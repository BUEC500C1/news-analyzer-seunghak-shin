import securefileuploader_ingester

class TestClass:

     def test_function_1(self):
        assert database_connect('Connected') == True

    def test_function_2(self):
        assert database_connect('Not connected') == False

    def test_function_3(self):
        assert browse('Browsing...') == 'List:'

    def test_function_4(self):
        assert search('airline failure') == 'Search results for "airline failure":'

    def test_function_5(self):
        assert encryption('Report_1.pdf') == 'Encryption successful \n Key : f923 a1ep vb05'

    def test_function_6(self):
        assert upload('List_2.xls') == True

    def test_function_7(self):
        assert upload('journey.mp4') == False

    def test_function_8(self):
        assert decryption('files_enc , key') == 'Files'