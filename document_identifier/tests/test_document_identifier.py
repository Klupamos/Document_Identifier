from unittest import TestCase

import document_identifier as di


class TestIdentify(TestCase):
    def test_documentation_example(self):
        import document_identifier.RealID as RealID
        unknown_document = {'raw_input': "   -\x1eQ\x01%PAGETTYSBURG^SMITH$JOHN^11 WINDERMERE ST$^?                                                                  ;63632208065640=160819340807=?"}
        documents = di.Identify(scope=RealID, **unknown_document)  # return all constructable machine readable travel documents.
        string = '\n'.join(map(str, documents))
        self.assertIn('PennsylvaniaLicence', string)
        self.assertIn('#08065640', string)
        self.assertIn('JOHN SMITH', string)
        self.assertIn('Tuesday, August 07, 1934', string)

    def test_passport(self):
        import document_identifier.MRTD
        documents = di.Identify(scope=di.MRTD,
            raw_input="P0CHNXIONG<<JUN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<1446251025CHN7907108F021209019204201<<<<<<38")
        self.assertIsInstance(documents, list)
        self.assertIsInstance(documents[0], di.MRTD.Passport)

    def test_realid(self):
        import document_identifier.RealID
        document = di.Identify(scope=di.RealID, return_single=True,
                               mag_track1="%PABERWYN^BUCHER$CHRIS$STEWART^351 4TH DR$^?",
                               mag_track2=";63602529142073=150919890915=?")
        self.assertIsInstance(document, di.RealID.RealID)

    def test_barcode(self):
        import document_identifier.Barcode
        document = di.Identify(scope=di.Barcode, return_single=True,
                               raw_input="447362553223")
        self.assertIsInstance(document, di.Barcode.UPC_A)

    def test_licence(self):
        import document_identifier.LegacyLicence
        document = di.Identify(scope=di.LegacyLicence, return_single=True,
                               raw_input="K12345678")
        self.assertIsInstance(document, di.LegacyLicence.LegacyLicence)
