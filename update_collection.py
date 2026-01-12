#!/usr/bin/env python3
"""
Update collection_data.json with new records from a CSV export
"""
import json
import csv
import sys
from pathlib import Path

def read_csv(csv_path):
    """Read CSV file and return list of records"""
    records = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)
    return records

def group_by_format(records):
    """Group records by CollectionFolder"""
    groups = {}
    for record in records:
        folder = record.get('CollectionFolder', 'Unknown')
        if folder not in groups:
            groups[folder] = []
        groups[folder].append(record)
    return groups

def update_collection(existing_json_path, new_csv_path, output_json_path):
    """Merge new CSV records with existing collection"""
    
    # Read existing collection
    if Path(existing_json_path).exists():
        with open(existing_json_path, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
        existing_records = existing_data.get('records', [])
        print(f"✓ Loaded {len(existing_records)} existing records")
    else:
        existing_records = []
        print("! No existing collection found, starting fresh")
    
    # Read new CSV
    new_records = read_csv(new_csv_path)
    print(f"✓ Loaded {len(new_records)} records from CSV")
    
    # Create a set of existing release IDs for quick lookup
    existing_ids = {record['release_id'] for record in existing_records if record.get('release_id')}
    
    # Find new records
    added_count = 0
    for record in new_records:
        release_id = record.get('release_id')
        if release_id and release_id not in existing_ids:
            existing_records.append(record)
            existing_ids.add(release_id)
            added_count += 1
    
    print(f"✓ Added {added_count} new records")
    print(f"✓ Total records: {len(existing_records)}")
    
    # Group by format
    format_groups = group_by_format(existing_records)
    
    # Create updated collection data
    updated_data = {
        'records': existing_records,
        'formats': format_groups
    }
    
    # Save to output file
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(updated_data, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Saved to {output_json_path}")
    
    # Print format breakdown
    print("\nFormat breakdown:")
    for format_name, format_records in sorted(format_groups.items()):
        print(f"  {format_name}: {len(format_records)}")
    
    return added_count

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python update_collection.py <new_csv_file>")
        print("Example: python update_collection.py new-export.csv")
        sys.exit(1)
    
    new_csv = sys.argv[1]
    existing_json = 'collection_data.json'
    output_json = 'collection_data.json'
    
    if not Path(new_csv).exists():
        print(f"Error: CSV file not found: {new_csv}")
        sys.exit(1)
    
    added = update_collection(existing_json, new_csv, output_json)
    
    if added > 0:
        print(f"\n✅ Successfully added {added} new records to collection!")
    else:
        print("\n✅ Collection is up to date - no new records found")
