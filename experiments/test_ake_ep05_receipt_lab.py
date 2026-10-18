import unittest
from ake_ep05_receipt_lab import validate_record,sample_record,report
class ReceiptLabTests(unittest.TestCase):
    def test_valid(self):self.assertTrue(validate_record(sample_record())[0])
    def test_recipient(self):self.assertEqual(validate_record(dict(sample_record(),recipient_owner='OTHER'))[1],'WRONG_RECIPIENT_OWNER')
    def test_mint(self):self.assertEqual(validate_record(dict(sample_record(),mint='OTHER'))[1],'WRONG_TOKEN_MINT')
    def test_failed(self):self.assertEqual(validate_record(dict(sample_record(),meta_err={'error':'failed'}))[1],'TRANSACTION_FAILED')
    def test_finality(self):self.assertEqual(validate_record(dict(sample_record(),confirmation_status='confirmed'))[1],'NOT_FINALIZED')
    def test_amount(self):self.assertEqual(validate_record(dict(sample_record(),raw_amount='499999999'))[1],'AMOUNT_MISMATCH')
    def test_decimals(self):self.assertEqual(validate_record(dict(sample_record(),decimals=9))[1],'WRONG_TOKEN_DECIMALS')
    def test_instruction(self):self.assertEqual(validate_record(dict(sample_record(),instruction='memo'))[1],'NO_RECOGNIZED_TRANSFER')
    def test_duplicate(self):
        seen=set();self.assertTrue(validate_record(sample_record(),seen=seen)[0]);self.assertEqual(validate_record(sample_record(),seen=seen)[1],'DUPLICATE_SIGNATURE')
    def test_missing_signature(self):self.assertEqual(validate_record(dict(sample_record(),signature=''))[1],'MISSING_SIGNATURE')
    def test_float(self):self.assertEqual(validate_record(dict(sample_record(),raw_amount=500000000.0))[1],'INVALID_AMOUNT')
    def test_negative(self):self.assertEqual(validate_record(dict(sample_record(),raw_amount='-500000000'))[1],'INVALID_AMOUNT')
    def test_report(self):self.assertEqual(len(report()),6)
if __name__=='__main__':unittest.main(verbosity=2)
