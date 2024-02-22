from csv import DictReader
from cd4ml.filenames import get_problem_files
from cd4ml.utils.utils import float_or_zero


def stream_raw(problem_name):
    """
    :param problem_name: name of problem
    :return: stream to raw rows of titanic sales data
    """
    file_names = get_problem_files(problem_name)
    filename = file_names['raw_titanic_data']
    return (dict(row) for row in DictReader(open(filename, 'r')))


def stream_data(problem_name):
    """
    :param problem_name: name of problem
    :return: stream to processed rows of titanic sales data
    """
    from cd4ml.problems import read_schema_file
    from pathlib import Path
    categorical_fields, numeric_fields = read_schema_file(Path(Path(__file__).parent, "raw_schema.json"))

    return (process_row(row, categorical_fields, numeric_fields) for row in stream_raw(problem_name))


def process_row(row, categorical_fields, numeric_fields):
    """
    Process a raw row of titanic data and give it the right schema
    :param row: raw row
    :param schema: raw_schema_dict
    :return: processed row
    """

    row_out = {k: row[k] for k in categorical_fields}

    for field in numeric_fields:
        row_out[field] = float_or_zero(row[field])

    return row_out
