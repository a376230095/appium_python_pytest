from api.wework import Wework


class TestG(Wework):
    def setup(self):
        corpsecret="YC9RRMQcQqGNxapjoeiDIn84mCY7H-aJblz_X9X073U"
        wework=Wework()
        print(wework.get_token(corpsecret))

    def test_a(self):
        pass