import unittest
from tool import validate, validate_many

class ContractTests(unittest.TestCase):
    def test_required_and_types(self):
        contract={"id":{"required":True,"type":"int"},"name":{"type":"str"}}
        self.assertEqual(validate({"id":1,"name":"ok"},contract),[])
        self.assertEqual(validate({"id":"x"},contract),["id has wrong type"])
        self.assertEqual(validate_many([{}, {"id":2}],contract),{0:["missing id"]})

if __name__ == "__main__": unittest.main()
