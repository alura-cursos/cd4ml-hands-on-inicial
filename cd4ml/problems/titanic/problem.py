from cd4ml.problems.problem_base import ProblemBase
from cd4ml.problems.titanic.download_data.download_data import download
import cd4ml.problems.titanic.readers.stream_data as stream_data


class Problem(ProblemBase):
    def __init__(self,
                 problem_name,
                 data_downloader='default',
                 feature_set_name='default',
                 ml_pipeline_params_name='default',
                 algorithm_name='default',
                 algorithm_params_name='default'):

        super(Problem, self).__init__(problem_name,
                                      data_downloader=data_downloader,
                                      feature_set_name=feature_set_name,
                                      ml_pipeline_params_name=ml_pipeline_params_name,
                                      algorithm_name=algorithm_name,
                                      algorithm_params_name=algorithm_params_name)
        self._stream_data = stream_data.stream_data

    @staticmethod
    def get_feature_set_constructor(feature_set_name):
        if feature_set_name == 'default':
            import cd4ml.problems.titanic.features.feature_sets.default.feature_set as default_features
            return default_features.get_feature_set
        else:
            raise ValueError("Featureset name {} is not valid".format(feature_set_name))

    def prepare_feature_data(self):
        # do the work required to look up derived features
        pass

    def download_data(self):
        download()
