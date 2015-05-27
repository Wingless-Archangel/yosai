import pytest

from yosai import (
    DefaultAccountCacheHandler,
)

from ..doubles import (
    MockAccount,
)

from .doubles import (
    MockAccountCacheHandler,
    MockAccountCacheResolver,
    MockAccountCacheKeyResolver,
)

@pytest.fixture(scope='function')
def mock_account_cache_resolver():
    return MockAccountCacheResolver()

@pytest.fixture(scope='function')
def mock_account_cache_key_resolver():
    return MockAccountCacheKeyResolver()

@pytest.fixture(scope='function')
def patched_default_account_cache_handler(
        mock_cache_resolver, mock_cache_key_resolver):
    return DefaultAccountCacheHandler(mock_cache_resolver,
                                      mock_cache_key_resolver)

@pytest.fixture(scope='function')
def mock_account_cache_handler():
    return MockAccountCacheHandler(MockAccount(account_id='MACH13579'))


@pytest.fixture(scope='function')
def patched_accountstore_realm(
        default_accountstorerealm, monkeypatch, default_password_matcher, 
        mock_account_cache_handler, mock_account_store):
    dasr = default_accountstorerealm
    dasr.account_cache_handler = mock_account_cache_handler
    dasr.account_store = mock_account_store
    return default_accountstorerealm   