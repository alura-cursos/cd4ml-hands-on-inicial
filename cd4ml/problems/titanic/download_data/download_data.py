from cd4ml.filenames import get_problem_files
from cd4ml.utils.utils import download_to_file_from_url

baseUri = "https://raw.githubusercontent.com/tiozao/continuous-delivery-for-machine-learning-data/main"

download_params = {
    'url': f"{baseUri}/train.csv"
}


def download(use_cache=True):
    # The simulated house price data
    url = download_params['url']
    file_names = get_problem_files("titanic")
    filename = file_names['raw_titanic_data']

    download_to_file_from_url(url, filename, use_cache=use_cache)
