from test_other.abc import A
import pytest

class TestB:
    @pytest.mark.parametrize("a,b,c", [["a", "b", "c"], ["c", "d", "1"], ], ids=["提报告厅", "提报告厅2"])
    def test_a(self,a,b,c):
        print(a,b,c)
        assert False

    @pytest.mark.parametrize("a,b,c", [["a", "b", "c"], ["c", "d", "1"], ], ids=["提报告厅", "提报告厅2"])
    def test_b(self,a,b,c):
        print(a,b,c)
        assert False
