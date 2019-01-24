import pytest
import redistalker
import os

# test will be performed on separate instance of Redis, kept on another port
# os.system('redis-server /home/kuba/Desktop/redis/redis-stable/redis_test.conf --daemonize yes')

db_test_instance = redistalker.RedisTalker("localhost", 6666)
db_test_instance.connect()

def test_set_method(capsys):
    db_test_instance.set("key_test", "value_test")
    captured = capsys.readouterr()[0]
    assert captured == "Redis response: b'+OK'\n"

def test_get_method(capsys):
    db_test_instance.get("key_test")
    captured = capsys.readouterr()[0]
    assert captured == "Redis response: b'value_test'\n"

def test_connection_to_nonexisting_redis_instance(capsys):
    dummy_instance = redistalker.RedisTalker("dummy localhost", 123456789007)
    dummy_instance.connect()
    captured = capsys.readouterr()[0]
    assert captured == "Connection to Redis failed.\n"

# os.system('redis-cli -h 127.0.0.1 -p 6666 shutdown')
