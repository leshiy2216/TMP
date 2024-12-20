import json
import file_utils
import pytest

from unittest.mock import patch, mock_open


@pytest.mark.parametrize("data", [
    ({"step": 1}),
    ({"step": 2, "value": 42}),
])


def test_write_dict_to_json_param(data):
    with patch("builtins.open", mock_open()) as mock_file, patch("json.dump") as mock_json_dump:
        file_utils.write_dict_to_json("dummy_path", data)
        mock_file.assert_called_once_with("dummy_path", 'w', encoding='utf-8')
        mock_json_dump.assert_called_once_with(data, mock_file(), indent=4)


@pytest.mark.parametrize("data", [
    ([("a", 1), ("b", 2)]),
    ([("x", 10), ("y", 20), ("z", 30)]),
])


def test_save_to_text_param(data):
    with patch("builtins.open", mock_open()) as mock_file:
        file_utils.save_to_text(data, "dummy_path")
        mock_file.assert_called_once_with("dummy_path", 'w', encoding='UTF-8')
        handle = mock_file()
        for char, frequency in data:
            handle.write.assert_any_call(f"{char}: {frequency}\n")


def test_read_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError) as mock_file:
        result = file_utils.read_file("dummy_path")
        mock_file.assert_called_once_with("dummy_path", 'r', encoding='utf-8')
        assert result == ""


def test_write_text_to_file_exception():
    mock_text = "some text"
    with patch("builtins.open", side_effect=Exception("Some error")) as mock_file:
        file_utils.write_text_to_file("dummy_path", mock_text)
        mock_file.assert_called_once_with("dummy_path", 'w', encoding='utf-8')


def test_write_decryption_key_with_assert():
    mock_data = {"a": "b"}
    with patch("builtins.open", mock_open()) as mock_file, patch("json.dump") as mock_json_dump:
        file_utils.write_decryption_key("dummy_path", mock_data)
        mock_file.assert_called_once_with("dummy_path", 'w', encoding='utf-8')
        mock_json_dump.assert_called_once_with(mock_data, mock_file(), ensure_ascii=False, indent=4)
        assert mock_json_dump.call_args[0][0] == mock_data


def test_read_settings_with_assert():
    mock_settings = {"crypt_alphabet": "abc", "normal_alphabet": "xyz"}
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_settings))) as mock_file:
        result = file_utils.read_settings("dummy_path")
        mock_file.assert_called_once_with("dummy_path", 'r', encoding='UTF-8')
        assert result == mock_settings
        assert "crypt_alphabet" in result
        assert "normal_alphabet" in result


def test_write_dict_to_json():
    mock_data = {"step": 3}
    with patch("builtins.open", mock_open()) as mock_file, patch("json.dump") as mock_json_dump:
        file_utils.write_dict_to_json("dummy_path", mock_data)
        mock_file.assert_called_once_with("dummy_path", 'w', encoding='utf-8')
        mock_json_dump.assert_called_once_with(mock_data, mock_file(), indent=4)


def test_write_decryption_key():
    mock_data = {"a": "b"}
    with patch("builtins.open", mock_open()) as mock_file, patch("json.dump") as mock_json_dump:
        file_utils.write_decryption_key("dummy_path", mock_data)
        mock_file.assert_called_once_with("dummy_path", 'w', encoding='utf-8')
        mock_json_dump.assert_called_once_with(mock_data, mock_file(), ensure_ascii=False, indent=4)


def test_save_to_json():
    mock_data = {"test": "data"}
    with patch("builtins.open", mock_open()) as mock_file, patch("json.dump") as mock_json_dump:
        file_utils.save_to_json(mock_data, "dummy_path")
        mock_file.assert_called_once_with("dummy_path", 'w')
        mock_json_dump.assert_called_once_with(mock_data, mock_file(), indent=4)


def test_read_file():
    mock_file_content = "file content"
    with patch("builtins.open", mock_open(read_data=mock_file_content)) as mock_file:
        result = file_utils.read_file("dummy_path")
        mock_file.assert_called_once_with("dummy_path", 'r', encoding='utf-8')
        assert result == mock_file_content


def test_write_text_to_file():
    mock_text = "some text"
    with patch("builtins.open", mock_open()) as mock_file:
        file_utils.write_text_to_file("dummy_path", mock_text)
        mock_file.assert_called_once_with("dummy_path", 'w', encoding='utf-8')
        mock_file().write.assert_called_once_with(mock_text)


def test_save_to_text():
    mock_data = [("a", 1), ("b", 2)]
    with patch("builtins.open", mock_open()) as mock_file:
        file_utils.save_to_text(mock_data, "dummy_path")
        mock_file.assert_called_once_with("dummy_path", 'w', encoding='UTF-8')
        handle = mock_file()
        handle.write.assert_any_call("a: 1\n")
        handle.write.assert_any_call("b: 2\n")


def test_read_settings():
    mock_settings = {"crypt_alphabet": "abc", "normal_alphabet": "xyz"}
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_settings))) as mock_file:
        result = file_utils.read_settings("dummy_path")
        mock_file.assert_called_once_with("dummy_path", 'r', encoding='UTF-8')
        assert result == mock_settings