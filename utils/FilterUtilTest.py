import unittest
from FilterUtil import FilterUtil

class FilterUtilTest(unittest.TestCase):
    def test_Empty_CleanDescription(self):
        self.assertEquals(FilterUtil.cleanDescription(self, ""), [])

    def test_One_CleanDescription(self):
        result = ["hello"]
        self.assertEquals(FilterUtil.cleanDescription(self, "Hello!"), result)

    def test_Multiple_CleanDescription(self):
        result = ["hello", "my", "name", "is", "aidan"]
        self.assertEquals(FilterUtil.cleanDescription(self, "Hello! My name is Aidan"), result)

    def test_CleanDescription(self):
        result = ["doesnt"]
        self.assertEquals(FilterUtil.cleanDescription(self, "Doesn't"), result)

    def test_Empty_FilterIgnoreList(self):
        self.assertEquals(FilterUtil.filterIgnoreList(self, [], []), [])

    def test_Empty_IgnoreList_FilterIgnoreList(self):
        input = ["hello", "there"]
        result = ["hello", "there"]
        self.assertEquals(FilterUtil.filterIgnoreList(self, [], input), result)

    def test_Empty_Input_FilterIgnoreList(self):
        self.assertEquals(FilterUtil.filterIgnoreList(self, FilterUtil.initializeIgnoreList(self), []), [])

    def test_One_Input_FilterIgnoreList(self):
        input = ["brother"]
        result = ["brother"]
        self.assertEquals(FilterUtil.filterIgnoreList(self, FilterUtil.initializeIgnoreList(self), input), result)

    def test_One_Input_Ignore_FilterIgnoreList(self):
        input = ["hello"]
        self.assertEquals(FilterUtil.filterIgnoreList(self, FilterUtil.initializeIgnoreList(self), input), [])

    def test_Multiple_Input_FilterIgnoreList(self):
        input = ["brother", "my", "problem"]
        result = ["brother", "my", "problem"]
        self.assertEquals(FilterUtil.filterIgnoreList(self, FilterUtil.initializeIgnoreList(self), input), result)


    def test_Multiple_Ignore_FilterIgnoreList(self):
        input = ["hello", "goodbye"]
        self.assertEquals(FilterUtil.filterIgnoreList(self, FilterUtil.initializeIgnoreList(self), input), [])

    def test_FilterIgnoreList(self):
        input = ["hi", "my", "door", "doesnt", "close", "thanks"]
        result = ["my", "door", "doesnt", "close"]  
        self.assertEquals(FilterUtil.filterIgnoreList(self, FilterUtil.initializeIgnoreList(self), input), result)

    def test_Empty_FilterDescription(self):
        self.assertEquals(FilterUtil.filterDescription(self, ""), "")

    def test_One_Ignore_FilterDesciption(self):
        self.assertEquals(FilterUtil.filterDescription(self, "Hello!"), "")

    def test_One_FilterDescription(self):
        self.assertEquals(FilterUtil.filterDescription(self, "Brother!"), "brother")

    def test_All_FilterDescription(self):    
        self.assertEquals(FilterUtil.filterDescription(self, "Brother I am good!"), "brother i am good")


    def test_All_Ignore_FilterDescription(self):
        self.assertEquals(FilterUtil.filterDescription(self, "Hello, hello, Goodbye!"), "")

    def test_FilterDescription(self):
        self.assertEquals(FilterUtil.filterDescription
                          (self, 
                           "Hi. Please let reception know that the person looking after my cat will be taking it out today. I am delayed in the uk, so they are taking it home with them.")
                           , "please let reception know that the person looking after my cat will be taking it out today i am delayed in the uk so they are taking it home with them")


if __name__ == '__main__':
    unittest.main()