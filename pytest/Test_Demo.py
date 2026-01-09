class Test_Demo:
    def test_1(self, rp_logger):
        assert 1 == 1, "1 is not equal to 1"
        rp_logger.info("1 is equal to 1")
        rp_logger.debug("1 is equal to 1")
        rp_logger.warning("1 is equal to 1")
        rp_logger.error("1 is equal to 1")
        rp_logger.critical("1 is equal to 1")
