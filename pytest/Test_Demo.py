import logging

logger = logging.getLogger(__name__)


class Test_Demo:
    def test_Demo(self):
        assert 1 == 1, "1 is not equal to 1"
        logger.info("1 is equal to 1")
        logger.debug("1 is equal to 1")
        logger.warning("1 is equal to 1")
        logger.error("1 is equal to 1")
        logger.critical("1 is equal to 1")

    def test_user_name(self, mock_user):
        logger.info("检查用户名")
        assert mock_user["name"] == "mock_user", "用户名错误"

    def test_user_role(self, mock_user):
        logger.info("检查用户角色")
        assert mock_user["role"] == "admin", "用户角色错误"

    def test_order_paid(self, mock_order):
        logger.info("检查订单状态")
        assert mock_order["status"] == "PAID"

    def test_order_amount(self, mock_order):
        logger.info("检查订单金额")
        assert mock_order["amount"] > 0
