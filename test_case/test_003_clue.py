# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-
import pytest

from page_action.clue_manage import ClueManage
from page_action.components import Components
from page_action.ai import AiDashboard


class TestClue:

    @pytest.mark.usefixtures("login_by_token")
    # @pytest.mark.usefixtures("login_by_mobile")
    def test_001(self, drivers):
        """搜索"""
        # clue = ClueManage(drivers)
        # clue.search_check()
        pass


if __name__ == '__main__':
    pytest.main(['-s', 'TestCase/test_003_clue.py'])
