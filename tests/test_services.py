from src.application.services import SalaryPredictionService, DataSyncService
from src.domain.interfaces import IDataStorage


class MockStorage(IDataStorage):

    def download_file(self, remote_path: str, local_path: str):
        pass

    def upload_file(self, local_path: str, remote_path: str):
        pass


def test_prediction():
    storage = MockStorage()
    sync_service = DataSyncService(storage)
    service = SalaryPredictionService(sync_service)

    # Создайте локальный тестовый файл перед запуском
    result = service.predict_salary(3)

    assert isinstance(result, float)