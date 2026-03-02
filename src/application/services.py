from pathlib import Path
import csv
from src.domain.interfaces import IDataStorage


class DataSyncService:

    def __init__(self, storage: IDataStorage):
        self.storage = storage

    def sync_dataset(self, remote_path: str, local_path: str) -> None:
        local_file = Path(local_path)

        if not local_file.exists():
            print("[Sync] Dataset not found locally. Downloading...")
            local_file.parent.mkdir(parents=True, exist_ok=True)
            self.storage.download_file(remote_path, local_path)
        else:
            print("[Sync] Dataset already exists.")


class SalaryPredictionService:

    def __init__(self, sync_service: DataSyncService):
        self.sync_service = sync_service
        self.dataset_path = "data/hr_data.csv"

    def load_data(self):
        with open(self.dataset_path, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)

    def predict_salary(self, experience: int) -> float:
        """
        Простейшая логика:
        средняя зарплата по записям с близким опытом.
        """
        self.sync_service.sync_dataset(
            remote_path="hr_data.csv",
            local_path=self.dataset_path
        )

        data = self.load_data()

        filtered = [
            float(row["salary"])
            for row in data
            if abs(int(row["experience"]) - experience) <= 1
        ]

        if not filtered:
            return 0.0

        return sum(filtered) / len(filtered)