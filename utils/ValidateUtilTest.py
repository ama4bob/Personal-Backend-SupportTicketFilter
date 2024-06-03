import unittest
from ValidateUtil import ValidateUtil

class ValidateUtilTest(unittest.TestCase):
    def test_Empty_ValidateTicket(self):
        self.assertEquals(ValidateUtil.validateTicket(self, {}), True)
    
    def test_One_Required_ValidateTicket(self):
        input = {
            "createdAt": "2023-03-06T15:08:00Z"
        }
        self.assertEquals(ValidateUtil.validateTicket(self, input), True)

    def test_Two_Required_ValidateTicket(self):
        input = {
            "createdAt": "2023-03-06T15:08:00Z",
            "tel": 55555555
        }
        self.assertEquals(ValidateUtil.validateTicket(self, input), False)        

    def test_One_Optional_ValidateTicket(self):
        input = {
            "msg": "askldfjakld"
        }
        self.assertEquals(ValidateUtil.validateTicket(self, input), True)

    def test_Two_Optional_ValidateTicket(self):
        input = {
            "msg": "askldfjakld",
            "fileUrl": "fileUrl"
        }
        self.assertEquals(ValidateUtil.validateTicket(self, input), True)

    def test_One_Optional_Valid_ValidateTicket(self):
        input = {
            "createdAt": "2023-03-06T15:08:00Z",
            "tel": 55555555,
            "msg": "askldfjakld"
        }
        self.assertEquals(ValidateUtil.validateTicket(self, input), False)

    def test_Two_Optional_Valid_ValidateTicket(self):
        input = {
            "createdAt": "2023-03-06T15:08:00Z",
            "tel": 55555555,
            "msg": "askldfjakld",
            "fileUrl": "fileUrl"
        }
        self.assertEquals(ValidateUtil.validateTicket(self, input), False)

    def test_Two_Optional_Invalid_ValidateTicket(self):
        input = {
            "createdAt": "2023-03-06T15:08:00Z",
            "msg": "askldfjakld",
            "fileUrl": "fileUrl"
        }
        self.assertEquals(ValidateUtil.validateTicket(self, input), True)

    def test_One_Required_Empty_Field_ValidateTicket(self):
        input = {
             "createdAt": None,
        }

        input2 = {
             "createdAt": "",
        }
        self.assertEquals(ValidateUtil.validateTicket(self, input), True)
        self.assertEquals(ValidateUtil.validateTicket(self, input2), True)

    def test_Two_Required_Empty_Field_ValidateTicket(self):
        input = {
             "createdAt": None,
             "tel": None,
        }

        input2 = {
            "createdAt": "",
            "tel": None
        }
        self.assertEquals(ValidateUtil.validateTicket(self, input), True)
        self.assertEquals(ValidateUtil.validateTicket(self, input2), True)

    def test_Two_Required_One_Empty_One_Filled_ValidateTicket(self):
        input = {
            "createdAt": "2023-03-06T15:08:00Z",
            "tel": None
        }
        self.assertEquals(ValidateUtil.validateTicket(self, input), True)


        

if __name__ == '__main__':
    unittest.main()