
from src.utils import to_get_json


from unittest.mock import patch


@patch("json.load")
def test_to_get_json(mock_load):
    mock_load.return_value = [1, 2, 3]
    result = to_get_json("fake_path.json")
    assert result == [1, 2, 3], f"Expected [1, 2, 3], but got {result}"
