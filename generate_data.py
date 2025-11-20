import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

os.makedirs('input', exist_ok=True)

n_samples = 100
sample_ids = [f'S{str(i).zfill(4)}' for i in range(1, n_samples + 1)]

metadata = pd.DataFrame({
    'sample_id': sample_ids,
    'patient_id': [f'P{str(i).zfill(3)}' for i in np.random.randint(1, 51, n_samples)],
    'collection_date': [
        (datetime(2024, 1, 1) + timedelta(days=int(x))).strftime('%Y-%m-%d')
        for x in np.random.randint(0, 365, n_samples)
    ],
    'sample_type': np.random.choice(['blood', 'urine', 'tissue', 'saliva'], n_samples),
    'age': np.random.randint(18, 80, n_samples),
    'gender': np.random.choice(['M', 'F'], n_samples),
    'diagnosis': np.random.choice(['healthy', 'disease_A', 'disease_B', 'disease_C'], n_samples)
})

metadata.to_csv('input/sample_metadata.csv', index=False)
print(f"sample_metadata.csv: {len(metadata)} rows")

existing_samples = list(np.random.choice(sample_ids, 80, replace=False))
new_samples = [f'S{str(i).zfill(4)}' for i in range(101, 121)]
ms_ids = existing_samples + new_samples

ms_results = pd.DataFrame({
    'sample_id': ms_ids,
    'protein_id': [f'PROT{str(i).zfill(5)}' for i in np.random.randint(1, 5000, len(ms_ids))],
    'intensity': np.random.uniform(100, 10000, len(ms_ids)).round(2),
    'mz_ratio': np.random.uniform(300, 2000, len(ms_ids)).round(4),
    'retention_time': np.random.uniform(5, 60, len(ms_ids)).round(2),
    'peptide_count': np.random.randint(1, 20, len(ms_ids)),
    'confidence_score': np.random.uniform(0.5, 1.0, len(ms_ids)).round(3)
})

ms_results.to_csv('input/mass_spec_results.csv', index=False)
print(f"mass_spec_results.csv: {len(ms_results)} rows")

qc_existing = list(np.random.choice(sample_ids, 70, replace=False))
qc_new_ms = [f'S{str(i).zfill(4)}' for i in range(101, 119)]
qc_brand_new = [f'S{str(i).zfill(4)}' for i in range(201, 203)]
qc_ids = qc_existing + qc_new_ms + qc_brand_new

quality = pd.DataFrame({
    'sample_id': qc_ids,
    'ph_level': np.random.uniform(6.5, 8.0, len(qc_ids)).round(2),
    'temperature': np.random.uniform(-20, -18, len(qc_ids)).round(1),
    'contamination_level': np.random.choice(['none', 'low', 'medium', 'high'], 
                                           len(qc_ids), p=[0.7, 0.2, 0.08, 0.02]),
    'storage_days': np.random.randint(1, 365, len(qc_ids)),
    'qc_pass': np.random.choice([True, False], len(qc_ids), p=[0.85, 0.15]),
    'integrity_score': np.random.uniform(0.6, 1.0, len(qc_ids)).round(3)
})

quality.to_csv('input/quality_data.csv', index=False)
print(f"quality_data.csv: {len(quality)} rows")

os.makedirs('output', exist_ok=True)
os.chmod('output', 0o777)
print("\nOutput directory created with permissions 777")
