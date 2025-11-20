import pandas as pd
import sys
from datetime import datetime

def timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def log_msg(msg):
    print(f"[{timestamp()}] {msg}")
    sys.stdout.flush()

def load_datasets():
    log_msg("Reading input files from /data/input...")

    try:
        df_meta = pd.read_csv('/data/input/sample_metadata.csv')
        log_msg(f"  sample_metadata.csv: {len(df_meta)} rows")

        df_ms = pd.read_csv('/data/input/mass_spec_results.csv')
        log_msg(f"  mass_spec_results.csv: {len(df_ms)} rows")

        df_qc = pd.read_csv('/data/input/quality_data.csv')
        log_msg(f"  quality_data.csv: {len(df_qc)} rows")

        return df_meta, df_ms, df_qc

    except Exception as e:
        log_msg(f"Error reading files: {e}")
        sys.exit(1)

def perform_inner_join(df1, df2, df3):
    log_msg("\nINNER JOIN: metadata <-> ms_results <-> quality")

    temp = df1.merge(df2, on='sample_id', how='inner')
    log_msg(f"  Step 1: {len(temp)} rows")

    result = temp.merge(df3, on='sample_id', how='inner')
    log_msg(f"  Final: {len(result)} rows")

    result.to_csv('/data/output/inner_join.csv', index=False)
    log_msg(f"  Saved to /data/output/inner_join.csv")

    return result

def perform_left_join(df1, df2, df3):
    log_msg("\nLEFT JOIN: metadata <- ms_results <- quality")

    temp = df1.merge(df2, on='sample_id', how='left')
    log_msg(f"  Step 1: {len(temp)} rows")

    result = temp.merge(df3, on='sample_id', how='left')
    log_msg(f"  Final: {len(result)} rows")

    nulls = result.isnull().any(axis=1).sum()
    log_msg(f"  Rows with missing data: {nulls}")

    result.to_csv('/data/output/left_join.csv', index=False)
    log_msg(f"  Saved to /data/output/left_join.csv")

    return result

def perform_right_join(df1, df2, df3):
    log_msg("\nRIGHT JOIN: metadata -> ms_results -> quality")

    temp = df1.merge(df2, on='sample_id', how='right')
    log_msg(f"  Step 1: {len(temp)} rows")

    result = temp.merge(df3, on='sample_id', how='right')
    log_msg(f"  Final: {len(result)} rows")

    nulls = result.isnull().any(axis=1).sum()
    log_msg(f"  Rows with missing data: {nulls}")

    result.to_csv('/data/output/right_join.csv', index=False)
    log_msg(f"  Saved to /data/output/right_join.csv")

    return result

def perform_outer_join(df1, df2, df3):
    log_msg("\nOUTER JOIN: metadata <=> ms_results <=> quality")

    temp = df1.merge(df2, on='sample_id', how='outer')
    log_msg(f"  Step 1: {len(temp)} rows")

    result = temp.merge(df3, on='sample_id', how='outer')
    log_msg(f"  Final: {len(result)} rows")

    nulls = result.isnull().any(axis=1).sum()
    log_msg(f"  Rows with missing data: {nulls}")

    result.to_csv('/data/output/outer_join.csv', index=False)
    log_msg(f"  Saved to /data/output/outer_join.csv")

    return result

def main():
    log_msg("Starting join operations")
    log_msg("=" * 70)

    metadata, ms_results, quality = load_datasets()

    log_msg("\n" + "=" * 70)
    log_msg("Executing joins")
    log_msg("=" * 70)

    r_inner = perform_inner_join(metadata, ms_results, quality)
    r_left = perform_left_join(metadata, ms_results, quality)
    r_right = perform_right_join(metadata, ms_results, quality)
    r_outer = perform_outer_join(metadata, ms_results, quality)

    log_msg("\n" + "=" * 70)
    log_msg("Summary statistics")
    log_msg("=" * 70)
    log_msg(f"  INNER: {len(r_inner)} rows")
    log_msg(f"  LEFT:  {len(r_left)} rows")
    log_msg(f"  RIGHT: {len(r_right)} rows")
    log_msg(f"  OUTER: {len(r_outer)} rows")
    log_msg("\nAll operations completed successfully")

if __name__ == "__main__":
    main()
