import logging

import pytest

from reportportal_client import RPLogger


@pytest.fixture(scope="session", autouse=True)
def rp_logging_setup():
    # 只做一次：接管 logging
    logging.setLoggerClass(RPLogger)

    # 可选：统一日志级别
    root = logging.getLogger()
    root.setLevel(logging.INFO)

import pytest

@pytest.fixture
def mock_user():
    return {
        "id": 1,
        "name": "mock_user",
        "role": "admin"
    }

@pytest.fixture
def mock_order():
    return {
        "order_id": "ORD-001",
        "amount": 99.9,
        "status": "PAID"
    }
